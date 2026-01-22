# Python Basics

# ===== Basic Output =====
print("Hello, World!")

# ===== Variables and Data Types =====
x = 10  # Integer
y = 3.14  # Float
name = "Alice"  # String
is_student = True  # Boolean

# ===== Lists =====
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Access first element

# ===== Conditional Statements =====
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")

# ===== Loops =====
for fruit in fruits:
    print(fruit)

count = 0
while count < 3:
    print("Count:", count)
    count += 1

# ===== Functions =====
def greet(person):
    return f"Hello, {person}!"

print(greet(name))

# ===== Classes =====
class Dog:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age
    
    def bark(self):
        return "Woof!"
    
    def __str__(self):
        return f"Dog named {self.name}, age {self.age}"

my_dog = Dog("Buddy", 3)
print(my_dog.bark())
print(my_dog)

# ===== Importing Modules =====
import math
from datetime import datetime

print("Square root of 16 is", math.sqrt(16))
print("Current time:", datetime.now())

# ===== File Handling =====
with open("example.txt", "w") as file:
    file.write("This is an example file.")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# ===== Exception Handling =====
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Cleanup code runs regardless")

# ===== List Comprehension =====
squares = [i**2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# ===== Dictionaries =====
person = {"name": "Bob", "age": 25, "city": "New York"}
print(person["name"])
print(person.get("email", "Not found"))  # Safe access

# Dictionary methods
print(person.keys())
print(person.values())
print(person.items())

# ===== Tuples =====
coordinates = (10, 20)
print(coordinates[0])

# Tuple unpacking
x_coord, y_coord = coordinates
print(f"X: {x_coord}, Y: {y_coord}")

# ===== Sets =====
unique_numbers = {1, 2, 3, 2, 1}
print(unique_numbers)  # {1, 2, 3}

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b))  # {1, 2, 3, 4, 5, 6}
print(set_a.intersection(set_b))  # {3, 4}
print(set_a.difference(set_b))  # {1, 2}

# ===== Lambda Functions =====
add = lambda a, b: a + b
print(add(3, 5))  # 8

# ===== Map, Filter, and Reduce =====
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(squared_numbers)  # [1, 4, 9, 16, 25]
print(even_numbers)  # [2, 4]

from functools import reduce
sum_all = reduce(lambda a, b: a + b, numbers)
print(sum_all)  # 15

# ===== Generators =====
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)  # 5 4 3 2 1

# Generator expression
gen_squares = (x**2 for x in range(5))
print(list(gen_squares))  # [0, 1, 4, 9, 16]

# ===== Decorators =====
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")

display()

# ===== List Slicing =====
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])  # [2, 3, 4]
print(numbers[:4])  # [0, 1, 2, 3]
print(numbers[5:])  # [5, 6, 7, 8, 9]
print(numbers[-3:])  # [7, 8, 9]
print(numbers[::2])  # [0, 2, 4, 6, 8]
print(numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# ===== F-Strings =====
age = 30
print(f"My name is {name} and I am {age} years old.")
print(f"Calculation: {10 + 5}")

# ===== Advanced List Comprehension =====
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ===== Dictionary Comprehension =====
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# ===== Enumerate =====
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# ===== Zip =====
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# ===== Args and Kwargs =====
def print_args(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

print_args(1, 2, 3, name="Alice", age=30)

# ===== String Methods =====
text = "  Hello World  "
print(text.strip())  # Remove whitespace
print(text.upper())
print(text.lower())
print(text.replace("World", "Python"))
print(text.split())

# ===== Ternary Operator =====
result = "Even" if x % 2 == 0 else "Odd"
print(result)

# ===== Multiple Assignment =====
a, b, c = 1, 2, 3
print(a, b, c)

# ===== Swap Variables =====
a, b = b, a
print(a, b)

# ===== Any and All =====
print(any([False, True, False]))  # True
print(all([True, True, True]))  # True

# ===== Context Managers =====
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# Usage: with FileManager("test.txt", "w") as f: ...

# ===== Type Hints (Python 3.5+) =====
def add_numbers(a: int, b: int) -> int:
    return a + b

# ===== Walrus Operator (Python 3.8+) =====
if (n := len(numbers)) > 5:
    print(f"List has {n} elements, more than 5")

