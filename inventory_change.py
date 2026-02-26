"""
You have two CSV files representing inventory snapshots at times T1 and T2.
Write a script that:
● Reads both CSVs into dictionaries
● Outputs added, removed, and quantity-changed items
Results should be saved to JSON and printed in a human-friendly report.
"""

import os
import csv
import json

def read_inventory(file_path):
    inventory = {}

    with open(file_path, newline ='', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) !=2:
                continue

            item = row[0].strip()

            try:
                quantity = int(row[1].strip())
            except ValueError:
                continue

            inventory[item] = quantity
        
    return inventory


def compare_inventory(t1, t2):

    t1_keys = set(t1.keys())
    t2_keys = set(t2.keys())

    added = t2_keys - t1_keys
    removed = t1_keys - t2_keys
    common = t1_keys & t2_keys

    quantity_changed = {}

    for item in common:
        if t1[item] != t2[item]:
            quantity_changed[item] = {
                "T1" : t1[item],
                "T2" : t2[item]
            }

    return {
        "added" : {item: t2[item] for item in added},
        "removed" :{item: t1[item] for item in removed},
        "quantity_changed": quantity_changed
    }


def print_report(name, result):

    print(f"\nInventory Change Report : {name}\n")

    print("Added Items:")
    if result["added"]:
        for item, qty in result["added"].items():
            print(f" +{item}:{qty}")
    else:
        print("None")

    print("\nRemoved Items:")
    if result["removed"]:
        for item, qty in result["removed"].items():
            print(f" -{item}:{qty}")
    else:
        print("None")

    print("\nQuantity Changed:")
    if result["quantity_changed"]:
        for item, values in result["quantity_changed"].items():
            print(f" *{item}:{values['T1']} -> {values['T2']}")
    else:
        print("None")


def process_directory(input_dir, output_dir):

    os.makedirs(output_dir, exist_ok=True)

    file_groups = {}

    for filename in os.listdir(input_dir):

        if not filename.endswith(".csv"):
            continue

        if filename.endswith("_t1.csv"):
            prefix = filename[:-7]
            file_groups.setdefault(prefix, {})["T1"] = filename

        elif filename.endswith("_t2.csv"):
            prefix = filename[:-7]
            file_groups.setdefault(prefix, {})["T2"] = filename

    for prefix, files in file_groups.items():

        if "T1" not in files or "T2"not in files:
            print(f"Skipping {prefix} (missing T1 or T2)")
            continue

        t1_path = os.path.join(input_dir, files["T1"])
        t2_path = os.path.join(input_dir, files["T2"])

        t1_inventory = read_inventory(t1_path)
        t2_inventory = read_inventory(t2_path)

        result = compare_inventory(t1_inventory, t2_inventory)


        output_path = os.path.join(output_dir, f"{prefix}_changes.json")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4)

        print_report(prefix, result)


if __name__ == "__main__":

    input_directory = "/home/marie/code/Python-AI_assignment/assignment_data"
    output_directory = "computed_data/"

    process_directory(input_directory, output_directory)