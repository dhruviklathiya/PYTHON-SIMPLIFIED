# break keyword & continue keyword

for i in range(1,11):
    if i == 5:
        continue
    else:
        print(i)

# OUTPUT: 1 to 10 except 5

for i in range(1,11):
    if i == 5:
        break
    else:
        print(i)

# OUTPUT: 1 to 4