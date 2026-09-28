# Function Arguments References Scope

# Python does not pass variables by reference or by value in the simple traditional sense.

# A more precise model is:
# When a function is called, the parameter name is bound to the object supplied by the caller.

# function definition
# A function parameter that is parameter_p is a local name
def change(parameter_p):
    # Rebinding inside the function
    # Rebinding the parameter_p as 20 does not rebind the caller's name argument_a
    parameter_p = 20
    # return parameter_p

argument_a = 10 # object

# function call
# result_b = change(argument_a)

# When change(argument_a) is called, the parameter_p is bound to the argument_a or object supplied by the caller

# Calling the function binds that local name that is parameter_p to the object that is argument_a supplied by the caller
change(argument_a)

# The local name parameter_p disappears from the function's local scope.

print(argument_a) # prints 10
# print(result_b)

# The key principle
# The function received access to the object, but:
# Rebinding the parameter does not rebind the caller's name.
# This is why saying simply "Python passes by reference" can be misleading.
# A more precise Python mental model is:



# Step 1: Before the call
# a ─────► 10
# Step 2: Function call
# When we call:
# change(a)
# the parameter x becomes bound to the same object that a refers to.
# a ──┐
#     ├──► 10
# x ──┘
# At this point, a and x refer to the same integer object.
# Step 3: Inside the function
# x = 20
# This does not change the integer 10.
# Integers are immutable.
# Instead, x is rebound:
# a ─────► 10

# x ─────► 20
# Step 4: Function returns
# The local name x disappears from the function's local scope.
# a ─────► 10
# Therefore:
# print(a)
# → 10



# caller:

# a ─────► object


# function call:

# a ──┐
#     ├──► same object
# x ──┘


# x = something_else:

# a ─────► original object
# x ─────► new object

# A function parameter is a local name. 
# Calling the function binds that local name to the object supplied by the caller. 
# Rebinding the parameter does not rebind the caller's name.

# A function parameter is a local name.
# A function parameter that is parameter_p is a local name.

# Calling the function binds that local name to the object supplied by the caller. 
# Calling the function binds that local name that is parameter_p to the object that is argument_a supplied by the caller. 


# Rebinding the parameter does not rebind the caller's name.
# Rebinding the parameter_p as 20 does not rebind the caller's name argument_a.





# Mutable objects as function arguments
print()
def add_item(items):
    items.append(20)

numbers = [10]

add_item(numbers)

print(numbers)


# Exactly right. Your reasoning is precise.

# Trace it

# Before the call:
# numbers ─────► [10]

# When we call:
# add_item(numbers)

# Python binds the parameter items to the same object:

# numbers ──┐
#           ├──► [10]
# items ────┘

# Then:

# items.append(20)

# append() mutates that existing list:

# numbers ──┐
#           ├──► [10, 20]
# items ────┘

# So after the function returns:

# print(numbers)
# produces:
# [10, 20]

# And yes, your distinction is important:

# The argument is not copied. The parameter is bound to the same object. 
# Because the object is mutable, the function can mutate that shared object.

# One refinement: mutability itself does not automatically cause the mutation. 
# The operation must actually mutate the object. append() does.


# Example
print()
def add_item(items):
    items = items + [20]

numbers = [10]

add_item(numbers)

print(numbers)

# Trace

# Before the call:
# numbers ─────► [10]

# At the function call:

# numbers ──┐
#           ├──► [10]
# items ────┘

# Then:
# items = items + [20]

# The important part is items + [20].

# + creates a new list:

# numbers ─────► [10]

# items ───────► [10, 20]

# Then the assignment binds the local name items to that new list.

# When the function returns, the local items binding disappears. Therefore:

# print(numbers) gives: [10]

# The key distinction

# Code	                What happens

# items.append(20)	    Mutates existing list
# items += [20]	        For a list, typically mutates existing list in place
# items = items + [20]	Creates a new list and rebinds items


# So your mental model is now:

