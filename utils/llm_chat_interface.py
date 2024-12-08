from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model="ft:gpt-4o-mini-2024-07-18:personal:db-and-explanation:AbxJwl0k"
#model= "gpt-4o"

def create_response(model, client, content):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "I am a chatbot designed to assign the best database based on a given input query. I also provide an explanation based on my choice"}, {"role": "user", "content": content}
        ],
        temperature=1.0,
    )
    return completion

count = 0

with open('../data/training/test.jsonl', 'r') as file:
    for line in file:
        try:
            data = json.loads(line)
            messages = data.get("messages", [])

            query = None
            db_type = None
            explanation = None
            
            for message in messages:
                if message["role"] == "user":
                    query = message["content"].strip()
                elif message["role"] == "assistant":
                    content = message["content"].strip()
                    if "Database Type:" in content:
                        db_type = content.split("Database Type:", 1)[1].split("\n")[0].strip()
                    if "Explanation:" in content:
                        explanation = content.split("Explanation:", 1)[1].strip()
            
            completion = create_response(model, client, query)
            message_content =  completion.choices[0].message.content
            database_type = message_content.split("Database Type:")[1].split("\n")[0].strip()

            

            if database_type == db_type:
                print(str(count) + ". correct - " + db_type)
            else:
                print(str(count) + ". incorrect - " + db_type + " assigned as " + database_type)

            count += 1


        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

