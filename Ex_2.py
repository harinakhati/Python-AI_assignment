#2. Write a program that tracks multiple login attempts per user and locks the user account after a fixed number of failures.

users = {
    "harina": "pass123",
    "ram": "ram2024",
    "sita": "sita@908"
}

attempts = {}
locked_users = set()
limit = 3

while True:
    user = input("Username: ")
    password = input("Password: ")

    if user not in users:
        print("User does not exist!")
        continue

    if user in locked_users:
        print("Account is locked!")
        continue

    if user not in attempts:
        attempts[user] = 0
        

    if password == users[user]:
        print("Login successful!")
        attempts[user] = 0
        break
    else:
        attempts[user] += 1
        print("Wrong password!")

        if attempts[user] >= limit:
            print("Account locked due to too many failures!")
            locked_users.add(user)
            break