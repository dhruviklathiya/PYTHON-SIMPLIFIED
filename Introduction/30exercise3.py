# 2 list => Find out comman element and create new list containing common elements

_list1 = input("Enter list element seperated by comma").split(",")
_list2 = input("Enter list element seperated by comma").split(",")
_duplicate = []

n = max(len(_list1),len(_list2))
m = min(len(_list1),len(_list2))

if len(_list1) > len(_list2):
    for i in range(0,n):
        for j in range(0,m):
            if int(_list1[i]) == int(_list2[j]):
                _duplicate.append(int(_list1[i]))
            else:
                pass
else:
    for i in range(0,n):
        for j in range(0,m):
            if int(_list2[i]) == int(_list1[j]):
                _duplicate.append(int(_list2[i]))
            else:
                pass

print(_duplicate)