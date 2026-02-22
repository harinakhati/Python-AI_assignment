#9. Write a program that simulates seat booking for a small event, tracking available seats and preventing overbooking.

#Seat booking system

total_seats = int(input("Total no. of seats:"))
booked = 0

while True:
    request = input("Seats to book:")
    if request == "done":
        break

    seats = int(request)

    if booked + seats <= total_seats:
        booked+=seats
        print("Booked successfully!")
    else:
        print("Not enough seats")

print("Remaining seats:", total_seats-booked)