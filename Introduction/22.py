# fibonacci series
n = int(input("How many elements do you need in fibonacci?: "))
sum = 2
var1 = 1
var2 = 1
print(0, 1, 1, end = " ")
for i in range(2,n):
    sum = var1+var2
    print(sum,end = " ")
    var1 = var2
    var2 = sum