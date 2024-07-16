# any() => And one element passes condition will return True
# any() => All element passes then only condition will return True

print(any(list(map(lambda a:a>10,[1,2,3,4,5,11]))))
print(any(list(map(lambda a:a>10,[1,2,3,4,5,6]))))

print(all(list(map(lambda a:a>10,[1,2,3,4,5,6]))))
print(all(list(map(lambda a:a<10,[1,2,3,4,5,6]))))