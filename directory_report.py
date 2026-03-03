"""
Scan all files in a folder recursively and produce:
● A JSON file listing each file path, size, and last modified timestamp
● A set of unique file extensions
● A count of how many files per extension type
Handle permission exceptions and skip unreadable files cleanly.
"""

import os
import json
from datetime import datetime

def generate_report(scan_dir, output_dir):

    os.makedirs(output_dir, exist_ok=True)

    file_report = []
    unique_extensions = set()
    extension_count = {}

    for root, dirs, files in os.walk(scan_dir):
        for file in files:

            full_path = os.path.join(root, file)

            try:
                size = os.path.getsize(full_path)
                modified_time = os.path.getmtime(full_path)

                readable_time = datetime.fromtimestamp(modified_time).strftime("%Y-%m-%d %H:%M:%S")
            except PermissionError:
                print(f"Skipping (Permission Denied): {full_path}")
                continue
            except OSError:
                print(F"skipping (OS Error):{full_path}")
                continue

            _, ext = os.path.splitext(file) 

            if ext:
                unique_extensions.add(ext)
                extension_count[ext] = extension_count.get(ext, 0) +1
            else:
                unique_extensions.add("NO_EXTENSION")
                extension_count["NO_EXTENSION"] = extension_count.get("NO_EXTENSION", 0) +1

            
            file_report.append({
                "path":full_path,
                "size":size,
                "modified": readable_time
            })

    final_report = {
        "files": file_report,
        "unique_extensions": list(unique_extensions),
        "extension_counts": extension_count
    }

    output_path = os.path.join(output_dir, "directory_report.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_report, f, indent=4)

    print("\nDirectory scan complete.")
    print(f"Total files scanned: {len(file_report)}")
    print(f"Unique extensions: {unique_extensions}")
    print(f"Extension counts: {extension_count}")
    print(f"Report saved to: {output_path}")

if __name__ == "__main__":
    
    scan_directory = "/home/marie/code/Python-AI_assignment/assignment_data"
    output_directory = "computed_data"

    generate_report(scan_directory, output_directory)