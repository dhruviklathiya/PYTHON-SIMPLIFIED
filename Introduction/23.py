# Changing value of global variable via local scope
global_variable = 10
print(global_variable)

def hello():
    global global_variable
    global_variable = 100

hello()
print(global_variable)