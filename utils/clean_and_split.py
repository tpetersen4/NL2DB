from openai import OpenAI
import pandas as pd
from sklearn.model_selection import train_test_split
import os
import csv


def clean_text(text):
    if isinstance(text, str):
        text = ' '.join(text.strip().split())
        text = text.replace(", ", ",").replace(" ,", ",")
        text = text.replace(". ", ".").replace(" .", ". ")
        text = text.replace('"', '')
        return text
    return text

def add_quotes_to_csv(input_filename, output_filename):
    with open(input_filename, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        
        # Open the output file
        with open(output_filename, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile, quotechar='"', quoting=csv.QUOTE_ALL)  # Ensure quoting
            
            for row in reader:
                # Convert all entries to strings and write the row
                quoted_row = [str(cell) for cell in row]
                writer.writerow(quoted_row)

data = pd.read_csv("../data/final_training_data_explanation.csv")

data['nl_query'] = data['nl_query'].apply(clean_text)
data['explanation'] = data['explanation'].apply(clean_text)
data['db'] = data['db'].apply(clean_text)

train_data, temp_data = train_test_split(data, test_size=0.2, random_state=100)
val_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=100)

train_data.to_csv("../data/model/train_temp.csv", index=False)
val_data.to_csv("../data/model/validation_temp.csv", index=False)
test_data.to_csv("../data/model/test_temp.csv", index=False)

add_quotes_to_csv("../data/model/train_temp.csv", "../data/model/train.csv")
add_quotes_to_csv("../data/model/validation_temp.csv", "../data/model/validation.csv")
add_quotes_to_csv("../data/model/test_temp.csv", "../data/model/test.csv")

