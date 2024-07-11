# Add and remove items from dictonary

_dictonary = {
    "fname":"D",
    "lname":"CODER"
}
_dictonary['ADDED'] = "NEW ITEM"
print(_dictonary)

_dictonary.pop('fname')
print(_dictonary)

# Error here
# _dictonary.pop()
    # .pop() method requires atleast 1 argument if it's working on dictonary because dictonary does not have items in indexed form

# Randomly removing item from dictonary
_dictonary.popitem()
print(_dictonary)

# .pop() returns value
# .popitem() returns key&value