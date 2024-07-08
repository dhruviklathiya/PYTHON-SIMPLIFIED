# Box-office discont offer
# People with age above 10 & name starting from 'A' or 'a' can only see movie
_str = input("Enter your name: ")
_age = int(input("Enter your age: "))

# Solution 1
# if _age > 10 and _str[0] == 'a' or 'A':
#     print("You can watch movie")
# else:
#     print("You cannot watch movie")

# Solution 2
if _age > 10 and _str.lower()[0] == 'a':
    print("Congratulations \U0001F389 \U0001F389 \U0001F389 \U0001F389 on discount !!!")
else:
    print("No discount this time, better luck next time \U0001F641\U0001F641")