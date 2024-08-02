# Creating single first-class function

def first_class_fun(_para1):
    def calculation(n):
        return n**_para1
    return calculation

# Creating multiple functions from a single function acoording to usecase
square = first_class_fun(2)
cube = first_class_fun(3)
_to_poer_10 = first_class_fun(10)

print(square(10))
print(cube(10))
print(_to_poer_10(9))