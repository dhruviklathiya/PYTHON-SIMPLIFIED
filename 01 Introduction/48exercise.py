# Input multiple items & then return list containing cube

_input = input("Enter values for cube: ").split(",")

def cube_function(*nums):
    total = 0
    for i in nums:
        total+= i
    print(f"Total sum is: {total}")

for i in range(0,len(_input)):
    _input[i] = int(_input[i])
    print(type(_input[i]))
    # _input[i]:int(_input)

cube_function(*_input)