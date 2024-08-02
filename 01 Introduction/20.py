# for-in-string

_string = "HELLO WORLD"

for i in _string:
    print(i)

# input=>2345 || output=> 2+3+4+5 = 14
_string = input("Enter a number: ")
print(_string)
result = 0
for i in _string:
    result += int(i)
print(f"Sum of all digits in number is: {result}")