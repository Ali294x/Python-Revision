"""Day 3: Exception handling, file handling, and advanced Python concepts.

This file demonstrates the major topics covered in Day 3 of the Python revision plan.
"""

from pathlib import Path
import csv
import json

base_dir = Path.home() / "PythonRevisionDay3Data"
base_dir.mkdir(parents=True, exist_ok=True)

# Exception Handling
print("EXCEPTION HANDLING")


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


try:
    print(divide(10, 2))
    print(divide(10, 0))
except ZeroDivisionError as error:
    print(f"Caught an error: {error}")
else:
    print("No exception occurred.")
finally:
    print("This block always runs.")


class InvalidAgeError(ValueError):
    """Raised when the age is negative."""


def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    return age


try:
    print(validate_age(-5))
except InvalidAgeError as error:
    print(f"Custom exception: {error}")


# File I/O - Writing and reading text files
print("\nFILE HANDLING")

sample_path = base_dir / "sample.txt"
with sample_path.open("w", encoding="utf-8") as file:
    file.write("Hello Python\n")
    file.write("Day 3 revision\n")
    file.write("File handling is easy.\n")

with sample_path.open("r", encoding="utf-8") as file:
    content = file.read()
    print(content)


# JSON handling
student = {
    "name": "Ali",
    "age": 21,
    "skills": ["Python", "SQL", "Excel"],
}

student_path = base_dir / "student.json"
with student_path.open("w", encoding="utf-8") as file:
    json.dump(student, file, indent=2)

with student_path.open("r", encoding="utf-8") as file:
    loaded_student = json.load(file)
    print(loaded_student)


# CSV handling
rows = [
    ["name", "score"],
    ["Ali", 90],
    ["Aisha", 85],
    ["Zaid", 95],
]

scores_path = base_dir / "scores.csv"
with scores_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

with scores_path.open("r", encoding="utf-8") as file:
    data = list(csv.reader(file))
    print(data)


# List comprehensions
print("\nLIST COMPREHENSIONS")

squares = [x ** 2 for x in range(1, 11)]
print(f"Squares: {squares}")

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Dictionary comprehension
square_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Square dictionary: {square_dict}")

# Set comprehension
letters = {char for char in "pythonprogramming"}
print(f"Unique letters: {letters}")


# Generators
print("\nGENERATORS")


def countdown(number):
    while number > 0:
        yield number
        number -= 1


for value in countdown(5):
    print(value)


# Iterators
print("\nITERATORS")


class MyRange:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


for number in MyRange(4):
    print(number)


# Decorators
print("\nDECORATORS")


def uppercase_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result.upper()

    return wrapper


@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"


print(greet("ali"))


# Practice exercises
print("\nPRACTICE EXERCISES")

# 1. Check whether a number is even.
def is_even(number):
    return number % 2 == 0


print(f"Is 10 even? {is_even(10)}")

# 2. Convert Celsius to Fahrenheit using list comprehension.
celsius_values = [0, 10, 20, 30]
fahrenheit_values = [(c * 9 / 5) + 32 for c in celsius_values]
print(f"Fahrenheit values: {fahrenheit_values}")

# 3. Create a simple generator for squares.
def square_generator(limit):
    for number in range(1, limit + 1):
        yield number ** 2


print(list(square_generator(5)))

# 4. Basic file appending example.
notes_path = base_dir / "notes.txt"
with notes_path.open("a", encoding="utf-8") as file:
    file.write("Python revision is going well.\n")

with notes_path.open("r", encoding="utf-8") as file:
    print(file.read())

print("\nDay 3 revision complete!")
