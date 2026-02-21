#TASK 9: Mini System Integration Task

#Build a menu-driven student utility system

#Student details
name = ""
age = 0
faculty = ""
semester = ""
marks = []
average = 0
grade = ""

#Enter student details
def student_details():
    global name, age, faculty, semester

    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    faculty = input("Enter your faculty name:")
    semester = input("Enter semester:")

    print("Student details saved successfully.\n")

#Enter marks
def enter_marks():
    global marks, average, grade

    marks=[]
    subjects = int(input("Enter no. of subjects:"))

    for i in range(subjects):
        mark = float(input(f"Enter marks for subject {i+1}:"))
        marks.append(mark)

    #calculate average
    average= sum(marks)/len(marks)

    #Determine grade
    if average>=80:
        grade = "A"
    elif average>=60:
        grade = "B"
    elif average>=50:
        grade = "C"
    elif average>=40:
        grade = "D"
    else:
        grade = "Fail"

    print("Marks saved successfully.\n")


#view result summary

def view_result():
    if name=="":
        print("Student details not found.")
        return
    
    if not marks:
        print("No marks details entered.\n")
        return 
    
    print("Result summary:\n")
    print("Name:", name)
    print("Age:", age)
    print("Faculty:", faculty)
    print("Semester:", semester)
    print("Marks:", marks)
    print("Average:", round(average,2))
    print("Grade:", grade)


#Main program
while True:
    print("Student Utility System:")
    print("1.Enter student details")
    print("2.Enter marks")
    print("3.View result summary")
    print("4.Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        student_details()
    elif choice == "2":
        enter_marks()
    elif choice == "3":
        view_result()
    elif choice == "4":
        print("Existing program...")
        break
    else:
        print("Invalid choice! Try again!\n")    



"""
Reasoning questions

1. What changes would be required to convert this into a web application?
To convert this console program into web application:
    - We have to use HTLM form
    - Use web response rendering
    - store data in databases instead of variable
    - use backend framework
    - user authentication implementation
    - deploy on server

Web application will be of multi user, server-based, database and secure input validation will also be required.
While core logic remains same, interface will change.
# """





