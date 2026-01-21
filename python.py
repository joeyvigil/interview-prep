#python basics

print("Hello, World!")  # This line prints a greeting message to the console
# Variables and Data Types
x = 10  # Integer variable
y = 3.14  # Float variable
name = "Alice"  # String variable
is_student = True  # Boolean variable
# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Accessing the first element of the list
# Conditional Statements
if x > 5:
    print("x is greater than 5")    
else:
    print("x is 5 or less")
# Loops
for fruit in fruits:
    print(fruit)
count = 0
while count < 3:
    print("Count:", count)
    count += 1
# Functions
def greet(person):
    return "Hello, " + person + "!"
print(greet(name))

# Classes
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())

# Importing Modules
import math
print("Square root of 16 is", math.sqrt(16))

# File Handling
with open("example.txt", "w") as file:
    file.write("This is an example file.")
    
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Lists Comprehension
squares = [i**2 for i in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Dictionarys
person = {"name": "Bob", "age": 25}
print(person["name"])  # Accessing value by key

# Tuples
coordinates = (10, 20)
print(coordinates[0])  # Accessing the first element of the tuple

# Sets
unique_numbers = {1, 2, 3, 2, 1}
print(unique_numbers)  # Output: {1, 2, 3}

# Lambda Functions
add = lambda a, b: a + b
print(add(3, 5))  # Output: 8

# Map and Filter
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
print(even_numbers)  # Output: [2, 4]
# Generators
def countdown(n):
    while n > 0:
        yield n # Yield makes this a generator
        n -= 1
for number in countdown(5):
    print(number)
    
# Output: 5 4 3 2 1 

# Decorators
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function


# Using the decorator
@decorator_function
def display():
    print("Display function executed")
display()
# Output:   # Wrapper executed before display
#           # Display function executed 
# List Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])  # Output: [2, 3, 4]
print(numbers[:4])   # Output: [0, 1, 2, 3]
print(numbers[5:])   # Output: [5, 6, 7, 8, 9]
print(numbers[-3:])  # Output: [7, 8, 9]
print(numbers[::-1]) # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(numbers)      # Original list remains unchanged

# F-Strings
age = 30
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 30 years old.
# Output: My name is Alice and I am 30 years old.
# Modules and Packages
# Creating a module named my_module.py with a function
def module_function():
    return "This is a function from my_module."
# Importing and using the module
# import my_module
# print(my_module.module_function())  # Output: This is a function from my_module.    
# Virtual Environments
# To create a virtual environment, use the following command in the terminal:
# python -m venv myenv
# To activate the virtual environment:
# On Windows:
# myenv\Scripts\activate
# On macOS/Linux:
# source myenv/bin/activate
# Once activated, you can install packages using pip:
# pip install package_name  
# To deactivate the virtual environment, simply run:
# deactivate
# Output: This is a function from my_module.
