# TASK: Create infinite division calculator
# Take 2 number user input
# Tell user not to divide value by zero if second entered value is 0

while True:
    try:
        _para1 = int(input("Enter first value: "))
        _para2 = int(input("Enter second value: "))
        print(f"Final output of division is {_para1/_para2}")
        print("Press ctrl+z for exit")
    except ZeroDivisionError:
        print("Please enter non-zero value as divisor")
    except ValueError:
        print("Enter number only as input")