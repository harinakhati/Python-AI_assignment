#7. Write a program that tracks student attendance across multiple days and prints students who fall below a minimum attendance threshold.

#Attendance Tracker


attendance = {}

days = int(input("Number of days:"))

for _ in range(days):
    present_students = input("Present students:").split(",")

    for student in present_students:
        student = student.strip()
        attendance[student] =attendance.get(student, 0) +1


threshold = int(input("Minimum attendance required:"))

print("Low attendance students:")
for student, count in attendance.items():
    if count<threshold:
        print(student)