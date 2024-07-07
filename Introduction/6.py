# Input multiple values using only one input function
fname, lname, designation, lucky_number = input("Enter firstname, lastname, designation, lucky number input seperated by space: ").split()
print(fname + " " + lname + " " + designation + "'s lucky number is" , lucky_number)

# Seperate with comma
fname, lname, designation, lucky_number = input("Enter firstname, lastname, designation, lucky number input seperated by comma: ").split(",")
print(fname + " " + lname + " " + designation + "'s lucky number is" , lucky_number)