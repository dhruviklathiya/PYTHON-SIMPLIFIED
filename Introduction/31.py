# Difference in append and extend
    # append adds elements directly
    # extend extracts elements and then adds to list
_list = [1,2,3,4]
print(_list)
_list.append([10,20,30,40])
print(_list)
_list.extend([10,20,30,40])
print(_list)