# Python custom error
    # We can provide our custom name to error so that readability of code increase
        # Custom errors are nothing more than extending or inheriting python in-built ERROR classes
# Example

class CUSTOMERROR(ZeroDivisionError):
    pass

class MUSTBEDECIMALVALUE(ValueError):
    pass

while True:
    try:
        _para1 = int(input("Enter first value: "))
        _para2 = int(input("Enter second value: "))
        print(f"Final output of division is {_para1/_para2}")
        print("Press ctrl+z for exit")
    except ZeroDivisionError:
        raise CUSTOMERROR("Please enter non-zero value as divisor")
    except ValueError:
        raise MUSTBEDECIMALVALUE("Enter number only as input")