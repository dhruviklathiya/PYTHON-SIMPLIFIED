# Zip function
    # Combines indexed value from 2 different list to return multiple tuples
_list1 = ['USER1','USER2','USER3','USER4']
_list2 = [1,2,3,4]

_result = list(zip(_list1,_list2))

print("Reducing size of one list")

_list2 = [1,2]

_result = list(zip(_list1,_list2))
print(_result) # Minimum size will be counted for zipping together