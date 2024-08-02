# items in dictonaries
    # Important topic because .items() is most used method
_dictonary = {
    "fname":"D",
    "lname":"CODER",
    "list":[1,2,3,4]
}

_dictonary_items = _dictonary.items()
print(_dictonary_items)
    # Returns multiple tuple containing key&value pair inside a list

for i in _dictonary_items:
    print(i)
    # This prints only tuples
for i,j in _dictonary_items:
    print("Key:",i)
    print("Value:",j)