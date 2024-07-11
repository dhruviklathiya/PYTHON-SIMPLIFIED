# Set in python
    # Definition: set can only hold uniques value
_set = {1,2,3,4,3,2,4,5,5,5,4,3}
print(_set)
    # Set will automatically remove duplicate data

# Add elements to set
_set.add(1)
_set.add(10)
_set.add(10) # will be ignored because set only saves unique values
print(_set)

# Remove from set
_set.remove(10)
# _set.remove(10) # Error
_set.discard(10) # No error
print(_set)

# Something similar to traditional method and .get() method difference is also seen in sets
    # for example: .remove() will throw error if element does not exist in list
    # while .discard will not throw error even if element is not in set

# Clear set
# _set.clear()
# print(_set)

# Copy set
_set2 = _set.copy()
_set.discard(1)
print(_set)
print(_set2)

# Note: Set will not print element in same order as they are declared