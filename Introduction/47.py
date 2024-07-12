# Unlimited number of arguments:-
    # *args
def addition(*args):
    print(args)

addition(4,3,5,3,3,2,4,3,6)
    # Data type of *args is tuple

# Another example
def addition2(*numbers):
    print(numbers)
    sum = 0
    for i in numbers:
        sum+=i
    print(sum)

addition2(3,2,4,3,6)

# Some arguments are known and some are not:
def multiplication(num1,num2,num3,*nums):
    total = num1*num2*num3
    for i in nums:
        total*=i
    print(total)

multiplication(1,2,3,4,5)
multiplication(1,2) #Error
multiplication(1,2,3) #No error
