# Change position of cursor ==> .seek()

# Cursor position ==> .tell()

_file = open('file.txt')
print("Cursor position is after before readline() ===> ", _file.tell())
_line1 = _file.readline() # Cursor starts from line 1 character 1 till end of first line
print("Data from file is", _line1)
print("Cursor position is after first readline() ===> ", _file.tell())
_line2 = _file.readline() # Cursor starts from line 2 character 1 till end of second line
print("Data from file is", _line2)
print("Cursor position is after second readline() ===> ", _file.tell())
_line3 = _file.readline() # Cursor starts from line 3 character 1 till end of third line
print("Data from file is", _line3)
print("Cursor position is after third readline() ===> ", _file.tell())

# It's not necessary to close the file but it's good practice
_file.close()

# .readline() return data of one line + shift cursor to newline