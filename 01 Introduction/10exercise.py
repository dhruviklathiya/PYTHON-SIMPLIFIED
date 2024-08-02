# Take 2 input from user
    # First input is name
    # Second input is character

# Run program and print length of name & character repetition in name
_string,_check = input("Enter name and character seperated by comma").split(",")
print(f"Your input is {len(_string)} large & '{_check}' is repeated {_string.count(_check)} times in string")
# Advance version => Will count repetition without case-sensitivity
print(f"Your input is {len(_string)} large & '{_check}' is repeated {_string.lower().count(_check.lower())} times in string")