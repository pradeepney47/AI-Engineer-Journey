# Functions in depth

# defining the function without a return
def greet(name):
    print("Hello ", name)

# stores the function in x
x = greet #function object (function is not called)
x("Alice") #function is called

print()

y = greet
result = y("Bob")
print(result)

print()

# executes the function and stores the return value (whatever the value maybe) in z 
z = greet("Charlie")
print(z)

print()

print(type(x), type(y), type(z))

# defining the function with a return

def square(number):
    return number * number
    # print(number * number)
    # return number * 3

print()

# reference or store the function
a = square #function object (function is not called)
c = a(5) #function is called and the returned value is stored in c
# print(a(5))
print(c)
print()

# calling the function and stores the returned value
b = square(6) #function is called and the returned value is stored in b
print(b)

print()

print(type(a), type(c), type(b))


    #              function_name
    #                    │
    #             ┌──────┴──────┐
    #             │             │
    #       no parentheses   parentheses
    #             │             │
    #             ↓             ↓
    #    function object     execute
    #             │             │
    #             ↓             ↓
    #        x = function   return value
    #                           │
    #                  ┌────────┴────────┐
    #                  │                 │
    #             has return        no return
    #                  │                 │
    #                  ↓                 ↓
    #             value stored        None stored

# defining function with return 

print()
def greet(name):
    return "Hello " + name

d = greet

d("Daniel")
# print(d("Da"))

print()

e = greet("Eva")
print(e)

# print()
# def greet(name):
#     print("Hello", name)

# z = greet("Charlie")
# print(z)

# Parameters and Arguments

# Parameter is a variable defined by the function to receive an input (while defining the function)
# Argument is the actual value supplied to the function it is called (while calling the function)

# Function can have multiple parameters eg., (a, b)
# Function can receive different kinds of objects eg., integer, string, list, dictionary, etc
print()
def introduce(name, age):
    return "My name is " + name + " and I am " + str(age)

result = introduce("Alice", 25)
print(result)

print()

# Passing a function as an argument

# square function
def square(number):
    return number * number

# calculate function
def calculate(function, value):
    # return function * 5
    return function(value)

# passing the square function as an argument when calling the calculate function
# square is a function object which is passed as the argument

# result = calculate(square(5), 5)
result = calculate(square, 5)

print(result)

# strings
print()
def greet(name):
    return "Hello " + name

def use_function(function, value):
    return function(value)

result = use_function(greet, "Alice")

print(result)

# function can be treated like a value/ object
# So, function can be
# assigned to a variable
# passed as an argument
# returned from another function
# stored in a collection
# This is why Python functions are called first-class objects

# Returning a Function from a Function
print()
def multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


# First call: calls multiplier()
double = multiplier(2) #returns function object multiply

# Second call: calls the function that multiplier() returned
result = double(10) #multiply(10)

print(result) #prints 20

# Another example

print()
def make_power(exponent):
    def power(number):
        return number ** exponent

    return power

# calling the function
result = make_power(4) #function object power is returned 
cube = result(3)

print(cube)

# Why passing function as argument is useful?

def add_ten(number):
    return number + 10

def multiply_by_three(number):
    return number * 3

def apply(function, value):
    return function(value)

a = apply(add_ten, 5)
b = apply(multiply_by_three, 5)

print()
print(type(a), type(b))
print(a, b)

# Function can be passed around just like value
# No parentheses → refer to the function object
# Parentheses → call the function and get its return value
print()
def square(x):
    return x * x

def apply(function, value):
    return function(value)

result = apply(square, 5)
print(result)

# Function Scope

print()
x = 10 # global variable

def show():
    x = 20 # local variable
    print(x)

# prints 20
show() # local variable is accessed because function is called and execution is within function scope

# prints 10
print(x) # global variable is accessed


# Local vs Global Scope
print()
x = 10 # global variable

def change():
    x = 20 # local variable does not overwrite the gloabal variable x

change()
print(x) # prints 10

# Changing the global variable inside function

print()
x = 10 # global variable x

def change():
    # global x tells Python that x inside this function refers to the existing global variable
    # this affects the variable x even outside
    # the scope of the function
    global x 
    x = 20 # local and global variable x

