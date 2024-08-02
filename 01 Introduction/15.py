# use of 'in' keyword in python

if 'A' in 'ANTMAN':
    print("A is present")
else:
    print("A is not present")

# Checking presence of variables
_variable1 = 10
# _variable2 = 100
_variable2 = None

if _variable1:
    print("_variable1 is in code")
else:
    print("_variable1 is not in code")

if _variable2:
    print("_variable2 is in code")
else:
    print("_variable2 is not in code")


# Both combined
if _variable1 and _variable2:
    print("_variable1 & _variable2 are in code")
else:
    if not _variable1:
        print("_variable1 is missing")
    elif not _variable2:
        print("_variable2 is missing")
    else:
        print("Both variable are missing")