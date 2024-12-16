from openai import OpenAI
import os
import json
from dotenv import load_dotenv
import pickle
from tqdm import tqdm

load_dotenv()


#model= "gpt-4o"

def create_response(content, model, client):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "I am a chatbot designed to assign the best database based on a given input query. I also provide an explanation based on my choice"}, {"role": "user", "content": content}
        ],
        temperature=1.0,
    )
    return completion



# Function to run the test and collect results
def run_test(file_path, model, client, iterations=10):
    results = {}

    for run in range(iterations):
        print(f"Starting run {run + 1}/{iterations}")
        count = 0

        with open(file_path, 'r') as file:
            lines = file.readlines()
            for idx, line in tqdm(enumerate(lines), total=len(lines), desc=f"Run {run + 1}/{iterations}", unit="line"):
                try:
                    data = json.loads(line)
                    messages = data.get("messages", [])

                    query = None
                    db_type = None

                    for message in messages:
                        if message["role"] == "user":
                            query = message["content"].strip()
                        elif message["role"] == "assistant":
                            content = message["content"].strip()
                            if "Database Type:" in content:
                                db_type = content.split("Database Type:", 1)[1].split("\n")[0].strip()

                    if query is None or db_type is None:
                        print(f"Warning: Missing query or database type in line {idx + 1}")
                        continue

                    print(f"Processing query: {query}")
                    completion = create_response(query, model, client)
                    message_content = completion.choices[0].message.content
                    database_type = message_content.split("Database Type:")[1].split("\n")[0].strip()
                    database_type = database_type.lower()

                    if query not in results:
                        results[query] = []

                    results[query].append({
                        "run": run + 1,
                        "expected": db_type,
                        "predicted": database_type,
                        "correct": database_type == db_type
                    })

                    count += 1

                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in line {idx + 1}: {e}")

        print(f"Run {run + 1} completed. {count} queries processed.")

    return results

# Save results to a pickle file
def save_results_to_pickle(results, output_path):
    with open(output_path, 'wb') as f:
        pickle.dump(results, f)

# Example usage
if __name__ == "__main__":
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model="ft:gpt-4o-mini-2024-07-18:personal:db-and-explanation:AbxJwl0k"

    file_path = '../data/training/test.jsonl'
    output_path = 'results.pkl'

    print("Starting the test runs...")
    results = run_test(file_path, model=model, client=client, iterations=10)
    save_results_to_pickle(results, output_path)

    print(f"Results saved to {output_path}")
