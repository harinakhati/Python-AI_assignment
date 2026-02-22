#1. Write a program that records daily expenses by category (e.g., food, travel, rent) and prints which category consumed the highest total amount.

#Daily Expense Tracker

expenses = {}

while True:
    category = input("Enter category:").lower()
    if category == "done":
        break

    amount = float(input("Enter amount:"))

    if category in expenses:
        expenses[category] +=amount
    else:
        expenses[category] = amount

highest = max(expenses, key = expenses.get)
print("Highest expense category:", highest)
print("Amount:", expenses[highest])