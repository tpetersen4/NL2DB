from openai import OpenAI
from dotenv import load_dotenv
import os
import random

load_dotenv()

def generate_training_data(client, content):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": content}
        ],
        temperature=1.0,
    )

    return completion

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

for i in range(9, 14):
    count = str(random.randint(32, 40))
    # count = 5
    nested_query = "Find all cities connected by fewer than four flights to a major hub and identify which have experienced an increase in passengers over the past year."
    if i == 0:
        content = f"Give {count} natural language queries that would run efficiently on Graph databases and less efficient on other databases also explain why? they should be complex queries like {nested_query}."
    else:
        content = f"Give another {count} natural language queries that would run efficiently on Graph databases and less efficient on other databases also explain why? they should be complex queries like {nested_query}."

    completion = generate_training_data(client, content)

    # print(completion.choices[0].message.content)
    with open(f'../data/graph/query_explaination/output_{i}.txt', 'w') as f:
        f.write(completion.choices[0].message.content)
        f.close()

