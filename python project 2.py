Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Ask user for name

name = input("What is your name?: ")

# Ask user for age

age = input("How old are you?: ")

# Ask user for city

city = input("What city do you live in?: ")

# Ask user what they enjoy

love = input("What do you love doing?: ")

# Create output text

string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, love)

# Print output to screen
print(output)