#8. Write a program that processes multiple customer orders, calculates the total bill per customer, and applies a discount rule based on total amount.

orders = {}

while True:
    customer = input("Customer:")
    if customer == "done":
        break

    amount = float(input("Order amount:"))

    orders[customer] = orders.get(customer, 0)+ amount


for customer, total in orders.items():
    if total>5000: #for example
        total *=0.3
    print(customer, "Final bill:", total)
