# MIN-MAX advance function
_list = ["DHRUVIK","LATHIYA","DCODER","D","CODER","A SOMETHING IS WRONG"]
# If I want to find maximum length from list I cannot use  directly
print("Wrong result==> ",max(_list))
    # It will return the maximum element based on lexicographical order (dictionary order), not the length of the strings

def fun_find_len(element):
    return len(element)

print("Right result ===> ",max(_list,key=fun_find_len))
                            # Pass iterable data and function in key property

# Same applies for min
print("Right result ===> ",min(_list,key=fun_find_len))

# Doing same thing with lambda function
print("Right result for min length ===> ",min(_list,key=lambda a:len(a)))
print("Right result for max length===> ",max(_list,key=lambda a:len(a)))