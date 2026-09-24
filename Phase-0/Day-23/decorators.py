# Decorators

# Functions are objects

def greet():
    print("Hello")
    return "greeting"

x = greet() # x is a function object

# Function can receive another function

def greet():
    print("Hello")

def execute(func): # function receiving another function
    func()

execute(greet)

# Function can return another function

def greet():
    print("Hello")

def wrapper():
    def inner():
        print("Before")
        greet()
        print("After")

    return inner

new_function = wrapper()
print()
new_function()



# What is a decorator?
# A function that takes another function, wraps or modifies its behavior,
# and returns a function

def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper

def greet():
    print("Hello")

greet = decorator(greet)

print()
greet()
print(type(greet))
print(greet)


# Decorator
# Python gives us a cleaner way to write this

# def greet():
#     print("Hello")

# greet = decorator(greet)

# as seen in this below manner
print()
# @decorator means: take the function being defined and pass it through the decorator
@decorator
def greet():
    print("Hello")
greet()

# Mental Model for Decorator

# function object
#       ↓
# passed as argument
#       ↓
# decorator function
#       ↓
# wrapper function created
#       ↓
# wrapper returned
#       ↓
# original name points to wrapper
#       ↓
# calling original name
#       ↓
# wrapper executes
#       ↓
# wrapper calls original function

# -----

# BEFORE decoration:

# hello ─────► original hello function


# decorator(hello)
#        ↓
#     wrapper


# AFTER decoration:

# hello ─────► wrapper function
#                  │
#                  └── func ─────► original hello function

# ----

# decorator function

# func refers to function object for hello which is essentially hello = decorator(hello) which Python creates first 
# when @decorator is used before defining a function as decorator so that the decorator function is effectively called

# func refers to the original hello function object
def decorator(func):
# wrapper is the inner function object created inside decorator
# and because wrapper refers to func, it can call the original hello
    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


# AFTER decoration:

# hello ─────► wrapper function
#                  │
#                  └── func ─────► original hello function


@decorator
# hello = decorator(hello)
def hello():
    print("Hello")
print()
hello()

# hello
#  ↓
# wrapper
#  ↓
# Start
#  ↓
# original hello()
#  ↓
# Hello
#  ↓
# End

# Decorators with arguments

def decorator(func):

    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper

# @decorator
# def greet(name):
#     print("Hello", name)

# greet("Pradeep")


# Revise Decorators

# 1. Functions are objects
# 2. Functions can be passed to other functions
# 3. Functions can return functions
# 4. Decorators combine these ideas

# 1. Functions are objects

x = 10 # x is an integer object

# Same idea applies to function
def greet():
    print("Hello")
print()
y = greet # y is a function object
print()
print(y)
print()
y() # calls the same function
print()
z = greet() # call greet() and return the value from the function and store in the variable z


# Example
print()
def greet():
    print("Hello")

# Does not create another function
# It creates another reference to the same function object

x = greet #function object
x() # calls that function object

# greet ───────┐
#              ↓
#         [function object]
#              ↑
#              │
# x ───────────┘

# A function object is a Python object that exists in memory, 
# and names such as greet and x can reference it

# 2. Functions can be passed to other functions

# Functions are objects 

def greet():
    print("Hello")


def run_function(func):
    func()

print()
run_function(greet)
# run_function(greet()) #not this because we want to give the function itself to run_function, rather than execute it first


# run_function(greet)
#        ↓
# func ─────→ greet function object
#        ↓
# func()
#        ↓
# greet()
#        ↓
# Hello

# Example
print()
def say_hello():
    print("Hello")

print()
def execute(func):
    print("Before")
    func()
    print("After")


execute(say_hello) #passing function as an argument to another function

# 3. Functions can return functions
print()
def create_greeting():
    
    def greet():
        print("Hello")
    
    return greet #not return greet() because we are trying to return function object and not execute it/ or executed value

a = create_greeting() # a refer to the greet function object

print(a)
print()
a() # executes the function as we call the function greet(), and so Hello is printed

# Example
print()
def create_greeting():

    def greet():
        print("Hello")

    return greet


b = create_greeting() # returns a function object which is greet

print(b) # prints the function object 
b() # greet() is called and so prints Hello

# create_greeting()
#       ↓
# creates greet function object
#       ↓
# return greet
#       ↓
# x ─────→ greet function object

