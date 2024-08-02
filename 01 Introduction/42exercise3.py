# List comprehension complex problems
names = ["John Doe", "Jane Smith", "Alice Johnson"]
# Expected Output: ['J.D.', 'J.S.', 'A.J.']
_list = [i.split()[0][0]+"."+i.split()[1][0]+"." for i in names]
print(_list)

words = ["cat", "elephant", "dog", "tiger", "lion"]
# Expected Output: ['elephant', 'tiger', 'lion']
_result = [i for i in words if len(i)>3]
print(_result)

celsius = [0, 20, 37, 100]
# Expected Output: [32.0, 68.0, 98.6, 212.0]
_Fahrenheit = [i*1.8+32 for i in celsius]
print(_Fahrenheit)

# Expected Output: [(1, 2, 2), (1, 3, 3), (1, 4, 4), ..., (10, 9, 90), (10, 10, 100)]
_multiplication = [(i,j,j*i) for i in range(0,11) for j in range(0,11)]
print(_multiplication)

strings = ["a1b2c3", "x9y8z7", "abc", "123"]
# Expected Output: ['123', '987', '', '123']