change()

print(x) # global variable and prints the current value in the variable which is 20


# Global check default
print()
x = 10 # global variable x

def show():
    print(x) # there is no variable x inside the function so Python looks for global variable x

show() # prints 10

# Variable no where
# When reading a variable inside a function, Python looks in the local scope first, 
# and if it doesn't find it, it can look in an enclosing/global scope
print()
def show():
    # no local variable and no global variable
    print(g) # no variable g found inside or outside function
try:
    show()
except NameError:
    print()
    print("Variable not found neither in the local nor in the global scope of the function")
finally:
    print()
    print("Learning function scope one at a time!")

# Python determines a variable's local scope from assignments in the function as a whole, 
# not dynamically line-by-line during execution

# It doesn't fall back to the global h, 
# because Python has already determined that h in this function is a local name.

# If a name is assigned anywhere in a function, that name is treated as local throughout that function, 
# unless explicitly declared global or nonlocal

print()
h = 10

def test():
    print(h)
    h = 20
try:
    test()
except UnboundLocalError:
    print()
    print("Cannot access local variable 'h' where it is not associated with a value")
finally:
    print()
    print("Learning function scope one at a time!")


# test()
#  ↓
# print(x)
#  ↓
# Python knows x is LOCAL
#  ↓
# Has local x received a value yet?
#  ↓
# No
#  ↓
# UnboundLocalError


print()
try:
    print(m) #NameError
    m = 8
except NameError:
    print()
    print("Variable not found")
finally:
    print()
    print("Python is interesting!")

# No assignment inside the function → Python can look outward for a value
# Assignment inside the function → Python treats that name as local throughout the function
# global x → explicitly tells Python to use the global x
# return → sends a value back to the caller
# Function parameters and local variables belong to the function's local scope

# *args
# lets the function accept a variable number of positional arguments

# In this program it is expected that position arguemnts 
# will only supply two arguments to functon definition
# otherwise throws error

print()
# result = add(10, 20, 30)

def add(a, b):
    return a + b
try:
    result = add(10, 20, 30)
    # result = add(10, 20)
except TypeError:
    print()
    print("Only 2 Positional arguments expected")
else:
    print()
    print(result)
finally:
    print()
    print("Learning *args and *kwargs")

# *args
# Suppose we do not know how many arguments does the function takes in before hand
# *args used during function definition
print()
def add(*args):
    print(args)
    print(type(args))

add(10, 20)
add(10, 20, 40, 60, 30, 67, 99, 36, 99, 72)

# * in the args tells Python: "Collect all extra positional arguments into one variable"
# args receives them as tuples
# args is conventional name but we can have any name 
# but preceding with * to collect all arguments into one variable
print()
def add(*numbers):
    print(numbers)
    print(type(numbers))
    print(len(numbers))

add(1, 2, 4, 5, 8, 9, 4345, 45, 342, 767)

# Tuple can contain any type 
print()
def show(*args):
    print(type(args))
    print(args)

show(5, "hello", True) #int, str, bool

# Add any number of numbers using *args
print()
def add(*args):
    total = 0
    for number in args:
        # total = total + number
        total += number
    return total

result = add(10, 20, 30, 40, 50)
print(result)

# Another Example
print()
def show(*args):
    print(args[0])
    print(args[1])
    print(len(args))

show("A", "B", "C", "D")

# *args collects an arbitrary number of positional arguments into a tuple

# normal parameters + *args together
print()
# first is a normal parameter, so it gets the first positional argument
# *args collects the remaining positional arguments
# *args collects all positional arguments that remain after the normal positional parameters 
# have received theirs
def show(first, *args):
    print(first)
    print(args)

show("A", "B", "C", "D")

# Another example
# Normal positional parameters take their arguments first; 
# *args collects the remaining positional arguments into a tuple
print()
# args returns tuple
def show(name, age, *args):
    print(name, type(name))
    print(age, type(age))
    print(args, type(args))

show("Alice", 25, "Python", "AI", "ML")

# empty args
print()
def show(name, age, *args):
    print(name)
    print(age)
    print(args)

show("Alice", 25)

#  *args 
# *args used during function call

