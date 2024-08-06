# Implementing end='' for printing file with loop

_file = open('file.txt')
_list = _file.readlines()
print(_list)

for i in _list:
    print(i,end='') # We used end='' so that we do not see \n (nextline) in our output

_file.close()