# Input: 2345 || Output => 2+3+4+5 => 14
_number = input("Enter youe number: ")
i = 0
result = 0
while i < len(_number):
    result += int(_number[i])
    i+=1

print(f"Sum of all digits in number is {result}")

# Working : Do the same program using number as input