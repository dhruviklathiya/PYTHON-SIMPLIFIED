# Comprehension in sets
_set = {i for i in range(0,101)}
print(_set)

_set = {i if i%2!=0 else i**2 for i in range(0,101)}
print(_set)
    # Reminder: Set is unordered collection of data