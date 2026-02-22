#3. Write a program that simulates inventory stock updates, where items are added and removed over time, and reports which items are out of stock.

#Inventory stock system

inventory = {}

while True:
    action = input("add/remove/done:")

    if action == "done":
        break

    item = input("Item name:")
    quantity = int(input("Quantity:"))

    if item not in inventory:
        inventory[item] = 0

    if action == "add":
        inventory[item] += quantity
    elif action == "remove":
        inventory[item] -=quantity
    else:
        break


for item, qty in inventory.items():
    if qty<=0:
        print("Out of stock:", item)
        