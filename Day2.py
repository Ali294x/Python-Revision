"""Day 2: Functions, OOP, and Modules

Run this file to review the examples from the three-day Python revision plan.
"""

from datetime import datetime
from functools import reduce
import math
import random


# Functions
def greet(name, message="Welcome to Python"):
	"""Return a greeting using a default argument."""
	return f"Hello, {name}! {message}."


def calculate_total(price, quantity=1, discount=0):
	"""Calculate a discounted total with keyword-friendly parameters."""
	subtotal = price * quantity
	return subtotal - (subtotal * discount / 100)


print("FUNCTIONS")
print(greet("Ali"))
print(greet("Ali", "Keep revising"))
print(f"Total: {calculate_total(100, quantity=2, discount=10):.2f}")


# *args collects positional arguments; **kwargs collects keyword arguments.
def summarize_scores(*scores, **student_info):
	return {
		"student": student_info.get("name", "Unknown"),
		"count": len(scores),
		"average": sum(scores) / len(scores) if scores else 0,
		"highest": max(scores) if scores else None,
	}


print(summarize_scores(80, 90, 75, name="Ali"))


# Lambda, map, filter, and reduce
numbers = [1, 2, 3, 4, 5]
double = lambda number: number * 2
doubled_numbers = list(map(double, numbers))
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
product = reduce(lambda first, second: first * second, numbers)

print(f"Doubled: {doubled_numbers}")
print(f"Even: {even_numbers}")
print(f"Product: {product}")


# Classes and objects
class BankAccount:
	bank_name = "Python Bank"

	def __init__(self, owner, balance=0):
		self.owner = owner
		self.__balance = balance  # Encapsulation: private implementation detail

	def deposit(self, amount):
		if amount <= 0:
			raise ValueError("Deposit must be positive")
		self.__balance += amount

	def withdraw(self, amount):
		if amount <= 0 or amount > self.__balance:
			raise ValueError("Invalid withdrawal")
		self.__balance -= amount

	def get_balance(self):
		return self.__balance

	def __str__(self):
		return f"{self.owner}'s account: ${self.__balance:.2f}"


account = BankAccount("Ali", 100)
account.deposit(50)
account.withdraw(25)
print("\nCLASSES AND OBJECTS")
print(account)
print(f"Balance: ${account.get_balance():.2f}")


# Inheritance and polymorphism
class Animal:
	def speak(self):
		return "Some sound"


class Dog(Animal):
	def speak(self):
		return "Woof"


class Cat(Animal):
	def speak(self):
		return "Meow"


for animal in (Dog(), Cat()):
	print(animal.speak())


# Abstraction: subclasses must implement describe().
from abc import ABC, abstractmethod


class Shape(ABC):
	@abstractmethod
	def area(self):
		pass

	@abstractmethod
	def describe(self):
		pass


class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return math.pi * self.radius ** 2

	def describe(self):
		return f"Circle area: {self.area():.2f}"


print(Circle(3).describe())


# Modules: importing and using functionality from the standard library.
print("\nMODULES")
print(f"Square root of 81: {math.sqrt(81)}")
print(f"Today: {datetime.now().date()}")


# Solved practice exercises
print("\nSOLVED EXERCISES")

# 1. Return whether a number is prime.
def is_prime(number):
	if number < 2:
		return False
	for divisor in range(2, math.isqrt(number) + 1):
		if number % divisor == 0:
			return False
	return True


print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 20 prime? {is_prime(20)}")


# 2. Create a Rectangle class with area and perimeter methods.
class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height

	def perimeter(self):
		return 2 * (self.width + self.height)


rectangle = Rectangle(5, 3)
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")


# 3. Convert Celsius values to Fahrenheit with map().
celsius_values = [0, 20, 37, 100]
fahrenheit_values = list(map(lambda celsius: (celsius * 9 / 5) + 32, celsius_values))
print(f"Fahrenheit values: {fahrenheit_values}")


# 4. Build a number-guessing game with random.
def guessing_game(guesses, low=1, high=10):
	secret_number = random.randint(low, high)
	for guess in guesses:
		if guess == secret_number:
			return f"Correct! The number was {secret_number}."
		if guess < secret_number:
			print("Try a higher number.")
		else:
			print("Try a lower number.")
	return f"Game over. The number was {secret_number}."


random.seed(7)
print(guessing_game([3, 8, 6]))
