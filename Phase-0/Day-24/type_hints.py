# Type Hints

# When projects become larger, type hints make code easier to understand, maintain, refactor, 
# and work on with other developers 

# Type hints describe what we expect 
# They generally do not enforce types at runtime

# Without Type Hints

def add(a, b):
    return a + b

print(add(5, 3))
print(add("Pradeep", " Kumar"))
print(add(2.5, 3.5))

# With Type Hints

# a      → expected to be int
# b      → expected to be int
# return → expected to be int

# The syntax is parameter: type
# -> return_type
# a should be an int, b should be an int, and the function is expected to return an int

def add_num(a: int, b: int) -> int:
    return a + b
# Type hint ≠ runtime type enforcement
# Type hints are useful for developers, IDEs, linters, and static type checkers
print(add_num("Pradeep", " Kumar"))

# Variables with type hints
# Communicating the intended type explicitly
# The syntax is variable: type = value

name: str = "Pradeep"
age: int = 36
height: float = 171.0
is_learning: bool = True

# Lists with type hints
# The syntax is variable: collection[type] = [value1, value2, .....]

numbers: list[int] = [1, 2, 3] #numbers is expected to be a list containing integers
names: list[str] = ["Alice", "Bob", "Charlie"] #names is expected to be a list containing strings
scores: list[float] = [3.5, 4.25, 5.0] #scores is expected to be a list containing floats
choose: list[bool] = [True, False, False, True, True] #choose is expected to be a list containing booleans

# Dictionary with type hints
# keys   → str, values → int
# dict[str, int]
#     │     │
#     │     └── value type
#     └────── key type

marks: dict[str, int] = {"Alice": 56, "Bob": 69}
# print(type(marks))

# Why Type Hints are important for AI Engineering?
# Because when someone reads the code will immediately gets information about the interface
# Example

# def embed_text(text: str) -> list[float]:
    # ...

# This says input is string and output is a list of floats
# It is particularly valuable when we work with APIs, Data Pipelines, 
# ML Preprocessing, Model Interfaces, Embeddings, RAG, Agent Tools, Large Multi-file Applications
# Type hints become a kind of documentation built into the code

# Useful Distinction

# Runtime type
# numbers = [10, 20, 30]
# What an object actually is - type is list

# Type hint
# numbers: list[int]
# What we are saying the variable/ parameter is expected to be - this is an annotation

# Static type checking
# A tool can inspect your code and say:
# "You said numbers should be list[int], but you're passing something else."
# For example, tools such as mypy or IDE tooling can analyze the annotations

# Mental Model

# Actual object
#      ↓
# runtime Python

# Expected type
#      ↓
# type hint

# Checking the expectation
#      ↓
# static type checker / IDE

# This distinction will become useful later when we're writing larger AI applications

# An example to see this distinction

def greet(name: str) -> str:
    return "Hello " + name 

# x = greet(100) #raises TypeError and this is runtime check and not based on type hint and not any static type check
print()
# print(x)

# Optional/ None
# Suppose a user may or may not have a name
# name may contain a str or None
# This is useful in APIs and real applications because data isn't always present

def greet(name: str | None) -> str:
    if name is None:
        return "Hello!"
    return "Hello " + name

print(greet("Pradeep"))
print(greet(None))

# def find_user(user_id: int) -> dict | None: # returns either a dictionary object or none value
    # ...
# communicates an interface:

# Input:
#     user_id → int

# Output:
#     dict OR None

# By seeing the interface written this way the caller can write confidently the program as

# user = find_user(123)

# if user is None:
#     print("User not found")
# else:
#     print(user)

# That kind of explicit contract becomes increasingly valuable when we have APIs, databases, 
# RAG retrieval, agent tools, and multiple components communicating with one another

