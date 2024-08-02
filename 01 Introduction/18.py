# for - in - range
for i in range(10):
    print(i)

for i in range(101,201):
    print(i)

_input = input("Enter a number: ")
result = 0
for i in range(0,len(_input)):
    result+=int(_input[i])

print(f"Sum of all digits is {result}")

# STEP argument in for-in-range

for i in range(1,100,2): # 3rd argument work as jump statement
    print(i)