#5. Write a program that analyzes a paragraph and prints the top 3 most frequent words, ignoring case and punctuation.

import string

text = input("Enter paragraph:").lower()

for p in string.punctuation:
    text = text.replace(p, "")

words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0)+1

sorted_words = sorted(frequency.items(), key= lambda x: x[1], reverse=True)

print("Top 3 words:")
for word, count in sorted_words[:3]:
    print(word, count)
