#TASK 8: Functions

#Create reusable functions

def calculate_average(total,subjects):
    return total/subjects

def determine_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
    

def format_output(total, average, grade):
    print("\nResult Summary")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")


#main program
subjects= int(input("Enter no. of subjects:"))
total = 0

for marks in range(subjects):
    marks= float(input("Enter marks:"))
    total+=marks

average = calculate_average(total, subjects)
grade = determine_grade(average)

format_output(total, average, grade)

"""
Conceptual questions

1. Why is returning values better than printing inside functions?
Printing inside a function limits reusability, makes testing difficult while returning value separates computation from display, allow reuse in other program, also improves modularity with making unit testing easier.

Returning values follow principles:
  - Separation of concerns
  - Modularity
  - Reusability
"""