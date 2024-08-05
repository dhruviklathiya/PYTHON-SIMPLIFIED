# 1. Basic Syntax and Data Types
# Q1: How do you create a list in Python?
# A1:

# Q2: Write a Python function that takes a list of numbers and returns the largest number.
# A2:
def largest_number(numbers):
    return max(numbers)

# 2. Control Flow
# Q3: How do you write an `if` statement in Python to check if a number is positive, negative, or zero?
# A3:

# Q4: Write a loop in Python that prints numbers from 1 to 10.
# A4:
for i in range(1, 11):
    print(i)

# 3. Functions
# Q5: How do you define a function in Python?
# A5:

# Q6: Write a Python function that takes two arguments and returns their sum.
# A6:
def sum_two_numbers(a, b):
    return a + b

# 4. String Manipulation
# Q7: How do you concatenate two strings in Python?
# A7:

# Q8: Write a Python function that takes a string and returns it reversed.
# A8:
def reverse_string(s):
    return s[::-1]

# 5. Lists and List Comprehensions
# Q9: How do you append an item to a list in Python?
# A9:

# Q10: Write a Python list comprehension that generates a list of squares of numbers from 1 to 10.
# A10:
squares = [x**2 for x in range(1, 11)]

# 6. Dictionaries
# Q11: How do you create a dictionary in Python?
# A11:

# Q12: Write a Python function that takes a dictionary and returns a list of its keys.
# A12:
def get_keys(d):
    return list(d.keys())

# 7. File Handling
# Q13: How do you read a file in Python?
# A13:

# Q14: Write a Python function that reads a file and prints its content line by line.
# A14:
def read_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# 8. Modules and Packages
# Q15: How do you import a module in Python?
# A15:

# Q16: Write a Python script that uses the `random` module to generate a random number between 1 and 100.
# A16:
import random
print(random.randint(1, 100))

# 9. Error Handling
# Q17: How do you handle exceptions in Python?
# A17:

# Q18: Write a Python function that divides two numbers and handles the case where the denominator is zero.
# A18:
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# 10. Object-Oriented Programming
# Q19: How do you define a class in Python?
# A19:

# Q20: Write a Python class `Rectangle` that has attributes for width and height and a
