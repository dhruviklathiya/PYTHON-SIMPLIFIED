# Add and remove items from dictonary

dictionary = {
    "fname":"D",
    "lname":"CODER"
}
dictionary['ADDED'] = "NEW ITEM"
print(dictionary)

dictionary.pop('fname')
print(dictionary)

# Error here
# dictionary.pop()
    # .pop() method requires atleast 1 argument if it's working on dictionary because dictionary does not have items in indexed form

# Randomly removing item from dictonary
dictionary.popitem()
print(dictionary)

# .pop() returns value
# .popitem() returns key&value