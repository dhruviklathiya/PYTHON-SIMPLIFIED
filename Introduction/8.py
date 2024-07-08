# String indexing
str = "Hello world"
print(f"Index 0 of string is {str[0]}")
print(f"Index 1 of string is {str[1]}")
print(f"Index 2 of string is {str[2]}")
print(f"Index 3 of string is {str[3]}")
print(f"Index 4 of string is {str[4]}")
print(f"Negative index -11 of string is {str[-11]}")
print(f"Negative index -10 of string is {str[-10]}")
print(f"Negative index -9 of string is {str[-9]}")
print(f"Negative index -8 of string is {str[-8]}")
print(f"Negative index -7 of string is {str[-7]}")

# Splicing string in python
sliced_string = str[0:5]
            # 0 => Starting index which will be in sliced part
            # 5 => Ending index which will not be in sliced part

# Questions
sliced_string = str[1:5]
print(sliced_string)
sliced_string = str[2:5]
print(sliced_string)
# Slice "world" from string
sliced_string = str[6:11]
print(sliced_string)

# Following code proved that we can redeclare and reassign variable in python

# Trick to remember [2:6] => index 2,3,4,5 will be printed
# Trick to remember [0:6] => index 0,1,2,3,4,5 will be printed

# We can also slice direct string without variable
print("Hello programmers"[6:17])