# Create dictionary that stores repetition of every character in string
    # Input string from user
_string = input("Enter string:")
_count_dictionary = {}
for i in _string:
    _count_dictionary[i] = _string.count(i)
print(_count_dictionary)