# The function greet was defined inside create_greeting, 
# but it continues to exist after create_greeting() has finished.

# That's possible because the returned function object is still referenced by x.
# This idea becomes very important later with closures, but we don't need to go there yet.



# 4. Decorators combine Functions can be passed into functions and Functions can be returned from functions into one

# A function that receives a function, creates a new function around it, and returns the new function

def greet():
    print("Hello")

def wrapper_function(func): # a function that receives a function as a parameter

    def wrapper(): # creates a new function within the function
        print("Before")
        func()
        print("After")

    return wrapper # returns the new function

greet_new = wrapper_function(greet) # decorating greet
print()
greet_new() #greet_new() is actually calling wrapper()

# Conceptually

# greet ─────────────→ [greet function]

# wrapper_function(greet)
#           ↓
#        creates
#           ↓
# wrapper ───────────→ [wrapper function]
#           ↓
#        return
#           ↓
# new_greet ─────────→ [wrapper function]

# or

# Before
#    ↓
# func()
#    ↓
# greet()
#    ↓
# Hello
#    ↓
# After

# So, we are taking greet (function object) and wrapping additional behaviour around it

#         ┌───────────────┐
#         │    wrapper    │
#         │               │
# Before ─┤               │
#         │    greet()    │
# After  ─┤               │
#         └───────────────┘

# Python gives us special syntax so we don't have to write:
# new_greet = wrapper_function(greet) manually

# We can write the same using special syntax called decorator

# @wrapper_function
# def greet():
#     print("Hello")

# and this is same as writing

# def greet():
#     print("Hello")

# greet = wrapper_function(greet)

print()