print()
numbers = [10, 20, 30] #list

def add(a, b, c):
    return a + b + c

try:
    result = add(numbers)
except TypeError:
    print()
    print("Missing 2 required positional arguments b and c")
else:
    print()    
    print(result)
finally:
    print()
    print("Learning about using *args during function call")

# Using *args in function call
print()
try:
    # *numbers (*args) when used during function call
    # unpacks the elements of numbers and pass them as separate positional arguments
    add_num = add(*numbers)
except TypeError:
    print()
    print("Missing required positional arguments")
else:
    print()    
    print(add_num)
finally:
    print()
    print("Learning about using *args during function call")

# During *args used in function defintion (*args in the parameters part)
# def show(*args):
# * means pack/collect positional arguments into a tuple

# During *args used in function call (*args in the arguments part)
# show(*numbers)
# * means unpack/distribute iterable elements into positional arguments

# Another Example

values = [5, 10, 15]
print()
def show(a, b, c):
    print(a)
    print(b)
    print(c)

show(*values)

# Another error scenario

values = [5, 10]
print()
def show(a, b, c):
    print(a, b, c)
try:
    show(*values)
except TypeError:
    print()
    print("One Positional argument missing expected for c")


# **kwargs
# keyword arguments which is counterpart to *args 

# *kwargs is keyword arguments that packs the key value arguments as a dictionary
# when used during function defintition
print()
def show(**kwargs):
    print(kwargs)
    print(type(kwargs))

show(name = "Pradeep", age = 36, language = "Python")

# another example
print()
def display(**information):
    print(information)
    print(type(information))

display(country = "India", continent = "Asia", rank = 1)

# When in function definition *args and **kwargs
# *args
#    ↓
# positional arguments
#    ↓
# tuple

# **kwargs
#    ↓
# keyword arguments
#    ↓
# dictionary

# Using *args and **kwargs together in function definition

# normal parameter
#       ↓
# specific positional argument

# *args
#       ↓
# remaining positional arguments → tuple

# **kwargs
#       ↓
# keyword arguments → dictionary


