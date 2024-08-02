# 2 list => Find out comman element and create new list containing common elements

# Method 1
# Get input from the user for the first list
list1 = input("Enter the elements of the first list separated by spaces: ").split()

# Get input from the user for the second list
list2 = input("Enter the elements of the second list separated by spaces: ").split()

# Convert both lists to sets to find the common elements & remove duplicates
set1 = set(list1)
set2 = set(list2)

# Find the intersection of both sets
common_elements = set1.intersection(set2)

# Convert the result back to a list if needed
common_list = list(common_elements)
print("Common elements:", common_list)


# Method 2
# _list1 = input("Enter list element seperated by comma").split(",")
# _list2 = input("Enter list element seperated by comma").split(",")
# _duplicate = []

# n = max(len(_list1),len(_list2))
# m = min(len(_list1),len(_list2))

# if len(_list1) > len(_list2):
#     for i in range(0,n):
#         for j in range(0,m):
#             if int(_list1[i]) == int(_list2[j]):
#                 _duplicate.append(int(_list1[i]))
#             else:
#                 pass
# else:
#     for i in range(0,n):
#         for j in range(0,m):
#             if int(_list2[i]) == int(_list1[j]):
#                 _duplicate.append(int(_list2[i]))
#             else:
#                 pass

# print(_duplicate)