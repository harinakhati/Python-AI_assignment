"""
Given a text file containing mixed structured records (name, email, phone number), use
regex to parse valid entries and output:
● A deduplicated set of all emails
● A list of names with valid phone numbers only
Save results to a JSON file with schema { "emails": [...], "contacts":
[...] }.
"""

import os
import re
import json

input_directory= "/home/marie/code/Python-AI_assignment/assignment_data"

email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
phone_pattern = re.compile(r'^\d{10}$')

emails = set()
contacts = []

for root, dirs, files in os.walk(input_directory):
    for filename in files:
        if filename.endswith(".txt"):
            file_path = os.path.join(root, filename)

            try:
                with open(file_path, "r") as file:
                    for line in file:
                        line = line.strip()

                        if not line:
                            continue

                        parts = [p.strip() for p in line.split(",")]

                        if len(parts) !=3:
                            continue

                        name, email, phone = parts

                        if email_pattern.fullmatch(email):
                            emails.add(email)

                        if phone_pattern.fullmatch(phone):
                            contacts.append({
                                "name":name,
                                "phone":phone
                            })

            except Exception as e:
                print(f"Error reading {file_path}:{e}")

output_data = {
    "emails": list(emails),
    "contacts": contacts
}

with open("computed_data/output.json", "w") as json_file:
    json.dump(output_data, json_file, indent=4)

print("Processing complete.")