print()
def show(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

show("Alice", 25, "Python", age=30, city="Chennai")

# Using **kwargs during function call
# unpacks the dictionary into keyword arguments
# unpacks the dictionary into values

information = {"country": "India", "continent": "Asia", "rank": 1}
print()
def view(country, continent, rank):
    print(country)
    print(continent)
    print(rank)

view(**information)

# Function definition:

# *args
#   ↓
# collect positional arguments
#   ↓
# tuple


# **kwargs
#   ↓
# collect keyword arguments
#   ↓
# dictionary

# ---

# Function call:

# *args
#   ↓
# unpack iterable
#   ↓
# positional arguments


# **kwargs
#   ↓
# unpack dictionary
#   ↓
# keyword arguments

# Error case in **kwargs during function call

# If the keyword matches a parameter, it is assigned to that parameter. 
# If it doesn't match and the function has no **kwargs to collect it, Python raises TypeError.

print()
data = {
    "name": "Alice",
    "age": 25,
    "city": "Chennai"
}

def show(name, age):
    print(name, age)

try:
    show(**data)
except TypeError:
    # dictionary's keys must correspond to acceptable keyword parameters
    print("Dictionary's keys must correspond to acceptable keyword parameters")
    print("")

# *args (function definition) → collect positional arguments → tuple
# **kwargs (function definition) → collect keyword arguments → dictionary

# *values (function call) → unpack iterable → positional arguments
# **data (function call) → unpack dictionary → keyword arguments

# ----
# Exercise (all four in one)
# *args used in function definition and function call
# **kwargs used in function definition and function call

# normal parameter → positional argument
# *args → remaining positional arguments
# **kwargs → keyword arguments
# **data → unpack dictionary into keyword arguments
print()
def process(name, *args, **kwargs):
    print(name)
    print()
    print(args)
    print()
    print(kwargs)

data = {
    "age": 25,
    "city": "Chennai"
}

# process(
#     "Alice",
#     "Python",
#     "AI",
#     age=25,
#     city="Chennai"
# )

process("Alice", "Python", "AI", **data)

# Output

# Alice

# ('Python', 'AI')

# {'age': 25, 'city': 'Chennai'}

# ---

# lambda function

# A lambda function is a compact way to write or create small function

# A typical square function
def square(x):
    return x * x

# Lambda way of expression the same sqaure function

# syntax
# function defintion name = lambda parameters: expression
# major restriction is that a lambda contains one expression, whose result is automatically returned
# lambda function is intended for single expression alone and the result is automatically returned
# unlike def where multiple expression is possible
square = lambda x: x * x

# Example
add_ten = lambda x: x + 10
result = add_ten(5)
print()
print(result)

# lambda multplication function

multiply = lambda x, y: x * y
result = multiply(4, 5)
print()
print(result)

# Pass a function as an argument with lambda

def apply(function, value):
    return function(value)

# (lambda x: x * 2) is the function object
# (10) is the function call
# Create a lambda function object, immediately call that function with 10, 
# and return the resulting 20

result = apply(lambda x: x * 2, 10)

print()
print(result)

# Higher order functions map(), and filter()

# map() 
# passing functions as arguments and lambda functions becomes useful
# map() transforms every element
# Typical program to double a number without using map()

def double(x):
    return x * 2

numbers = [1, 2, 3, 4]

result = []

for number in numbers:
    result.append(double(number))
print()
print(result)

# Using map() function to every element of this iterable 
# we can write the above ddouble a number program in a compact manner
print()
# result = map(function object, iterable)
result = map(double, numbers)
# print(result) #returns a map object

# The syntax for using map() is list(map(function object, iterable))
print()
result = list(map(double, numbers))
print(result)

# Another example for map() with lambda function

numbers = [1, 2, 3]
# each element of the iterable becomes the argument for x, one at a time
# list(map(lambda function object, iterable))
result = list(map(lambda x: x + 10, numbers))
print()
print(result)

# filter()
# function + iterable
# keeps or removes elements based on a condition
# filter() does not transform the elements. 
# It tests each element and keeps the ones for which the function returns True
# list(filter(lambda function object, iterable)) with lambda function

numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print()
print(result)

# Another example for filter()
# filter() skips/keeps elements based on the Boolean result returned by the function
numbers = [3, 8, 11, 14, 17]
result = list(filter(lambda x: x > 10, numbers))
print()
print(result)

# map()     → element → function → transformed element
# filter()  → element → function → True/False → keep/discard

numbers = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2 != 0, numbers)
print()
print(list(result))

# same can be expressed using list comprehension
# [x for x in numbers if x % 2 != 0]

# Exercise 1

def process(numbers, function):
    result = map(function, numbers)
    return list(result)


numbers = [2, 4, 6]

output = process(numbers, lambda x: x + 3)

print()
print(output)

# Exercise 2

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)
# even_numbers is filter object
print()
# print(even_numbers) # returns a filter object
result = list(map(lambda x: x * 10, even_numbers))

print()
print(result)

# filter() → select
# map() → transform

# small practical problem where you have to decide yourself 
# whether to use a normal function, lambda, map(), filter(), or a comprehension
# That's where the concepts become programming skill

# Practical challenge
# output needed is squares of only the numbers greater than 10

# Which operation should happen first: filter() or map()?
# What should the first operation do?
# What should the second operation do?
# Would you use a normal def function, a lambda, or a combination?

# Pipeline: input → selection → transformation → output

numbers = [3, 8, 12, 5, 20, 7]

# comprehension and map
list_c = [x for x in numbers if x > 10]
result = list(map(lambda x: x ** 2, list_c))
print()
print(result)

# filter and map
list_f = filter(lambda x: x > 10, numbers)
result = list(map(lambda x: x ** 2, list_f))
print()
print(result)

# comprehension
result = [x * x for x in numbers if x > 10]
print()
print(result)

# Knowing multiple ways to solve something is not the end of programming skill
# Choosing the clearest appropriate way is part of programming skill

def square_number(number):
    return number ** 2

squared = []
for number in numbers:
    if number > 10:
        # squared.append(square_number(number)) # using a function
        # squared = squared + [number ** 2] # without using a function
        squared += [number ** 2] # without using a function
print()
print(squared)


