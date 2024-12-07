import json

# Function to convert data into the desired chat format
def convert_to_chat_format(input_data):
    chat_data = []
    for item in input_data:
        # Split the completion into the database type and explanation parts
        completion_parts = item['completion'].split('\nExplanation: ')
        if len(completion_parts) == 2:
            database_type = completion_parts[0].replace('Database Type: ', '').strip()
            explanation = completion_parts[1].strip()
        else:
            # In case the explanation is missing or incorrectly formatted
            database_type = completion_parts[0].strip()
            explanation = "No explanation available."

        # Create chat format messages
        chat_data.append({
            "messages": [
                {"role": "system", "content": "I am a chatbot designed to assign the best database based on a given input query."},
                {"role": "user", "content": item['prompt']},
                {"role": "assistant", "content": f"Database Type: {database_type}\nExplanation: {explanation}"}
            ]
        })
    return chat_data

# Read the input data from a JSON file (replace 'input_data.json' with your actual file name)
input_file = 'formatted_output_with_validation.jsonl'  # Change this to your actual file path

# Load the input data from the file
with open(input_file, 'r') as file:
    input_data = []
    for line in file:
        input_data.append(json.loads(line))

# Convert the data
chat_data = convert_to_chat_format(input_data)

# Save the result to a new file in .jsonl format
output_file = 'validation_data.jsonl'  # Output filename
with open(output_file, 'w') as file:
    for item in chat_data:
        # Write each chat_data item as a single line in the file
        file.write(json.dumps(item) + '\n')

print(f"Conversion complete. Data saved as '{output_file}'.")
