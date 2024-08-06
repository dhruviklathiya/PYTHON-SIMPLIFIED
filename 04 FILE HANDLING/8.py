# Open files using 'with' keyword


with open('file.txt') as _file:
    data = _file.read()
    print(data)
    print("File is close in with block?",_file.closed)

# With block automatically closes file
print("File is close after with block?",_file.closed)
