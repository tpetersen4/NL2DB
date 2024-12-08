import json
import csv

def prepare_for_llm(input_filename, output_filename):
    with open(input_filename, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)  # Read the CSV as a dictionary (header as keys)
        
        # Open the output file for JSONL
        with open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
            for row in reader:
                nl_query = row['nl_query']
                db_type = row['db']
                explanation = row['explanation']
                
                # Prepare the prompt and completion
                prompt = f"Query: {nl_query}\n"
                completion = f"Database Type: {db_type}\nExplanation: {explanation}"
                
                # Create a dictionary for the JSONL format
                data = {
                    "prompt": prompt,
                    "completion": completion
                }
                
                # Write the data to the JSONL file
                json.dump(data, outfile)
                outfile.write("\n")
# Example usage:
prepare_for_llm('../data/model/test.csv', 'test.jsonl')
