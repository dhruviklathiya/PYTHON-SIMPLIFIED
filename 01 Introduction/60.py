# Min-max in list of dictionary
list_of_dictionary = [
    {"fname":"A","marks":12,"lname":"AA"},
    {"fname":"B","marks":34,"lname":"BB"},
    {"fname":"C","marks":45,"lname":"CC"}
]

# find max marks
print(max(list_of_dictionary,key=lambda one:one.get('marks')))
    # This will print dictionary
print(max(list_of_dictionary,key=lambda one:one.get('marks'))['fname'])
    # This will print specific value on key we provide

dictionary_of_dictionary = {
    "Adetail":{"fname":"A","marks":12,"lname":"AA"},
    "Bdetail":{"fname":"B","marks":34,"lname":"BB"},
    "Cdetail":{"fname":"C","marks":45,"lname":"CC"}
}
# Printing key name containing highest marks
print(max(dictionary_of_dictionary,key=lambda one:dictionary_of_dictionary[one]['marks']))
# Printing specific details
print(dictionary_of_dictionary[max(dictionary_of_dictionary,key=lambda one:dictionary_of_dictionary[one]['marks'])]['lname'])