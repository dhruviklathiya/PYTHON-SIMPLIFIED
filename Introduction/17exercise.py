# Searching repetition of every single character in input
_input = input("Enter your name: ")
i = 0
while i < len(_input):
    print(f"Character {_input[i]} is repeated {_input.count(_input[i])} times in string")
    i+=1

# Advance version: Not repeating same character
# _input = input("Enter your name: ")
# i = 0
# _container = ""
# while i < len(_input):
#     if _input[i] not in _container:
#         print(f"Character {_input[i]} is repeated {_input.count(_input[i])} times in string")
#         _container+=_input[i]
#     else:
#         pass
#     i+=1

# Another method
_input = input("Enter your name: ")
_already_counted = ""
for i in _input:
    if i in _already_counted:
        pass
    else:
        print(f"{i} is repeated {_input.lower().count(i.lower())} times in string")
        _already_counted+=i