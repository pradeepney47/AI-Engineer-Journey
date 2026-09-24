# Iterators, enumerate(), Generators & Context Managers

# 1. Iterators

numbers = [10, 20, 30]

for number in numbers:
    print(number)
print()

# Underneath the for loop, Python is doing something conceptually like:
# list
#  ↓
# iterator
#  ↓
# give me next item
#  ↓
# give me next item
#  ↓
# give me next item
#  ↓
# nothing left

# An iterator is an object that produces values one at a time

# We can explicitly obtain an iterator using iter():

numbers = [13, 26, 43]

iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))
print()



# under the iterator the code may look something like this

# it = iter(numbers)

# while True:
#     try:
#         number = next(it)
#         print(number)
#     except StopIteration:
#         break


# Distinction between iterable and iterator

# Iterable
# An iterable is an object that Python can get an iterator from

# numbers is a list (collection object) which is iterable
# other iterables include tuple, string, dict, set, range

numbers = [10, 20, 30]
it = iter(numbers)

# Iterator
# An iterator is the object that actually produces the values one at a time

it = iter(numbers)

next(it)  # 10
next(it)  # 20
next(it)  # 30


# Iterable
#    │
#    │ iter()
#    ▼
# Iterator
#    │
#    │ next()
#    ├── 10
#    ├── 20
#    └── 30


# Iterable = something you can iterate over.

# Iterator = something that gives you the next item.

# Example

numbers = [10, 20, 30]

it = iter(numbers)

print(type(it))
print(it)
print()
print(iter(it))
print(type(iter(it)))
# numbers is the iterable
# it is the iterator

# Why cannot we directly do?
# Because numbers itself is an iterable
# next() expects an iterator, not merely an iterable
# next(numbers)

# iter(iterable)
# next(iterator)


# 2. enumerate()
# enumerate() takes an iterable and produces pairs containing an index and the corresponding value

print()
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name)

# What if we also want position or index?

# One way (our way):
print()
index = 0
for name in names:
    print(index, name)
    index += 1

# Python's way to see the index/ position
print()
for index, name in enumerate(names):
    print(index, name)

# Conceptually:
# names
#    ↓
# enumerate(names)
#    ↓
# (0, "Alice")
# (1, "Bob")
# (2, "Charlie")

# Then the for loop unpacks each pair:
# for index, name in enumerate(names):

# For the first iteration:
# (index, name)
#     ↓
# (0, "Alice")
# So:
# index = 0
# name  = "Alice"

# then second, third

# We can choose the start of the index
# By default it is 0 but we can set as we wish

names = ["Alice", "Bob", "Charlie", "Dan", "Eve", "Fergie", "Gene", "Iva", "John"]
print()

# enumerate(names, start=3) produces an enumerate iterator that pairs each item with a counter as you iterate

for name, index in enumerate(names, start=3): # the index starts at 3 and the corresponding value that starts with 3 is Alice
    print(name, index)


# enumerate object

result = enumerate(["a", "b", "c"])
print()
print(type(result)) # this is an iterator (returns enumertor which is an iterator object)

print(next(result)) # returns a tuple of index and the value (next(iterator))

# iterable → iterator → values

# list or collection object → enumerate iterator → (index, value) tuples



# 3. Generators
# A generator is a convenient way to create an iterator that produces values one at a time


print()
# function definition
def get_numbers():
    return [10, 20, 30]

# function call
numbers = get_numbers()

print(numbers)

# With generators (a convenient way to create an iterator that produces values one at a time)

def get_numbers():
    yield 10
    yield 20
    yield 30

numbers = get_numbers()

print()
print(type(numbers)) # generator type
print(numbers) # this is a generator object (so it is an iterator)
print()
print(next(numbers))
print(next(numbers))
print(next(numbers))

# The interesting part: yield
# When Python reaches:
# yield 10

# the function pauses.
# It doesn't terminate permanently like return.


