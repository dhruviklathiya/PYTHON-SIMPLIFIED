# Take 3 input from user in single input function seperated by comma
    # average them and print them in string formatting

data1,data2,data3 = input("Enter value seprate by comma:").split(",")
result = int(data1)+int(data2)+int(data3)/3
print(f"Average of number {data1} {data2} {data3} is {result}")