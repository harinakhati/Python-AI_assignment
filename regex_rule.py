"""
Create a module with regex-based validation functions for:
● Username rules (start with a letter, no spaces, no trailing underscore)
● Password rules (min 10 chars, uppercase, digit, special char)
● Email validation
● Then write a CLI interface that reads user input CSV and validates each row’s
credentials, outputting results to a new CSV.
"""

import os
import re
import csv
import sys

def validate_username(username):
    pattern = r'^[A-Za-z][A-Za-z0-9_]*[A-Za-z0-9]$'
    return re.fullmatch(pattern, username) is not None

def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{10,}$'
    return re.fullmatch(pattern, password) is not None

def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.fullmatch(pattern, email) is not None

def validate_row(username, password, email):

    if not validate_username(username):
        return "INVALID USERNAME"
    
    if not validate_password(password):
        return "INVALID PASSWORD"
    
    if not validate_email(email):
        return "INVALID EMAIL"
    
    return "VALID"


def process_directory(input_dir, output_dir):
    
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):

        if filename.endswith(".csv"):

            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with open(input_path, newline='', encoding='utf-8') as infile, \
                  open(output_path, 'w', newline='', encoding='utf-8') as outfile:
                reader = csv.DictReader(infile)
                fieldnames = reader.fieldnames+ ["RESULT"]

                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in reader:

                    username = row.get("username", "")
                    password = row.get("password", "")
                    email = row.get("email", "")

                    result = validate_row(username, password, email)

                    row["RESULT"] = result
                    writer.writerow(row)

        print(f"Processed: {filename}")


if __name__ == "__main__":
    input_directory = "/home/marie/code/Python-AI_assignment/assignment_data"
    output_directory = "computed_data/"

    process_directory(input_directory,output_directory)