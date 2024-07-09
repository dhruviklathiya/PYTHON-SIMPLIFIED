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