"""
Write a program that:
● Reads a large unstructured text file
● Extracts only valid IP addresses, dates, and email addresses using regex
● Aggregates these into separate CSV files
● Outputs a final JSON report of how many of each type were found
Handle overlapping matches and avoid partial capture conflicts.
"""

import os
import json
import re

def regex_data_cleaner(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    date_pattern = r"\b\d{4}-\d{2}-\d{2}\b"
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

    ip_count = 0
    date_count = 0
    email_count = 0

    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        if not os.path.isfile(file_path):
            continue

        if not filename.lower().endswith(".txt"):
            continue

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:

                ips = re.findall(ip_pattern, line)
                dates = re.findall(date_pattern, line)
                emails = re.findall(email_pattern, line)

                ip_count +=len(ips)
                date_count +=len(dates)
                email_count +=len(emails)

    report = {
        "ips": ip_count,
        "dates": date_count,
        "emails": email_count
    }

    output_file = os.path.join(output_dir, "regex_report.json")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

input_directory = "assignment_data"
output_directory = "computed_data"

regex_data_cleaner(input_directory, output_directory)