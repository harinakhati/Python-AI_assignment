"""
Write a program that analyzes text data from multiple files to produce:
● A list of the top 100 most common words
● A dictionary mapping each word to its count
A set of words longer than 7 characters
Use efficient data structures and avoid loading entire files into memory at once.
"""


import os
import re
import json
import heapq

def analyze_text(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    word_counts = {}

    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)

        if not os.path.isfile(file_path):
            continue

        with open(file_path, "r", encoding= "utf-8") as file:
            for line in file:
                line = line.lower()
                line = re.sub(r"[^\w\s]", "", line)

                words = line.split()

                for word in words:
                    word_counts[word] = word_counts.get(word, 0) + 1

    top_100 = heapq.nlargest(100, word_counts.items(), key=lambda x: x[1])

    long_words = {word for word in word_counts if len(word) > 7}

    with open(os.path.join(output_dir, "word_counts.json"), "w") as f:
        json.dump(word_counts, f, indent=2)

    with open(os.path.join(output_dir, "top_100.json"), "w") as f:
        json.dump(list(long_words), f, indent=2)

input_directory = "/home/marie/code/Python-AI_assignment/assignment_data"
output_directory = "computed_data"
analyze_text(input_directory, output_directory)

