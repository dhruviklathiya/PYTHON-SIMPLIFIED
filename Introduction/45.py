# If-else comprehension in dictionary
# Concept => if number is odd => Cube will be saved
#         => if number is even => Square will be saved

_dictionary = {i:(i**3 if i%2!=0 else i**2) for i in range(0,11)}
print(_dictionary)