# String formatting part of python 3.6
    # String formatting is same as javascript's template literals
    # Difference is in syntax not containing $ and containing .format(parameters)

# NEW METHOD
programming_language = "PYTHON"
method = "CURLY BRACKETS"
number1 = 10
number2 = 100
print(f"This is example of {programming_language} programming string formating using {method}")
print(f"This is example of calculation in {programming_language}  programming string formating using {method}: {number1+number2}")


# OLD METHOD
print("This is example of {} programming string formating using {}".format(programming_language,method))
