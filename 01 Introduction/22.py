# fibonacci series
n = int(input("How many elements do you need in fibonacci?: "))
sum = 2
var1 = 1
var2 = 1
if n==0:
    print("Enter valid number")
elif n==1:
    print(0)
elif n==2:
    print(0, 1)
elif n==3:
    print(0, 1, 1)
else:
    print(0, 1, 1, end=" ")
    for i in range(2,n-1):
        sum = var1+var2
        print(sum,end = " ")
        var1 = var2
        var2 = sum

# Fibonacci using list in python
_fibonacci = []

for i in range(0,10):
    if i<2:
        _fibonacci.append(i)
        continue
    var1 = _fibonacci[i-2]
    var2 = _fibonacci[i-1]
    _fibonacci.append(var1+var2)

print(_fibonacci)