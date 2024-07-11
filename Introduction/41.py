# Actions with set
_set = {3,1,2,4,5,6}

for i in _set:
    print(i)

# Not valid
# for 6 in _set:
    # print("present")

# Valid
if 6 in _set:
    print("present")

# Maths in set
    # union in set
    # intersection in set

# Union => will combine all sets but not duplicate values
_set1 = {1,2,3,4,5,6,7,8,9}
_set2 = {11,12,13,14,15,16,17,18,19}
_union_set = _set | _set1 | _set2
print(_union_set)

# Intersection => Will combine common values from sets
_intersection_set = _set & _set1
print(_intersection_set)