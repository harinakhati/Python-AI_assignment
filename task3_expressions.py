#TASK 3: Arithmetic Logic & Expressions

#create a student performance score

assignment_score = float(input("Enter assignment score:"))
lab_score = float(input("Enter lab score:"))
exam_score = float(input("Enter exam score:"))

final_score = (assignment_score*0.3)+(lab_score*0.2)+(exam_score*0.5)  #30%- assignment, 20%- lab, 50%- exam


print(f"The final score of student with assignment score:{assignment_score}, lab score:{lab_score} and exam score:{exam_score} is {final_score}")

"""
Reasoning questions

1. Why is operator precedence critical in scientific or financial software?

Operator precedence determines the order in which expressions are evaluated, as we have famous BODMAS rule.

In scientific systems:
  - A wrong formula can lead to incorrect results
  - Incorrect physics calculations

In financial systems:
  - A small mistake in interst formula may cause major financial loss

Therefore, it is important to main the orders of parentheis and correct evaluations.



2. How could floating-point precision errors affect real-world applications?

Computers represent decimal numbers into binary format, while some decimals values cannot be represented exactly in decimal which impacts directly into real world applications. For example:

In banking system:
  - Rounding errors may accumulate.
  - Repeated transactions may cause imbalance

In scientific simulations:
  - Small precision errors ma grow over iterations

Solutions to these:
  - use decimal libraries
  - use rounding carefully
  - avoid direct equality comparison of floats
"""