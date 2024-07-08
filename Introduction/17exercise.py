# Searching repetition of every single character in input
_input = input("Enter your name: ")
i = 0
while i < len(_input):
    print(f"Character {_input[i]} is repeated {_input.count(_input[i])} times in string")
    i+=1