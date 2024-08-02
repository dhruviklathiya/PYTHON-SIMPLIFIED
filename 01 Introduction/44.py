# Comprehension in dictionary
n = int(input("How many numbers cube do you need in your dictionary: "))
_dictionary = {f'Cube of {i}' :i**3 for i in range(1,n+1)}
print(_dictionary)

# Print dictionary in seperate lines
for i,j in _dictionary.items():
    print(f"{i} ===> {j}")

# Count repetition of letters in string using dictionary comprehension
_string = input("Enter any string and count repetition:")
_count_letter = {f"{i} is repetition":_string.count(i) for i in _string}
print(_count_letter)

# Print dictionary in seperate lines
for i,j in _count_letter.items():
    print(f"{i} ===> {j}")