# Function argument
#        ↓
# parameter binds to same object
#        ↓
#  ┌─────┴─────┐
#  ↓           ↓
# mutate     rebind
#  ↓           ↓
# caller      only local
# sees it     name changes

# This is the heart of Python argument semantics.




# Mutation vs rebinding inside functions
print()
def change(items):
    items.append(20)
    items = [100, 200]

numbers = [10]

change(numbers)

print(numbers)

# Exact trace

# Initially:

# numbers ─────► [10]

# Function call:

# change(numbers)

# Parameter binding:

# numbers ──┐
#           ├──► [10]
# items ────┘

# Step 1: mutation

# items.append(20)

# The existing list is mutated:

# numbers ──┐
#           ├──► [10, 20]
# items ────┘

# So the caller sees [10, 20].

# Step 2: rebinding

# items = [100, 200]
# A new list is created, and only the local name items is rebound:

# numbers ─────► [10, 20]

# items ───────► [100, 200]

# When the function returns, the local items binding disappears.

# Therefore:
# print(numbers)
# outputs:
# [10, 20]

# The principle
# Mutation changes the object. Rebinding changes what a name refers to.
# This distinction is extremely important in Python because you'll encounter it constantly with 
# functions, lists, dictionaries, classes, data processing, and eventually ML tensors/data structures.



# Scope
# What happens when the same name exists at different levels, such as local, global, and enclosing scopes

# Local Scope

# A variable created inside a function is normally local to that function:
print()
def greet():
    message = "Hello"
    print(message) # inside the function Python can find the message

greet()
# print(message) # outside the function Python cannot find the message and so it raises NameError

# because the name message exists only in the function's local scope.

# Think:
# Global scope
#     │
#     └── greet()
#           │
#           └── Local scope
#                 message ──► "Hello"





# Local vs global name

message = "Global"
print()
def greet():
    message = "Local"
    print(message, id(message))

greet()
print(message, id(message))


# Correct. The outputs are:

# Local
# Global

# Your core reasoning is right. There is one important refinement that will make your mental model more precise.

# What actually happens

# At module level:
# message = "Global"
# we have:
# Global scope

# message ─────► "Global"
# When greet() is called, Python creates a local scope for that function.

# message = "Local"

# Because message is assigned inside the function, Python treats message as a local name in that function:
# Global scope
# message ─────► "Global"

#         ↓

# greet() local scope
# message ─────► "Local"

# These are two different name bindings.

# So:
# print(message)
# inside the function finds the local binding first.

# After the function returns, the local binding disappears:

# Global scope
# message ─────► "Global"

# Therefore the outside print(message) finds the global binding.

# One correction to your explanation
# You said:

# "we are neither binding the function parameter to the caller argument..."
# That's true but isn't the reason for this particular behavior.

# This example has no parameter at all.
# The important rule is:

# An assignment to a name inside a function normally creates/rebinds a local name, 
# unless Python is explicitly told otherwise with global or nonlocal.

message = "Global"
print()
def greet():
    global message # this explicit declaration tells Python to not to create a local message; use the global binding
    message = "Changed" # this points to global
    print(message, id(message))

greet()

print(message, id(message))

# The scope rule we're building toward
# Python's name lookup is commonly described with LEGB:
# L → Local
# E → Enclosing
# G → Global
# B → Built-in
# We'll examine E, enclosing scope, next because that's where nested functions introduce another important layer.



# Enclosing Scope
# Now introduce a nested function
print()
def outer():
    message = "Outer"

    def inner():
        print(message)

    inner()

outer() # prints Outer

# Exactly.
# Outer
# Python finds message in the enclosing scope, which is the scope belonging to outer().
# The LEGB lookup
# When inner() executes:
# print(message)
# Python conceptually searches:
# 1. Local       → no message
# 2. Enclosing   → message = "Outer" ✓
# 3. Global      → doesn't need to look
# 4. Built-in    → doesn't need to look
# So:
# outer()
#   │
#   ├── message ─────► "Outer"
#   │
#   └── inner()
#         │
#         └── looks outward
#              ↓
#           finds message
# This is the E in LEGB.


