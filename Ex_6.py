#6. Write a program that manages multiple bank accounts, allowing deposits and withdrawals, and prints accounts with negative balance.

#Bank Account Management

accounts = {}

while True:
    action = input("deposit/withdraw/done:")
    if action == "done":
        break

    name = input("Account name:")
    amount = float(input("Amount:"))

    if name not in accounts:
        accounts[name] = 0

    if action == "deposit":
        accounts[name] +=amount
    elif action == "withdraw":
        accounts[name] -=amount
    else:
        break

for name, balance in accounts.items():
    if balance<0:
        print("Accounts with negative balance:")
        print(name, balance)