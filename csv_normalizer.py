"""
c. CSV Normalizer
Write a script that reads a CSV where some fields are missing or malformed (e.g., number
fields as text). The script should:
● Detect and correct common data problems
● Fill missing numeric values with the column mean
● Save both clean CSV and a JSON report of data quality issues (counts of errors per
column).
"""

import os
import csv
import json

input_directory = "/home/marie/code/Python-AI_assignment/assignment_data"
report = {}

for root, dirs, files in os.walk(input_directory):
    for filename in files:
        if filename.lower().endswith(".csv"):

            file_path = os.path.join(root, filename)
            rows = []

            try:
                with open(file_path, "r") as file:
                    reader = csv.DictReader(file)
                    fieldnames = reader.fieldnames
                    for row in reader:
                        rows.append(row)

            except Exception as e:
                print(f"Error reading {file_path} as {e}")
                continue

            numeric_columns = []
            file_report = {}

            for column in fieldnames:
                valid_count = 0
                total_checked = 0

                for row in rows:
                    value  = row[column].strip()
                    if value == "":
                        continue
                    total_checked +=1
                    try:
                        float(value)
                        valid_count+=1
                    except:
                        pass

                if total_checked > 0 and valid_count/total_checked >0.5:
                    numeric_columns.append(column)
                    file_report[column] = {"missing":0, "invalid":0}

            means = {}

            for column in numeric_columns:
                valid_values = []

                for row in rows:
                    value = row[column].strip()

                    if value == "":
                        file_report[column]["missing"] +=1
                    else: 
                        try:
                            num = float(value)
                            valid_values.append(num)
                        except:
                            file_report[column]["invalid"] +=1

                if valid_values:
                    means[column] = sum(valid_values) /len(valid_values)
                else:
                    means[column] =0


            for row in rows:
                for column in numeric_columns:
                    value = row[column].strip()

                    if value == "": 
                        row[column] = str(means[column])
                    else:
                        try:
                            float(value)
                        except:
                            row[column] = str(means[column])

            clean_filename = "clean_" +filename
            clean_path = os.path.join(root, clean_filename)

            with open(clean_path, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

            report[filename] = file_report

with open("computed_data/data_quality_report.json", "w") as file:
    json.dump(report, file, indent=4)

print("Directory CSV normalization complete.")
