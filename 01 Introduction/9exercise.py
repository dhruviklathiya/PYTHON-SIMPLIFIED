# Take input from user and print output in reverse
fname,lname = input("Enter your name").split(" ")
print(fname[-1::-1] + " " + lname[-1::-1])