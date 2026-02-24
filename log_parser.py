"""
Write a script that reads multiple log files in a directory, extracts all log entries with severity ERROR or WARNING, and outputs:
● A CSV file with columns: timestamp, log level, message
● A JSON summary of counts per severity level
Handle malformed lines gracefully using regex.
"""

import os
import re
import csv
import json



log_directory = "/home/marie/code/Python-AI_assignment/assignment_data"

# print("files found:", os.listdir(log_directory))

#Regex pattern
pattern = re.compile(
    r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+\[(ERROR|WARNING)\]\s+(.*)$'
)

parsed_logs = []
summary = {"ERROR":0, "WARNING": 0}


for root, dirs, files in os.walk(log_directory):
    for filename in files:
        file_path = os.path.join(root, filename)

        try:
            with open(file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    match = pattern.match(line)

                    # print("Reading file:", file_path)
                    # print("Line:", line)

                    if match:
                        timestamp, level, message = match.groups()                           
                        parsed_logs.append((timestamp, level, message))
                        summary[level]+=1
                    else:
                        continue #malinformed
        except Exception as e:
            print(f"Error reading {filename}:{e}")


with open("computed_data/output.csv", "w", newline="") as csvfile:
    writer= csv.writer(csvfile)
    writer.writerow(["timestamp", "log level", "message"])
    writer.writerows(parsed_logs)


with open("computed_data/summary.json", "w") as jsonfile:
    json.dump(summary, jsonfile, indent=4)

print("Processing complete.")