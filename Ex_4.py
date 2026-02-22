#4. Write a program that records multiple temperature readings per city and prints the average temperature for each city.

temps = {}

while True:
    city  = input("City:")
    if city == "done":
        break

    temp = float(input("Temperature:"))
    
    if city not in temps:
        temps[city] = []

    temps[city].append(temp)


for city in temps:
    avg = sum(temps[city])/ len(temps[city])
    print(city, "Average:", avg)