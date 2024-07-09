# Input => [1,2,3,4,5,6,7,8]
# Output => [[odd number list], [even number list]]
_list = [1,2,3,4,5,6,7,8]
odd = []
even = []

for i in _list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

_list.clear()
_list.append(odd)
_list.append(even)
print(_list)