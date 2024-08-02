# Skipping parameter in python string slicing

_string = "Woo woo woo woo woo woo"
print(_string[0:24:4])

# Explanation: String will be cut down to index 0 till 23
# Slicing will be done on every 4th index
# # index will be skipped

# Not providing stop argument will check string till end
print(_string[0::4])

# Reverse a string
print(_string[24::-1])
print(_string[-1::-1])