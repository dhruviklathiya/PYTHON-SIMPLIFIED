# Define function that takes 2 arguments and prints greater number
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

def maximum_num(num1,num2):
    return max(num1,num2)
print(f"Maximum number is: {maximum_num(num1,num2)}")

def minimum_num(num1,num2):
    return min(num1,num2)
print(f"Minimum number is: {minimum_num(num1,num2)}")

# Define function that checks palindrome
_string = input("Enter string for checking: ")
_reversed = ""
for i in range(len(_string)):
    _reversed += _string[-i-1]
if(_string == _reversed):
    print("PALINDROME")
else:
    print("NOT PALIMDROME")

# Short method
_string = input("Enter string for checking: ")
_reversed = ""
if(_string == _string[::-1]):
    print("PALINDROME")
else:
    print("NOT PALIMDROME")

# Another method
_string = input("Enter string for checking: ")

def palindrome_check(_para):
    return _para == _para[::-1]

print(f"Is string palindromic? ==> {palindrome_check(_string)}")