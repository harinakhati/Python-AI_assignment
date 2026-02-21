#TASK 7: String Processing & Traversal

sentence = input("Enter a sentence:")
vowels= 0
consonants = 0
digits = 0
space = 0

for char in sentence:
    if char.lower() in "aeiou":
        vowels+=1
    elif char.isalpha():
        consonants+=1
    elif char.isdigit():
        digits+=1
    elif char.isspace():
        space+=1
    
print(f"Counts of vowels: {vowels}, consonants: {consonants}, digits:{digits} and spaces: {space}.")
    
print(f"The sentence in upper case is: {sentence.upper()}.")
print(f"The sentence in lower case is: {sentence.lower()}.")

print(f"Sentence without extra spaces: {" ".join(sentence.split())}.")

"""
Reasoning questions

1. Why is string processing critical in cybersecurity and NLP?
In cybersecurity, if string processing is weak, security risk increases.
  - Password validation requires string checks.
  - Log monitoring involves parsing text.
  - Detecting malicious patterns involve string analysis.

In NLP, models perform poorly if string processing is weak.
  - Tokenization
  - Sentiment analysis
  - Language translation
  - Chatbots


2. How can improper string handling introduce vulnerabilities?
Improper string handling may cause:
  SQL injection -if user input is directly added to query string.
  Command injection -if input is executed as system command.
  Buffer overflow -When string exceeds allocated memory.

Therefore, we should be always validate, sanitized input and avoid direct concatenation in sensitive contexts.

"""