# Conceptually:
# get_numbers()
#      ↓
# yield 10
#      ↓
# PAUSE
#      ↓
# next()
#      ↓
# resume
#      ↓
# yield 20
#      ↓
# PAUSE
#      ↓
# next()
#      ↓
# resume
#      ↓
# yield 30
# So yield means roughly:
# "Give this value to the caller now, but remember where I was so I can continue later."

# That's why generators are useful for producing values lazily, one at a time.

# Compare return vs yield
# def normal():
#     return [10, 20, 30]

# call function
#      ↓
# create entire list
#      ↓
# return list
# Generator:
# def generator():
#     yield 10
#     yield 20
#     yield 30

# call function
#      ↓
# generator object
#      ↓
# next() → 10
#      ↓
# next() → 20
#      ↓
# next() → 30
# This becomes particularly valuable when dealing with large amounts of data.
# Imagine:
# 10 million records
# You may not want to construct a giant list containing all 10 million records in memory before processing anything.
# A generator can produce:
# record 1
#    ↓
# process
# record 2
#    ↓
# process
# record 3
#    ↓
# process
# ...
# one at a time.


# Exercise

def numbers():
    yield 10
    yield 20
# x is a generator object, and a generator is an iterator
x = numbers()
print()
print(next(x)) #It gives 10 back and pauses
print(next(x)) #It gives 20 back and pauses

# Generator function → generator object → iterator → next() → one value at a time

# yield pauses and preserves the function's execution state, which is the key difference from return

# Exercise

def numbers():
    yield 10
    yield 20

x = numbers()
print()
print(next(x))
print(next(x))
# print(next(x)) #StopIteration because third next() → nothing left

# An iterator produces values until it has no more values, then raises StopIteration
# A for loop handles that StopIteration automatically, which is why you normally don't see 
# the exception when using generators in a for loop.

# Exercise
# Calling a generator function does not execute its body



print()
def numbers():
    for i in range(3):
        yield i

# x = generator object
    #   ↓
    #   [paused before the function body even starts]

# Python creates the generator object, but the for loop hasn't started yet

x = numbers()

print(next(x))
print(next(x))


# x = numbers()
#       ↓
# generator object created
#       ↓
# PAUSED, nothing executed yet

# next(x)
#       ↓
# run until yield
#       ↓
# yield 0
#       ↓
# PAUSE

# next(x)
#       ↓
# resume
#       ↓
# yield 1
#       ↓
# PAUSE

# next(x)
#       ↓
# resume
#       ↓
# yield 2
#       ↓
# PAUSE

# next(x)
#       ↓
# resume
#       ↓
# loop finished
#       ↓
# StopIteration

# A generator object does not "contain the last yielded value."

# It contains the state needed to resume the computation.
# That's why generators are called lazy: they produce the next value only when requested

# How python knows the function is a generator function and not a normal function prior?

# Python determines this from the function's code itself, specifically the presence of yield.
# Consider:
# def numbers():
#     for i in range(3):
#         yield i

# When Python defines this function, it compiles the function body. During compilation, Python sees:
# yield i

# and marks the function as a generator function.
# So later, when you do:
# x = numbers()

# Python already knows:
# "numbers is a generator function, so calling it should produce a generator object rather than execute its body normally."

# Therefore:
# def numbers()
#        ↓
# Python compiles function
#        ↓
# sees `yield`
#        ↓
# marks it as generator function
#        ↓
# numbers()
#        ↓
# creates generator object
#        ↓
# function body has NOT started
# You can actually see this:
# def numbers():
#     yield 10

# print(type(numbers))
# print(type(numbers()))

# Conceptually:
# type(numbers)   → function
# type(numbers()) → generator
# Notice the distinction:
# numbers is the generator function.
# numbers() creates the generator object.
# And that generator object is what next() operates on:
# x = numbers()

# next(x)

# The deeper Python rule
# A normal function:
# def normal():
#     return 10

# When called:
# x = normal()

# the body executes immediately:
# normal()
#    ↓
# execute body
#    ↓
# return 10
#    ↓
# x = 10
# A generator function:
# def generator():
#     yield 10

# When called:
# x = generator()

# the body doesn't execute yet:
# generator()
#    ↓
# create generator object
#    ↓
# x = generator object
#    ↓
# wait for next()
# So the presence of yield changes the calling semantics of the function.


