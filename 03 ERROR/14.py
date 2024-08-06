# try - except - else

try:
    print("=== Try block execution start")
    # print(10/5)
    print(10/0) # Uncomment to run except block
    print("Try block execution end ===")
except ZeroDivisionError as msg:
    print("=== Except block execution start")
    print(f"Error is {msg}")
    print("Except block execution End ===")
else: # will be run if no error found
    print("=== Else block execution start")
    print("Good to go")
    print("Else block execution End ===")