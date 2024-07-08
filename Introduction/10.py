# String methods || functions

# Find length of string
_str = "Hello world"
print(len(_str))

_str = "HELLO WORLD"
print(_str.lower())
print(_str.upper())
print(_str.title()) # Capitalise
print(_str.count("L")) # Counts character repetition in string
# count method is case-sensitive

# Difference between python string function & methods
# Python function takes argument
# Python methods can be chained

# String strip method => Work same as javascript's trim method
_str = "    Hello    "
_join = "|||||||||"
print(_str + _join)
print(_str.rstrip() + _join)
print(_str.lstrip() + _join)
print(_str.strip() + _join)

# Replace in string
# .replace(old,new,count)
_str = "    H e l l o    "
print(_str.replace(" ","") + _join)

# 3rd parameter in .replace is for how many replacement do we want to be changed
print(_str.replace(" ","",5) + _join)

# Find method in string
_str = "I will progress every hour in day"
print(_str.find("I")) # output => 0
print(_str.find("i")) # output => 3
# print(_str.find("i",SEARCH_START_INDEX))
print(_str.find("i",4)) # output => 27


# String center method || work like pad method in javascript
_str = "DCODER"
print(_str.center(4,"*")) # Not possible because of _str's length is more than parameter passed in center method
print(_str.center(7,"*")) # Priority to add extra is at right side
print(_str.center(8,"*"))
print(_str.center(50,"*"))


### Remember that all methods and functions worked on string will not change actual string || literal string
# Professional words: String are immutable
# We cannot change particular character or part of string manually like,
# _str[4] = 'A'
# _str.replace('E','A') # this is valid