# Enumarate function
    # Track both index and value of any iterable data in one loop
        # Similar to map method in javascript
_list = [1,2,3,4,3,2,3,4,5,6,7]

for index,value in enumerate(_list):
    print(f"{index} ===> {value}")