"""
Build a script that takes multiple JSON files (each with potentially different keys) and:
● Extracts a unified set of fields based on a mapping config
● Outputs a combined CSV with consistent columns
Your script should dynamically handle missing keys per record.
"""

import os
import json
import csv

def json_to_csv(input_dir, output_dir, mapping_config):

    os.makedirs(output_dir, exist_ok=True)

    unified_fields = list(mapping_config.keys())
    combined_records = []

    for filename in os.listdir(input_dir):

        file_path = os.path.join(input_dir, filename)

        if not os.path.isfile(file_path):
            continue

        data = []

        if filename.lower().endswith(".json"):
            with open(file_path, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    continue

        elif filename.lower().endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                try:
                    data = json.loads(file.read())
                except:
                    continue

        elif filename.lower().endswith(".csv"):
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                data = list(reader)

        else:
            continue


        # Convert dict → list
        if isinstance(data, dict):
            data = [data]


        # Process each record
        for record in data:

            unified_record = {}

            for unified_key, possible_keys in mapping_config.items():

                value = ""

                for key in possible_keys:
                    if key in record:
                        value = record[key]
                        break

                unified_record[unified_key] = value

            combined_records.append(unified_record)


    output_file = os.path.join(output_dir, "combined_output.csv")

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=unified_fields)

        writer.writeheader()
        writer.writerows(combined_records)



mapping = {
    "name": ["name", "full_name"],
    "email": ["email"],
    "age": ["age"]
}

input_directory = "/home/marie/code/Python-AI_assignment/assignment_data"
output_directory = "computed_data"

json_to_csv(input_directory, output_directory, mapping)