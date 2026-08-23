print("Hello World!")# print statement

# Variable declaration
name = "ALPHA" # string variable
age = 30 # integer variable 
cgpa = 3.5 # float variable
is_student = True # boolean variable
print(f"My name is: {name}\nMy age is: {age}\nCGPA: {cgpa}, Is Student: {is_student}") # f-string formatting


## Data types
print("Data types in Python")
print(type(name)) # string data type
print(type(age)) # integer data type
print(type(cgpa)) # float data type
print(type(is_student)) # boolean data type

#Data type conversion
age_str = str(age) # converting integer to string
print(type(age_str)) # string data type
print(age_str)

## Input from user
user_name = input("Enter your name: ") # taking string input
user_age = int(input("Enter your age: ")) # taking integer input
user_cgpa = float(input("Enter your CGPA: ")) # taking float input
user_is_student = input("Are you a student? (True/False): ") # taking boolean input as string

#Arithmetic operations
sum = user_age + 5
print(f"Your age after 5 years will be: {sum}")
print(3+2) # addition
print(3-2) # subtraction
print(3*2) # multiplication
print(3/2) # division
print(3//2) # floor division
print(3%2) # modulus
print(3**2) # exponentiation

##Comparison operators
print(3 > 2) # greater than
print(3 < 2) # less than
print(3 == 2) # equal to
print(3 != 2) # not equal to
print(3 >= 2) # greater than or equal to
print(3 <= 2) # less than or equal to

##logical operators
print(3 > 2 and 2 < 3) # and operator
print(3 > 2 or 2 > 3) # or operator
print(not(3 > 2)) # not operator

#if-else statement
if user_age >= 18:
    print("You are an adult.")
elif user_age >= 13:
    print("You are a teenager.")    
else:
    print("You are a minor.")
    
    
    
##Loops
#for loop
for i in range(5):
    print(f"Iteration {i+1}")

#while loop
count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1
    
#list
fruits = ["apple", "banana", "mango"]

print(fruits[0])      # apple
print(len(fruits))    # 3
fruits.append("orange")
print(fruits)

#common list operations
fruits.remove("banana")
print(fruits) # ['apple', 'mango', 'orange']
fruits.pop() # removes last element
print(fruits) # ['apple', 'mango']
fruits.insert(1, "grapes") # inserts at index 1
print(fruits) # ['apple', 'grapes', 'mango']
print(fruits.index("mango")) # 2
fruits.sort() # sorts the list
print(fruits) # ['apple', 'grapes', 'mango']
fruits.reverse() # reverses the list
print(fruits) # ['mango', 'grapes', 'apple']


##Strings
name = "Python"

print(name[0])         # P
print(len(name))       # 6
print(name.upper())    # PYTHON
print(name.lower())    # python
print(name.strip())    # removes spaces
print(name.replace("P", "J")) # Jython
print(name.split("y")) # ['P', 'thon']
print(name.find("t")) # 2
print(name.isalpha()) # True
print(name.isdigit()) # False
print(name.startswith("Py")) # True
print(name.endswith("on")) # True
print(name.count("o")) # 1
Print(name.capitalize()) # Python
print(name.title()) # Python
print(name.swapcase()) # pYTHON
print(name.center(20)) # centers the string in 20 spaces
print(name[::-1]) # reverses the string
print(name[1:4]) # extracts substring from index 1 to 3
print(name[::2]) # extracts every second character
print(name[-1]) # extracts the last character

#concatenation
first = "Ali"
last = "Ahmed"
full = first + " " + last
print(full)

##Tuples

tuble = (1, 2, 3, 4, 5)
print(tuble[0]) # 1
print(len(tuble)) # 5
print(tuble.index(3)) # 2
print(tuble.count(2)) # 1
print(tuble[1:4]) # (2, 3, 4)
print(tuble[-1]) # 5
print(tuble.count(6)) # 0
print(tble + (6, 7, 8)) # (1, 2, 3, 4, 5, 6, 7, 8)