# Python has two different stages here:
# 1. When Python encounters def
# Python does not execute the function body line by line.
# It first compiles the function body into Python bytecode and creates a function object.
# So:
# def numbers():
#     for i in range(3):
#         yield i

# When Python reaches def, it effectively determines:
# "This function contains yield, so this is a generator function."

# But it does not execute:
# for i in range(3):

# yet.
# 2. When you call the function
# For a normal function:
# def add():
#     x = 10
#     return x

# y = add()

# Calling add() starts executing its already-compiled body:
# add()
#  ↓
# x = 10
#  ↓
# return 10
# For a generator function:
# def numbers():
#     yield 10
#     yield 20

# x = numbers()

# calling it has special generator semantics:
# numbers()
#  ↓
# create generator object
#  ↓
# DO NOT execute body yet
# Then:
# next(x)

# finally starts/resumes execution:
# start function
#  ↓
# yield 10
#  ↓
# pause
# So your idea is close
# You said:
# "Python executes line by line but somehow within def it knows it fully."

# A more precise mental model is:
# Python reads source
#        ↓
# compiles code
#        ↓
# sees `def`
#        ↓
# creates function object
#        ↓
# body is not executed
#        ↓
# later: function is called
#        ↓
# body executes according to its function semantics
# And yield is special because Python identifies it during compilation, before the function ever runs.
# This is also why this works:
# def numbers():
#     yield 10

# even though Python hasn't reached the yield during execution yet. 
# It already knows from the compiled function code that this is a generator function.
# This distinction between defining code and executing code is a very important Python mental model.

# Let's keep the generator model as:
# Define → Python compiles → detects yield → generator function
# Call → generator object created → body waits
# next() → execute/resume → yield → pause
# That completes the core generator concept.


# 4. Context Managers

# with open("data.txt", "r") as file:
#     data = file.read()

# The important question is:
# Why do we need with?
# Imagine you open a file manually:
# file = open("data.txt", "r")

# data = file.read()

# file.close()

# You have to remember to close the file.
# But with:
# with open("data.txt", "r") as file:
#     data = file.read()

# Python automatically handles the cleanup when the with block finishes.
# Mental model
# Think of a context manager as:
# Enter context
#      ↓
# Do some work
#      ↓
# Exit context
#      ↓
# Cleanup
# For a file:
# open file
#    ↓
# read/write
#    ↓
# leave `with` block
#    ↓
# file automatically closed
# And importantly, cleanup happens even if an exception occurs inside the block.
# Tiny exercise
# What do you think this prints?
# with open("test.txt", "w") as file:
#     print("Inside")

# print("Outside")

# A. Only Inside
# B. Inside then Outside
# C. Outside then Inside
# D. Error because the file isn't explicitly closed
# And one more question: when does Python close the file?


# B. is the answer
# Inside
# Outside
# And test.txt remains empty because print("Inside") writes to the console, not the file.
 

# There are actually two different outputs here:
# with open("test.txt", "w") as file:
#     print("Inside")

# print("Outside")

# What happens
# When Python enters:
# with open("test.txt", "w") as file:

# it opens test.txt for writing.
# Then:
# print("Inside")

# prints Inside to the console.
# It does not write "Inside" into the file because you're using normal print(), not file.write().
# Then Python reaches the end of the with block:
# with block ends
#       ↓
# file is automatically closed
# Then:
# print("Outside")

# prints:
# Inside
# Outside
# And test.txt will actually be empty.
# If we wanted "Inside" written to the file:
# with open("test.txt", "w") as file:
#     file.write("Inside")

# print("Outside")

# Now:
# test.txt → Inside
# console  → Outside
# The key idea
# with doesn't mean "write something to a file."
# It means:
# Set up a resource, use it, then clean it up automatically.

# Files are one example. Context managers are also used for things like database connections, locks, 
# network resources, and other resources that need reliable cleanup.
# So the mental model is:
# with → enter → use resource → leave → cleanup automatically.
# That completes the core idea of context managers.