# But what if inner() tries to rebind it?
print()
def outer():
    message = "Outer"

    def inner():
        message = "Inner"

    inner()

    print(message)

outer() # prints Outer


# Python treats message as a local name in inner().

# So the scopes are:

# outer() local scope

# message ─────► "Outer"
#        │
#        └── inner() local scope
#            message ─────► "Inner"

# The two message names are different bindings.
# When inner() finishes, its local message disappears. 
# The enclosing message remains "Outer".

# Then what is nonlocal?
# nonlocal explicitly tells Python:
# "I want this name to refer to the binding in an enclosing function scope, rather than creating a new local binding."
print()
def outer():
    message = "Outer"

    def inner():
        nonlocal message
        message = "Inner"

    inner()

    print(message)

outer() # prints Inner

# Because inner() is explicitly rebinding the enclosing message:

# outer() local scope

# message ─────► "Outer"
#        ▲
#        │
#        │ nonlocal
#        │
# inner()┘

# After:

# message = "Inner"
# the same enclosing binding now refers to "Inner".


# Very important distinction
# message = "Inner"
# inside inner():
# without nonlocal
# → creates/rebinds a local message.

# nonlocal message
# message = "Inner"
# → rebinds the enclosing function's message.

# So:
# Scope determines where a name belongs. 
# 
# nonlocal lets a nested function explicitly rebind an enclosing function's name.
# That completes the core enclosing scope concept.



# LEGB Tracing Exercise
# Combines arguments, mutation, rebinding, local scope, enclosing scope, and global scope

value = 10
print()
def outer(items):
    value = 20

    def inner():
        nonlocal value
        value += 5
        items.append(value)

    inner()
    items = [100]
    inner()

    return items, value


numbers = [1]

result = outer(numbers)

print(numbers)
print(result)
print(value)


# value   = 10 # global
# numbers = [1]
# items   = [1]
# value   = 20 # local name within the scope of outer function
# value   = 25 # nonlocal name within the scope of inner and outer function
# items   = [1, 25]
# numbers = [1, 25]
# items   = [100]
# value   = 30
# items   = [100, 30]

# returns
# items = [100, 30]
# value = 30

# prints
# numbers = [1, 25]
# result = ([100, 30], 30) # return from the functions
# value = 10 # global



# Step 1: Initial state

# Global:
# value ─────► 10

# numbers ───► [1]

# Call:
# outer(numbers)

# Inside outer():

# outer local:

# value ─────► 20

# items ─────► [1]
#               ▲
#               │
# numbers ──────┘

# Step 2: First inner()

# nonlocal value means inner() modifies outer()'s value.

# value += 5

# So:
# value = 25

# Then:

# items.append(value)
# mutates the shared list:

# numbers ──┐
#           ├──► [1, 25]
# items ────┘

# Step 3: Rebinding items

# Now:
# items = [100]
# This does not change numbers.

# Instead:
# numbers ─────► [1, 25]

# items ───────► [100]

# Step 4: Second inner()

# value is still the same enclosing binding:
# value += 5

# Therefore:
# value = 30

# Then:
# items.append(value)

# mutates the new list:
# items ───────► [100, 30]

# So:
# return items, value
# returns:
# ([100, 30], 30)

# And the global value was never modified:
# Global value ─────► 10

# Therefore:
# numbers = [1, 25]

# result = ([100, 30], 30)

# value = 10


# The 30 belongs to outer()'s enclosing/local binding, modified through nonlocal.

# So we have three different bindings:

# GLOBAL
# value ─────► 10

# outer()
# value ─────► 30

# result
#          └──► ([100, 30], 30)

# This is a very important distinction.


# Day 34 mental model

# Function calls bind parameter names to existing objects. 
# Mutation changes those objects. 
# Rebinding changes a name's binding. '
# 'Scope determines where a name is resolved. '
# 'nonlocal allows a nested function to rebind an enclosing function's name.

# That completes Day 34: Function Arguments, References & Scope.