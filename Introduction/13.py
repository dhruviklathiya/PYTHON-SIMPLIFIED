# or , and
_variable1 = 10
_variable2 = 100

if _variable1 or _variable2: # checks if values are present or not
    print("One value is present")
    if _variable1 and _variable2:
        print("Both values are present")
        if _variable1 == _variable2:
                print("Both value are same")
        else:
                print("Both value are different")
    else:
        print("One value is missing")
else:
    print("No value present")