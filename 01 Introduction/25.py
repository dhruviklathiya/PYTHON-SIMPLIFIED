# Different ways to add items in list || Same as Array.push() method in javascript
_list = [1,2,3,4]
_list.append(5)
print(_list)

# Limitation of append: "Only adds element on last position"
# Solution: insert() method
    # Pass index and value

_list.insert(2,200)
print(_list)

# Adding two list into 3rd list
_list1 = [1,2,3,4]
_list2 = [5,6,7,8]
_result_list = _list1 + _list2
print(_result_list)

# Adding list into another list
_list1 = [1,2,3,4]
_list2 = [5,6,7,8]
_list1.extend(_list2)
print(_list1)