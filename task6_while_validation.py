#TASK 6: Input Validation with while Loops

while True:
    try:
        marks = float(input("Enter subject marks:"))
        if int(marks) in range(0,101):
            break
        else:
            print("Invalid")
    except ValueError:
        print("Invalid")



"""Conceptual question:

1. Why is validation better handled with while loops than for loops?

For loop run a fixed number of times and validations doesnot depend on count, it depends on correctness of input. Therefore, validation requires condition-based repetition and while loop is logically correct for uncertain number of attempts as we have seen in above use-case.
"""