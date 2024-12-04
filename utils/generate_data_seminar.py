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

for i in range(15):
    count = str(random.randint(95, 130))
    if i == 0:
        content = f"Give {count} natural language queries that can run efficiently on Graph databases"
    else:
        content = f"Give another {count} unique natural language queries that can run efficiently on Graph databases"
    completion = generate_training_data(client, content)

    with open(f'../data/graph/output_{i}.txt', 'w') as f:
        f.write(completion.choices[0].message.content)
        f.close()

