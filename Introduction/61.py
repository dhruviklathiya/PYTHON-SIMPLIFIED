# Revision of previous method sort() and function sorted()
    # Pay attention to words I am using methods and functions are different
_list = [5,20,4,2,5,2,442,49]
print("Using sorted function=> ",sorted(_list))
print("Will not change actual list=> ",_list)
_list.sort()
print("Using sort method will change actual list=> ",_list)

# Let's talk about advance sorting functins for complex data types
_complex = {
    "Adetail":{"fname":"A","marks":12,"lname":"AA"},
    "Cdetail":{"fname":"C","marks":45,"lname":"CC"},
    "Bdetail":{"fname":"B","marks":34,"lname":"BB"}
}

print(sorted(_complex,key = lambda one:_complex[one]['marks']))
# Reverse sorted function
print(sorted(_complex,key = lambda one:_complex[one]['marks'], reverse=True))