"""
Given a deeply nested JSON file (user profiles with activity logs), write functions to:
● Extract all user IDs who have performed a specific action
● Count how many times each action occurred
● Output a sorted list of actions by frequency
You should use dictionary logic and comprehension.
"""


import json
import os

input_directory = "/home/marie/code/Python-AI_assignment/assignment_data"
output_directory = "computed_data"
target_action = "upload"

os.makedirs(output_directory, exist_ok=True)

def load_all_users_from_directory(directory):
    all_users = []

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)

            try:
                with open(filepath, "r") as f:
                    data = json.load(f)

                    if isinstance(data, list):
                        all_users.extend(data)
                    else:
                        print(f"Skipping {filename}: Not a list structure")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return all_users

def get_users_by_action(users, target_action):
    return[
        user["user_id"]
        for user in users
        if any(
            activity["action"] == target_action
               for activity in user["profile"]["activity"]
               )
    ]

def count_actions(users):
    action_counts = {}

    for user in users:
        for activity in user["profile"]["activity"]:
            action = activity["action"]
            count = activity["count"]

            action_counts[action] = action_counts.get(action, 0) + count
    
    return action_counts

def sort_actions_by_frequency(action_counts):
    return sorted(
        action_counts.items(),
        key = lambda x: x[1],
        reverse=True
    )

users = load_all_users_from_directory(input_directory)

users_with_upload = get_users_by_action(users, "upload")
action_counts = count_actions(users)
sorted_actions = sort_actions_by_frequency(action_counts)   

output_data ={
        "users_with_target_action": users_with_upload,
        "action_counts": action_counts,
        "sorted_actions": sorted_actions
        }             

output_path = os.path.join(output_directory, "nested_json_result.json")

with open(output_path, "w") as f:
    json.dump(output_data, f, indent=4)

print("All json files processed.")
print("Ouput saved successfully.")


