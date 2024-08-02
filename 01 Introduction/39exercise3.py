# Create dictionary and take all values from user
_name = input("Enter your name:")
_age = int(input("Enter your age in digits:"))
_fav_movies = input("Enter your favourite movie seperated by comma:").split(",")
_fav_songs = input("Enter your favourite song seperated by comma:").split(",")

_result = {
    "name":_name,
    "age":_age,
    "fav movies":_fav_movies,
    "fav songs":_fav_songs
}
# Notice space in keys are allowed because of string formatting
print(_result)

# Print using loop
for i,j in _result.items():
    print(f"Key is {i} for value of {j}")