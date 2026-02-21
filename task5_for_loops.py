#TASK 5: Iteration Using for Loops

#create a marks analyzer

subject = int(input("Enter no. of subjects:"))
total = 0

highest = None
lowest = None

for i in range(subject):
    marks = float(input("Enter marks:"))  

    if highest is None or marks>highest:
       highest = marks

    if lowest is None or marks<lowest:
        lowest = marks

    total += marks
    
average = total/subject


print(f"Total marks obtained of {subject} is {total} and average is {average}.")
print(f"The obtained highest marks is {highest}.")
print(f"The obtained lowest marks is {lowest}.")



