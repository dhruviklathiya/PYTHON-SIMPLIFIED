# Dictonary methods
    # fromkeys()
    # get()
    # copy()
    # clear()

# fromkeys() creates dictonary from given keys
_dictonary = dict.fromkeys(['fname','lname'],'unknown')
    # value of unknown will be provided into all keys in list
    # we must use list otherwise string will be seperated into multiple variables
print(_dictonary)

_dictonary = dict.fromkeys("ABCD",'unnknown')
print(_dictonary)

_dictonary = dict.fromkeys("ABCD",[1,2,3,4,'Hello'])
print(_dictonary)

_dictonary = dict.fromkeys(range(1,11),[1,2,3,4,'Hello'])
print(_dictonary)

# Access element of dictionary using get method


# Difference in traditional method and get method is about throwing error
    # get method will not throw error whereas traditional method will throw error
result = _dictonary.get('2')
print(result)
    # If get is unable to find key it will return None
    # Uncomment upcoming 2 lines for demonstration of error
# result = _dictonary['2']
# print(result)
    # Traditional method will throw error

# Custom message pass in terminal for not found key in dictionary
print(_dictonary.get('name',"NOT FOUND"))

if 2 in _dictonary:
    print('Present')

# copy method
    # We can copy dictionary with 2 methods
        # Deep copy
        # Shallow copy
# Copy dictionary with deep copy
    # Deep copy ===> Copying actual data from any specific memory location
_copy_dictionary = _dictonary.copy()
print(_copy_dictionary)

# Copy dictionary with shallow copy
    # Shallow copy ===> 2 variables pointing to same memory location in this example: _dictonary & _copy_dictionary points to same memory address
_copy_dictionary = _dictonary
print(_copy_dictionary)

# How to find difference?
    # Add element to anyone dictionary and check if it changes other dictionary or not
        # If changes are done in both dictionary then it's a shallow copy
        # If changes are done in only one dictionary then it's a deep copy
_copy_dictionary2 = _dictonary.copy()
_dictonary["new"] = "CHANGES"
print(_copy_dictionary2)
    # _copy_dictionary2 will not have key: "new" and value: "CHANGES"
