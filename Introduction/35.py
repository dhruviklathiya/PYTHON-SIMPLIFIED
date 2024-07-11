# Dictonaries in python
    # Similar to objects in javascript except for it must be declared in string

# Create dictonaries using literals
_dictonary = {
    "fname":"D",
    "lname":"CODER"
}
print(_dictonary)

# Create dictonaries using dict keyword
_dictonary = dict(
    fname = "D",
    lname = "CODER"
) # notice that ':' has become '=' in this syntax
print(_dictonary['fname'])
print(_dictonary['lname'])
print(_dictonary['fname'] + _dictonary['lname'])

# add into dictonary
_dictonary['new_key'] = "I'll code more"
print(_dictonary)

# Loop in dictonary
for i in _dictonary:
    print("Keyname:",i,"==>","Value:",_dictonary[i])
# Note that a comma in print() leaves one blank space bydefault

# Loop values directly
for i in _dictonary.values():
    print(i)

# Loop keys directly
for i in _dictonary.keys():
    print(i)

# Checking keys in dictonaries
if 'fname' in _dictonary:
    print("Present 🙋🏻‍♂️")
    # Note directly using emojis

# Checking value in dictonaries
if 'CODER' in _dictonary.values():
    print("Present 🙋🏻‍♂️")

# Checking value in dictonaries
if 'fname' in _dictonary.keys():
    print("Present 🙋🏻‍♂️")