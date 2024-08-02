# elif conditions in python
_variable1 = int(input("Enter your marks: "))

if _variable1>=90:
    print(f"You can have grade A+ with {_variable1} marks")
elif 90>_variable1>=80:
    print(f"You can have grade A with {_variable1} marks")
elif 80>_variable1>=70:
    print(f"You can have grade B+ with {_variable1} marks")
elif 70>_variable1>=60:
    print(f"You can have grade B with {_variable1} marks")
elif 60>_variable1>=50:
    print(f"You can have grade C+ with {_variable1} marks")
elif 50>_variable1>=40:
    print(f"You can have grade C with {_variable1} marks")
else:
    print("Failed \U0001F641\U0001F641")