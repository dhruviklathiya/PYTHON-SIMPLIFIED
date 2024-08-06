# Handling ZeroDivisionError

def division(a,b):
    try:
        return a / b
    except ZeroDivisionError as msg:
        print(f"This is because of {msg}")

print(division(10,5)) # Output: 2
print(division(10,0)) # Output: This is because of division by zero