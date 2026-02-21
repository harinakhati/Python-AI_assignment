#Task 1 : Variables & Data Representation

#Creating variables
full_name = "Ram Prakash"
age = 20
cgpa = 3.45
current_semester = 5
enrollment_status = True

#printing value and datatype
print(full_name, type(full_name))
print(age, type(age))
print(cgpa, type(cgpa))
print(current_semester, type(current_semester))
print(enrollment_status, type(enrollment_status))



#Reassigning one variable to different type for observing change
full_name = 30
print(full_name, type(full_name))  #Python just checks type at runtime, not the compile time so it will show datatype as int instead of string



"""Reasoning question

1. How does Python’s dynamic typing influence memory allocation and runtime behavior?

As we have seen in above reassigining example, it clearly shows that python use dynamic typing which means type of variable can be determined at runtime,not a compile time. So the variables itself doesnot have a fixed type as in C, C++, it is just the reference to an object. 

Impact on memory allocation: 
  - Memory is allocated dynamically
  - Objects are created and destroyed at runtime

Impact on runtime behavior
  - Type checking happens during execution
  - Errors are detected only when that line runs

This may increase developer speed, but reduce performance compared to statically typed langaunges.


2. Why is strict type enforcement preferred in system-level software but not in scripting languages?

System-level software must be fast, memory-efficient, highly predictable, that's why languages like C, C++ use strict typing as:
  - types are checked at compile time
  - memory layout os known in advance
  - performance is optimized
  - fewer runtime 

But the scripting languages like Python prioritize:
  - Rapid development
  - Readablity
  - Flexibility

As system-level software cannot afford runtime errors- a mistake may crash the entire operating system."""