#TASK 4: Branching & Decision Making

#Build an academic decision system

attendance = int(input("Enter attendance %:"))
total_marks = float(input("Enter total marks:"))

if attendance<75:
    print("Not eligible")
else:
    if total_marks>= 80:
        print("A")
    elif total_marks>=60 and total_marks<80:
        print("B")
    elif total_marks>=50 and total_marks<60:
        print("C")
    else:
        print("Fail")


#create a scholarship eligibility checker

cgpa = float(input("Enter the cgpa:"))
income = float(input("Enter income:"))
attendance = float(input("Enter attendance:"))
 
if cgpa>=3.7 and income <200000 and attendance>=80:
    print("eligble")
else:
    print("Not eligible")