# Number predicting game in python
_actual_number = 9
while True:
    _check = int(input("Enter number from 0 to 100: "))
    if _check == _actual_number:
        print("You won!!! \U0001F389 \U0001F389 \U0001F389 \U0001F389")
        break
    else:
        if _check < _actual_number:
            print("Too low \U0001F641\U0001F641")
        else:
            print("Too high \U0001F641\U0001F641")