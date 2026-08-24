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


# Mini project: Hair Salon Appointment Booking
print("\nHAIR SALON APPOINTMENT BOOKING")


class SalonService(ABC):
	"""Abstraction for every service offered by the salon."""

	def __init__(self, name, price, duration_minutes):
		self.name = name
		self.price = price
		self.duration_minutes = duration_minutes

	@abstractmethod
	def description(self):
		pass


class Haircut(SalonService):
	def __init__(self, style, price, duration_minutes=45):
		super().__init__(f"{style} haircut", price, duration_minutes)
		self.style = style

	def description(self):
		return f"{self.style} haircut - ${self.price:.2f}, {self.duration_minutes} minutes"


class HairColor(SalonService):
	def __init__(self, color, price, duration_minutes=90):
		super().__init__(f"{color} hair color", price, duration_minutes)
		self.color = color

	def description(self):
		return f"{self.color} hair color - ${self.price:.2f}, {self.duration_minutes} minutes"


class Customer:
	def __init__(self, name, phone):
		self.name = name
		self.phone = phone


class Stylist:
	def __init__(self, name, specialty):
		self.name = name
		self.specialty = specialty


class Appointment:
	def __init__(self, customer, stylist, service, appointment_time):
		self.customer = customer
		self.stylist = stylist
		self.service = service
		self.appointment_time = appointment_time
		self.__status = "Booked"  # Encapsulation: status is changed through methods.

	@property
	def status(self):
		return self.__status

	def cancel(self):
		if self.__status == "Completed":
			raise ValueError("A completed appointment cannot be cancelled")
		self.__status = "Cancelled"

	def complete(self):
		if self.__status != "Booked":
			raise ValueError("Only booked appointments can be completed")
		self.__status = "Completed"

	def summary(self):
		return (
			f"{self.appointment_time:%Y-%m-%d %H:%M} | "
			f"{self.customer.name} with {self.stylist.name} | "
			f"{self.service.description()} | {self.status}"
		)


class Salon:
	def __init__(self, name):
		self.name = name
		self.__appointments = []

	def book_appointment(self, customer, stylist, service, appointment_time):
		if appointment_time <= datetime.now():
			raise ValueError("Appointment time must be in the future")
		for appointment in self.__appointments:
			if (
				appointment.stylist is stylist
				and appointment.appointment_time == appointment_time
				and appointment.status == "Booked"
			):
				raise ValueError("This stylist is already booked at that time")
		new_appointment = Appointment(customer, stylist, service, appointment_time)
		self.__appointments.append(new_appointment)
		return new_appointment

	def list_appointments(self):
		return tuple(self.__appointments)


salon = Salon("Fresh Look Salon")
customer = Customer("Ali", "555-0100")
stylist = Stylist("Sara", "Modern cuts")
selected_service = Haircut("Textured crop", 30)

appointment = salon.book_appointment(
	customer,
	stylist,
	selected_service,
	datetime(2099, 8, 24, 14, 30),
)
print(appointment.summary())
print(f"Appointments stored: {len(salon.list_appointments())}")

# Polymorphism: both service types use the same description() interface.
for service in (Haircut("Buzz cut", 20), HairColor("Brown", 50)):
	print(service.description())


# Mini project: ATM Machine
print("\nATM MACHINE")


class Account(ABC):
	"""Abstract base class for ATM accounts."""

	def __init__(self, account_number, owner, pin, balance=0):
		self.account_number = account_number
		self.owner = owner
		self.__pin = str(pin)
		self.__balance = balance
		self.__transactions = []

	def verify_pin(self, pin):
		return self.__pin == str(pin)

	@property
	def balance(self):
		return self.__balance

	def deposit(self, amount):
		if amount <= 0:
			raise ValueError("Deposit must be positive")
		self.__balance += amount
		self.__transactions.append(f"Deposit: +${amount:.2f}")

	def withdraw(self, amount):
		if amount <= 0:
			raise ValueError("Withdrawal must be positive")
		if amount > self.available_balance():
			raise ValueError("Insufficient funds")
		self.__balance -= amount
		self.__transactions.append(f"Withdrawal: -${amount:.2f}")

	@abstractmethod
	def available_balance(self):
		pass

	def add_transaction(self, message):
		self.__transactions.append(message)

	def transaction_history(self):
		return tuple(self.__transactions)


class CurrentAccount(Account):
	def available_balance(self):
		return self.balance


class SavingsAccount(Account):
	def __init__(self, account_number, owner, pin, balance=0, minimum_balance=100):
		super().__init__(account_number, owner, pin, balance)
		self.minimum_balance = minimum_balance

	def available_balance(self):
		return self.balance - self.minimum_balance


class ATM:
	def __init__(self, location):
		self.location = location
		self.__accounts = {}
		self.__current_account = None

	def add_account(self, account):
		self.__accounts[account.account_number] = account

	def login(self, account_number, pin):
		account = self.__accounts.get(account_number)
		if account is None or not account.verify_pin(pin):
			raise ValueError("Invalid account number or PIN")
		self.__current_account = account
		return f"Welcome, {account.owner}!"

	def logout(self):
		self.__current_account = None

	def current_balance(self):
		self._require_login()
		return self.__current_account.balance

	def deposit(self, amount):
		self._require_login()
		self.__current_account.deposit(amount)

	def withdraw(self, amount):
		self._require_login()
		self.__current_account.withdraw(amount)

	def transfer(self, recipient_number, amount):
		self._require_login()
		recipient = self.__accounts.get(recipient_number)
		if recipient is None:
			raise ValueError("Recipient account not found")
		self.__current_account.withdraw(amount)
		recipient.deposit(amount)
		self.__current_account.add_transaction(
			f"Transfer to {recipient.account_number}: -${amount:.2f}"
		)

	def _require_login(self):
		if self.__current_account is None:
			raise PermissionError("Please log in first")


atm = ATM("Main Street")
checking = CurrentAccount("1001", "Ali", "1234", 500)
savings = SavingsAccount("1002", "Sara", "5678", 1000)
atm.add_account(checking)
atm.add_account(savings)

print(atm.login("1001", "1234"))
atm.deposit(100)
atm.withdraw(50)
atm.transfer("1002", 100)
print(f"Checking balance: ${atm.current_balance():.2f}")
print(f"Checking history: {checking.transaction_history()}")
atm.logout()

# Polymorphism: both account types provide available_balance().
for account in (checking, savings):
	print(f"{account.owner}'s available balance: ${account.available_balance():.2f}")
