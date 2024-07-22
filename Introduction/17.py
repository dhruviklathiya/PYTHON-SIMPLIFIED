# Input: 2345 || Output => 2+3+4+5 => 14
_number = input("Enter youe number: ")
i = 0
result = 0
while i < len(_number):
    result += int(_number[i])
    i+=1

print(f"Sum of all digits in number is {result}")

# Working : Do the same program using number as input
_number = int(input("Enter number:"))
_sum = 0
while _number>0:
    _sum+= _number%10
        # Adding last digit in sum
    _number = _number // 10
        # Removing last digit for next iteration
print(_sum)