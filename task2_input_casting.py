#TASK 2: User Input, Type Casting & Runtime Errors

#create a basic financial calculator

income = input("Enter your montly income:")
expenses =input("Enter your montly expenses:")


savings = float(income)-float(expenses) #have to use numeic typecast otherwise strings ar egetting subtracted here.

if savings<0:
    print("Deficit")
else:
    print("Savings")

"""
Reasoning questions:

1. Why does Python delay type errors until runtime, unlike compiled languages?
Python is interpreted language, which means code gets executed line by line while in compiled language whole block of code is checked before execution, and even type mismatches are caught at compile time unlike interpreted one where type checking is done when line runs.

This makes developement faste sometime but it is harder to detect issues in large system, and some bugs appear only during execution.


2. How could unvalidated user input compromise real-world systems (e.g., billing, voting)?

Unvalidated user input can 
- break financial system
- cause incorrect transactions
- enable security attacks
 - manipulate voting systems

So validating is essential for security, integrity and system reliablility.
"""
