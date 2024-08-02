# Question: Find missing numbers from list

# _list = [1,2,5,6,7,13]
# _set_to_check = set(_list)

# for i in range(min(_set_to_check),max(_set_to_check)+1):
#     if i not in _set_to_check:
#         print(f"{i} is missing 🚫")
#     else:
#         print(f"{i} is present 🙋🏻‍♂️")
#     _set_to_check.add(i)

# print(f"Complete members are in {_set_to_check}")

# Question 2: Find missing numbers from user input list
_list = input("Enter input seperated by space").split()
_list = [int(i) for i in _list]
_set_to_check = set(_list)

for i in range(min(_set_to_check),max(_set_to_check)+1):
    if i not in _set_to_check:
        print(f"{i} is missing 🚫")
    else:
        print(f"{i} is present 🙋🏻‍♂️")
    _set_to_check.add(i)

print(f"Complete members are in {_set_to_check}")