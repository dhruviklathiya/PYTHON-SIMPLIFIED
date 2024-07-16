# Task:
    # Define a function taking multiple arguments of multiplt list
    # Function will return average of every list like following

# Passed argument: [1,2,3,4],[5,6,7,8],[9,10,11,12]
# Process: zero index of all list => 1,5,9 => 1+5+9/3 => 5
# Return value: [5,6,7]

def fun_avg(*all_list):
    _result = []
    l1,l2,l3,l4 = zip(*all_list)
    _result.append(sum(l1)/len(l1))
    _result.append(sum(l2)/len(l2))
    _result.append(sum(l3)/len(l3))
    _result.append(sum(l4)/len(l4))
    return _result

print(fun_avg([1,2,3,4],[5,6,7,8],[9,10,11,12]))