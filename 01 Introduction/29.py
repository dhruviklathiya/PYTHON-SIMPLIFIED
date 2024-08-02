# split() & join()
full_name = input("Enter name: ").split(" ")
print(full_name)

# full_name will be list

name1, name2, name3 = input("Enter name: ").split(",")
print(name1) # this will print particular value
print(name2) # this will print particular value
print(name3) # this will print particular value

# join
print(','.join(full_name))