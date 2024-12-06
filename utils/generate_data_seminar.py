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

for i in range(8, 14):
    count = str(random.randint(32, 40))
    # count = 5
    nested_query = "Identify the top 20 articles with the longest read time from users in different countries, during the last six months, and categorize these by the common top keyword phrases found within user comments."
    if i == 0:
        content = f"Give {count} natural language queries that would run efficiently on Non-relational databases like NoSql and very less efficient on other databases also explain why? the query should be a complex like this one {nested_query}"
    else:
        content = f"Give another {count} natural language queries that would run efficiently on Non-relational databases like NoSql and very less efficient on other databases also explain why? the query should be a complex like this one {nested_query}"

    completion = generate_training_data(client, content)

    # print(completion.choices[0].message.content)
    with open(f'../data/nosql/query_explaination/output_{i}.txt', 'w') as f:
        f.write(completion.choices[0].message.content)
        f.close()