def wrapper_function(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper

# A function that takes another function, wraps additional behavior around it, and returns a function.

# function
#    ↓
# decorator
#    ↓
# wrapped function

# @ syntax is simply convenient Python syntax for applying that transformation

# greet ─────→ wrapper()
#                  │
#                  └──→ original greet()


# greet ─────────────→ wrapper
#                          │
#                          │ func
#                          ↓
#                     original greet


# This is why calling the decorated greet() can still execute the original greet code.
# You've now understood the actual mechanism, rather than memorizing "@ means decorator."

@wrapper_function
def greet():
    print("Hello")

print("Decorator")

greet() #calling the wrapper


# Why decorators are useful?

# Consider we have several functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# and I want to print function started and function finished around every function
# then without decorators I would have to repeat the logic in every function

# def add(a, b):
#     print("Function started")
#     result = a + b
#     print("Function finished")
#     return result

# def subtract(a, b):
#     print("Function started")
#     result = a - b
#     print("Function finished")
#     return result

# def multiply(a, b):
#     print("Function started")
#     result = a * b
#     print("Function finished")
#     return result

# # That's duplication.

# A decorator lets us separate the extra behavior from the actual function logic.

# Example
print()
def log_function(func):

    def wrapper():
        print("Function started")
        func()
        print("Function finished")

    return wrapper

@log_function
def greet():
    print("Hello")

print("Why use Decorators?")
greet()

# The important design idea is:
# Original function
#       +
# Additional behavior
#       ↓
# Decorated function
# The original function doesn't need to know that logging exists.

# Decorators with *args and **kwargs

def log_function(func):

    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function finished")
        return result

    return wrapper


@log_function
def add(a, b):
    return a + b

print()
result = add(2, 3)
print(result)

# Let's trace it.

# 1. add(2, 3)
# Because of:
# @log_function
# def add(a, b):
#     return a + b

# add now refers to wrapper.
# So:
# result = add(2, 3)

# is effectively:
# result = wrapper(2, 3)

# 2. Enter wrapper
# print("Function started")

# Output:
# Function started
# 3. Call the original function
# result = func(*args, **kwargs)

# Here:
# args = (2, 3)
# so:
# func(*args)

# effectively calls:
# original_add(2, 3)

# which returns:
# 5
# That 5 is stored in the wrapper's local result.
# It hasn't been printed yet.
# 4. Continue the wrapper
# print("Function finished")

# So:
# Function finished
# 5. Return the result
# return result

# returns 5 to:
# result = add(2, 3)

# Now the outer result contains 5.
# 6. Finally:
# print(result)

# prints:
# 5

# So the full flow is:
# add(2, 3)
#     ↓
# wrapper(2, 3)
#     ↓
# "Function started"
#     ↓
# original add(2, 3)
#     ↓
# 5
#     ↓
# "Function finished"
#     ↓
# return 5
#     ↓
# print(result)
#     ↓
# 5
# This distinction between the wrapper's result and the caller's result is worth understanding. 
# The inner one temporarily holds the return value so the decorator can do something before returning it.

# And this is why the decorator pattern is powerful:
# original function
#       ↓
# wrapper receives arguments
#       ↓
# extra behavior
#       ↓
# original function executes
#       ↓
# extra behavior
#       ↓
# return original result



# Let's isolate *args and **kwargs, because this is the part that often makes decorators 
# look more complicated than they really are.

# *args (collect as tuple)

# *args in function definition
# → collect

print()
def wrapper(*args): # * here in the function definition means collect all positional arguments into args
    print(args)
    print(type(args)) #tuple

wrapper(10, 20, 30)

# *args (unpacks the tuple)

# *args in function call
# → unpack

def add(a, b):
    return a + b

args = (2, 3)
add(*args) # * here in the function call now unpacks the tuple as arguments when passed to a function

# args = (2, 3)
#        ↓
# add(*args)
#        ↓
# add(2, 3)


# **kwargs in function definition collect keyword arguments into dict
# → collect

print()

def wrapper(**kwargs): # ** here in the function definition means collect keyword arguments into dict
    print(kwargs)
    print(type(kwargs))

wrapper(name="Alice", age=30)


# **kwargs in function call unpacks dict into keyword arguments
# → unpacks

data = {
    "name": "Bob",
    "age": 30
}

wrapper(**data) # ** here in the function call now unpacks dict into keyword arguments

# Example 
# Connect Decorator with *args and **kwargs

def log_function(func):

    def wrapper(*args, **kwargs):
        print("Function started")

        result = func(*args, **kwargs)

        print("Function finished")
        return result

    return wrapper

# The wrapper essentially says:
# "I don't care what arguments the original function expects. Give me whatever arguments you give it, and I'll pass them along."
print()
@log_function
def add(a, b):
    return a + b

res_add = add(2, 3)
print(res_add)
# wrapper(2, 3)
#      ↓
# args = (2, 3)
# kwargs = {}
#      ↓
# func(*args, **kwargs)
#      ↓
# func(2, 3)
#      ↓
# 5

# **kwargs
print()
@log_function
def greet(name):
    print(f"Hello {name}")

greet(name="Alice")

# The wrapper receives:
# args = ()
# kwargs = {"name": "Alice"}

# Then:
# func(*args, **kwargs)

# becomes effectively:
# func(name="Alice")

# So the original function receives exactly what it expected.

from functools import wraps

def log_function(func):
    # When writing real decorators, functools.wraps is usually used on the wrapper
    @wraps(func) # @wraps(func) preserves important metadata from the original function
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function finished")
        return result

    return wrapper


# Exercise for Decorator basics

def announce(func):

    @wraps(func) # @wraps(func) solves a metadata problem created by decorators
    def wrapper(*args, **kwargs):
        print("Starting")
        result = func(*args, **kwargs)
        print("Finished")
        return result

    return wrapper



# add is a name referring to the wrapper function object
# It is not an instance of the decorator function.
# It is not an instance of announce.

# So, add is a function object, specifically the wrapper function (a wrapper function object) 
# returned by announce (or decorator function)

# add = announce(add) # which is add = wrapper() and add does not refer to original add
@announce
def add(a, b):
    return a + b

# So after decoration, new_add actually refers to the wrapper function, not directly to the original add.

print()
result = add(5, 7)
print(result)
# print(add.__name__) # without @wraps(func) this will print wrapper and not add (prints add only when @wraps (func) is used)
# The original function's identity information has been replaced by the wrapper's metadata.
# add → wrapper
# @wraps(func) fixes that and reveals the identity even when wrapped
# "This wrapper is wrapping func. Preserve the important metadata of the original function."
# @wraps(func) does NOT change the actual execution behavior.
# @wraps(func) mainly preserves information about the original function while the wrapper is replacing its name.
# So you can remember:
# # Decorator changes behavior. @wraps preserves identity/metadata.
# @wraps(func) preserves and conveys the original function's metadata/identity information 
# even though the name now points to a wrapper.

# print(add.__doc__)


# Original function
#       ↓
#     add()
#       │
#       │ wrapped by decorator
#       ↓
#    wrapper()
#       ↑
#       │
#  @wraps(func)
#  "This wrapper represents add"


# Without @wraps:
# add → wrapper
#        └── name: "wrapper"


# With @wraps(func):
# add → wrapper
#        ├── __name__: "add"
#        ├── __doc__: original add's docstring
#        └── other important metadata from add


# One important nuance: the wrapper is still the object bound to the name add. 
# @wraps does not magically make add point directly to the original function. 
# It makes the wrapper carry the original function's identifying metadata.
# That's why this is such a useful distinction:
# Wrapping changes what happens.
# @wraps preserves who the wrapped function is.


# Your execution trace
# Because of:
# @announce
# def add(a, b):
#     return a + b

# Python effectively transforms it into:
# add = announce(add)

# So add now refers to the wrapper.
# Then:
# result = add(5, 7)

# becomes:
# wrapper(5, 7)
#     ↓
# "Starting"
#     ↓
# original add(5, 7)
#     ↓
# 12
#     ↓
# "Finished"
#     ↓
# return 12
#     ↓
# result = 12
# Then:
# print(result)

# prints:
# 12


# 1. "How can the decorator function be accessed as attributes?"
# I think you're referring to our earlier distinction:
# object.attribute

# versus:
# object.method()

# The important rule is:
# A method is also an attribute.

# A method is essentially an attribute whose value is a callable object, usually a function bound to an instance.
# For example:
# class Person:    
#   def greet(self):        
#       print("Hello")

# If:
# p = Person()

# then:
# p.greet

# is attribute access.
# And:
# p.greet()

# is:
# 1. attribute access to get greet
# 2. then calling the resulting callable
# So the () is what actually performs the call.
# Now apply that to add.__name__
# add is an object.
# So:
# add.__name__

# means:
# "Access the attribute named __name__ on the object referenced by add."

# There is no (), so we're not calling anything.
# Therefore:
# add.__name__

# is attribute access.
# Whereas:
# add(...)

# calls the callable object referenced by add.
# 2. What exactly is add?
# This is the most important part.
# Consider:
# from functools import wraps
# 
# def announce(func):    
#   @wraps(func)    
#   def wrapper(*args, **kwargs):        
#       print("Starting")        
#       result = func(*args, **kwargs)        
#       print("Finished")        
#       return result    
#   return wrapper

# Then:
# @announce
# def add(a, b):    
#   return a + b

# Python effectively transforms this into:
# def add(a, b):    
#   return a + b
# 
# add = announce(add)

# Now let's trace it.
# Before decoration
# add
#  ↓
# original function object
# Then:
# announce(add)

# The decorator receives the original function:
# func
#  ↓
# original add function object
# Inside announce, we create:
# wrapper

# which is itself a function object.
# Then:
# return wrapper

# So:
# announce(add)

# returns the wrapper function object.
# Finally:
# add = announce(add)

# means:
# add
#  ↓
# wrapper function object
# Therefore:
# add is a name referring to the wrapper function object.

# It is not an instance of the decorator function.
# It is not an instance of announce.
# It is a function object, specifically the wrapper function returned by announce.
# So what happens with add.__name__?
# Because:
# add
#  ↓
# wrapper function object
# we are effectively doing:
# wrapper.__name__

# But because we used:
# @wraps(func)

# the wrapper's metadata was updated to reflect the original function.
# So:
# add.__name__

# gives:
# "add"
# Even though:
# add
#  ↓
# wrapper function
# That's the clever part of @wraps.
# What is __name__?
# __name__ is an attribute associated with a Python function object.
# For example:
# def hello():    
#   pass

# The function object has information associated with it:
# hello function object
# │
# ├── __name__
# ├── __doc__
# ├── __module__
# ├── __annotations__
# └── ...
# So:
# hello.__name__

# returns:
# "hello"
# And:
# hello.__doc__

# returns the function's docstring.
# For example:
# def hello():    
#   """Say hello."""    
#   pass

# Then:
# hello.__name__

# → "hello"
# and:
# hello.__doc__

# → "Say hello."
# What about those double underscores?
# This:
# __name__

# has a special naming convention.
# The double underscores on both sides are called dunder, short for double underscore.
# So:
# __name__
# is pronounced:
# "dunder name"

# Other examples you've probably encountered:
# __init____str____repr____len__

# These are commonly called dunder methods/attributes, although __name__ itself is an attribute rather than a method.
# The important thing is:
# Double underscores do not mean "method."

# They indicate names with special meaning in Python's data model or built-in machinery.
# And your final question: Is . accessing a method?
# No. . means attribute access.
# This distinction is extremely important.
# Suppose:
# add.__name__

# The . means:
# "Get the __name__ attribute from add."
# No call occurs.
# But:
# add(5, 7)

# means:
# "Call the callable object referenced by add."
# And:
# some_object.method()

# can be mentally decomposed as:
# some_object.method
#         ↓
# attribute access
#         ↓
# method object
#         ↓
# ()
#         ↓
# call it
# So . itself never means "call a method."
# It means access an attribute.
# The complete picture
# This is the mental model I want you to keep:
#                     add
#                      │
#                      ▼
#              wrapper function object
#                      │
#           ┌──────────┴──────────┐
#           ▼                     ▼
#       __name__               __doc__
#           │                     │
#           ▼                     ▼
#        "add"             original docstring
# And because of:
# @wraps(func)

# the wrapper carries the important metadata of the original add.
# So:
# add.__name__

# means:
# Take the function object currently referenced by add, then access its __name__ attribute.

# And:
# add(5, 7)

# means:
# Take the function object currently referenced by add and call it.

# That distinction between attribute access and calling the object obtained through attribute access 
# is a very important Python mental model.




# Your understanding of . is correct, but math_ops is not necessarily an instance object. It depends on how math_ops was created.
# Suppose we have:

# class MathOps:    
#     def sum(self, a, b):        
#         return a + b

# math_ops = MathOps()

# Then yes:

# math_ops.sum(3, 2)

# can be broken down as:

# math_ops
#    ↓
# instance object of MathOps
#    ↓
# .sum
#    ↓
# attribute access
#    ↓
# bound method
#    ↓
# (3, 2)
#    ↓
# call

# So your statement:
# sum is an attribute, although it is a method, and we access it through .

# Exactly right.


# But math_ops could also be a module

# Remember our Day 22 example:

# import math_tools

# math_tools.add(3, 2)

# Here:

# math_tools
#    ↓
# module object
#    ↓
# .add
#    ↓
# function object
#    ↓
# (3, 2)

# math_tools is not an instance of a class in this case. 
# It is a module object.

# So the universal rule is:

# . performs attribute access on an object.

# The object could be:

# - an instance
# - a module
# - a class
# - a function
# - etc.

# And the thing you retrieve through . could itself be a:

# - value
# - function
# - method
# - class
# - property
# - another object

# Then () means call the callable object you just accessed.

# So:
# math_ops.sum(3, 2) is conceptually:

# temp = math_ops.sum   # attribute access

# temp(3, 2)            # call

# That is the mental model I want you to keep.

# . → attribute access
# () → call the callable obtained
# And a method is an attribute whose value is callable, 
# with the exact behavior depending on whether it is accessed through an instance, class, etc.

# Decorator
# @property
print()
class Home():
    @property
    def bedroom(self):
        print("Is a room to take a nap or to rest!")

room = Home()
# → property → attribute-style access
room.bedroom #this is decorator type property and so the method inside the class is accessed as an attribute 

print()
class House():
    def naproom(self):
        print("Is a place to take nap!")

space = House()
# → normal method → explicit call
space.naproom() #normal method requires explicit use of () to access the method inside the class



# Mental Model

# Function → object
#         ↓
# can have attributes
#         ↓
# can be passed/returned
#         ↓
# can be wrapped by decorators
#         ↓
# @wraps → preserve metadata
# @property → expose getter through attribute-style access



# To use a class method as a decorator inside a class
# Move the decorator function outside of the class definition so it lives in the global scope

# Example

print()
def awesome(func): #decorator function
    def wrapper(*args, **kwargs):
        print("City is a place where people wish to migrate!")
        return func(*args, **kwargs)
    return wrapper

class City:
    @awesome
    def region(self):
        print("Region is otherwise called place!")

c = City()
c.region()


# Another example

print()
from functools import wraps
class City:
    @staticmethod
    def awesome(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            print("City is a place where people wish to migrate!")
            return func(self, *args, **kwargs)
        return wrapper

    def region(self):
        print("Region is otherwise called place!")

# Apply the decorator manually after City is created
City.region = City.awesome(City.region)

# Usage
c = City()
c.region()