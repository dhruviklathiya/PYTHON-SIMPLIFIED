# Input list of string
_input = list(input("Enter strings seperated by commas").split(","))
_search = input("Search value from list:")
def _index_find(search,list):
    print(list)
    for index,value in enumerate(list):
        print(value)
        if value==search:
            print(index)
            return index

print(_index_find(_search,_input))

# Why we cannot use is instead of == in condition
# for index,value is enumerate(list):
#         print(value)
#         if value==search:
#             print(index)
#             return index

# Answer: is will check for memory location if memory location is different then it will return True or else False