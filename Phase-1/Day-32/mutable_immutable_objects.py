# Mutable objects and Immutable objects

# Can an object's state be changed after the object has been created?

# If yes, the object is mutable.
# If no, the object is immutable.

# Examples

# Immutable
# Integer object is immutable
# Why because x is rebinding to the object and not object changing itself
print()
x = 10
print(x, id(x))
x = 20
print(x, id(x))

# Mutable
# List object is mutable
print()
x = [10]
print(x, id(x))
x.append(20)
print(x, id(x))

# Exercise
print()
x = [10]
y = x

print(x, id(x))
print(y, id(y))
print(x is y)

# this is mutable or x is a name that is no rebinding with the object 20 but modifying itself by allowing 20
# append() mutates the existing list object
x.append(20)
# both the names x and y are still same so they produce the modified mutable list
print(x, id(x))
print(y, id(y))
print(x is y)

# Example
print()
x = [10]
y = x
print(x, id(x))
print(y, id(y))
print(x is y)

x = [10, 20]

print(x, id(x))
print(y, id(y))
print(x is y)

# Rebinding changes what a name refers to. Mutation changes the object itself.

# Don't classify an operation based only on the type of the object. Look at what the operation actually does

# A list being mutable means: "This type supports mutation."
# It does not mean: "Every operation involving a list mutates the list."

# So,
# Mutation changes an existing object 
# Rebinding changes which object a name refers to

print()
x = [10]
y = x

x.append(5)

print(x, id(x))
print(y, id(y))
print(x is y)


print()
x = [10]
y = x

x = x + [5]

print(x, id(x))
print(y, id(y))
print(x is y)

# Example
# Python concept: a mutating method like append can modify an object but return None

print()
x = [10]
y = x
print(x, id(x))
print(y, id(y))
print(x is y)

# But why does append() return None?
# list.append() is an in-place mutation operation. It modifies the list. 
# It does not need to produce another list as its result.
# So Python's list API makes this explicit by returning None


z = x.append(20)
y = z

print(x, id(x))
print(y, id(y))
print(z, id(z))
print(x is y)
print(y is z)
print(z is x)

# This gives us a very useful three-part distinction
# x.append(20)
#     │
#     ├── modifies existing object
#     └── returns None


# x + [20]
#     │
#     ├── does not modify original list
#     ├── creates a new list
#     └── returns that new list


# x = [10, 20]
#     │
#     ├── RHS creates/evaluates a list
#     └── x is rebound to that list

# So your experiment actually uncovered three concepts at once:
# mutation → return value → rebinding

# Python language/library API for lists (it is not HTTP API call)

# An API means, broadly:
# A defined interface through which you interact with some software component.

# Python defines that lists have methods such as:
# append()
# extend()
# insert()
# remove()
# pop()
# sort()
# These are part of the interface Python provides for working with lists.

# API (buit in and not over Internet or remote server)
# This is Python API

# Your Python code
#       ↓
# Python list API
#       ↓
# list object

# Example
# x.append(20)


# API (over Internet through a library)
# This is Library API
# We don't need to know the internal implementation of HTTP sockets, connection pooling, etc. 
# We use the interface provided by requests library

# Your Python code
#       ↓
# requests library
#       ↓
# HTTP request
#       ↓
# Internet
#       ↓
# Remote server API

# Example

# requests.get("https://jsonplaceholder.typicode.com/users/1")


# Web/HTTP API
# GET /users/1
# You communicate with a remote service through HTTP.

# OpenAI API
# client.responses.create(...)
# You communicate with an external AI service through its API.

# The underlying idea is the same:
# An API defines how you are allowed/expected to interact with a component
# without needing to know its internal implementation.

# And with an OpenAI API, you don't need to implement the model yourself. You use the API contract.
# This is actually one of the central ideas of software engineering: abstraction through interfaces.

# And yes, this connects directly to your AI Engineer journey. Later you'll constantly interact with APIs 
# at several layers: Python APIs, library APIs, database APIs, REST APIs, SDK APIs, and LLM APIs.


# When developers use FastAPI, they are usually using it to build a REST API. 
# FastAPI makes this process much quicker by providing built-in tools like 
# automatic Swagger documentation and Pydantic data validation. 
# However, FastAPI is flexible enough that it can also be used to build other types of API connections, 
# like WebSockets or GraphQL.


# Mutable vs Immutable

# Mutable: The state of the object can be modified
# list

print()
x = [10]
# mutates the existing list
x.append(20)
print(x)


# Immutable: Once that object exists, its internal state cannot be modified.
# integer

print()
x = 10
y = x
# rebinds x to the object 20
x = 20
print(x)


# Common immutable types include:
# int
# float
# bool
# str
# tuple
# frozenset

# Common mutable types include:
# list
# dict
# set

# Example
print()
x = 10
y = x

print(x is y)

# lists implement += through in-place extension, so the existing list can be mutated.
# That means += is another excellent example of why we need to understand 
# the operation + the object's type, rather than just memorizing syntax.

x += 1

print(x)
print(y)
print(x is y)

# Immutable object: its state cannot be changed. Operations that appear to "change" 
# its value instead produce another object/value and may rebind the name.

# Strings
# Strings: collection-like, but immutable
print()
x = "hello"
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])

# x[0] = "H" #TypeError (string is immutable)

x = "Hello"
print(x)

# Compare with list
# list
print()
x = ["h", "e", "l", "l", "o"]
print(x)
x[0] = "H"
# list is mutable
print(x)

# 
print()
x = "hello"
y = x
# string is immutable (cannot modify the existing string but this 
# upper() method of the string type can produce a new string)
x.upper() 
print(x) # prints hello
print(y) # prints hello
print(x is y) # True

# 
print()
x = "hello"
y = x
# string is immutable so this produces new string and x is rebinded to this new string
x = x.upper()
print(x) # prints HELLO
print(y) # prints hello
print(x is y) # False

# You can now recognize this family of operations:
# x = x.upper()
# x = x.replace("h", "H")
# x = x + "!"
# x = x.strip()
# For strings, these operations produce new strings rather than modifying the existing string.

# The original string object is immutable.

# Whereas with a list:
# x.append(...)
# x.extend(...)
# x.insert(...)
# the existing list can be modified.

# Don't interpret immutability as:
# "The value can never appear to change."
# Instead:
# "This particular object cannot have its state changed."
# That's why this is perfectly fine:
# x = "hello"
# x = "HELLO"
# The name changed what it refers to.
# The original "hello" object wasn't modified.

# Mutable
# The state of an existing object can be changed by an operation that mutates it
# object identity: same
# object state:    changed
print()
x = [10]
print(x, id(x))
x.append(20)
print(x, id(x))

# Immutable 
# The state of an existing object cannot be changed after the object is created
# object identity: x now refers to another object
# object state:    original 10 was not changed
print()
x = 10
print(x, id(x))
x += 1 # at this point the old object 10 is unreachable because x is rebinds to the new object 11
print(x, id(x))


# Once an object is no longer reachable, Python is allowed to reclaim its memory when appropriate.
# An object does not cease to exist merely because it has no name. 
# It becomes unreachable when nothing holds a reference to it.
# An object does not need a name or a reference to have an identity.


# Mutable/immutable describes what can happen to the object itself. Reassignment describes what happens to a name.

# Being mutable does not mean every operation changes the object.

# x = [10]
# y = x + [20]

# Lists are mutable, but + creates a new list rather than mutating x.

# Mental Model

#                  Operation
#                     │
#           ┌─────────┴─────────┐
#           ▼                   ▼
#       Mutates object      Creates/returns
#           │                another object
#           ▼                   ▼
#    existing state       name may be rebound
#       changes

# Name → reference → object → object lifetime

# An object can exist without having a name. If no references to it remain, it becomes unreachable 
# and may eventually be reclaimed. While the object exists, it has an identity. Once the object itself
# is reclaimed, that particular object's identity no longer exists.

# Object exists
#      ↓
# Object has identity
#      ↓
# References to it disappear
#      ↓
# Object becomes unreachable
#      ↓
# Object becomes eligible for reclamation
#      ↓
# Eventually reclaimed
#      ↓
# Object no longer exists

# id() gives you an integer identifying an object during that object's lifetime. 
# After the object is gone, Python can eventually reuse that identity value for another object.

#               reference exists?
#                     │
#           ┌─────────┴─────────┐
#          YES                  NO
#           │                    │
#    object reachable      object unreachable
#           │                    │
#       id(obj) works       cannot access it
#                                │
#                                ▼
#                     eligible for reclamation

# And importantly, the object having an identity and us being able to access that identity are two different things.
# The object can have an identity while unreachable, but you cannot retrieve that identity through id()
# once you have no way to obtain the object itself.





# Case += operation: behaving differently for mutable and immutable objects
print()
x = [10]
y = x
# Here append() is performing an in-place addition
# mutating the existing object
x.append(20)

print(x)
print(y)

# ----------------

print()
x = [10]
y = x
# Case += operation: behaving differently for mutable object
# Here += operation is performing an in-place addition
# mutating the existing object
x += [20]

print(x)
print(y)

# ----------------

print()
x = [10]
y = x
# RHS is evaluated first and then x rebinds to this new object
x = x + [20]

print(x)
print(y)

# Mutability describes what an object allows. It does not determine what every operation will do.
# A mutable list can be changed in place, but whether a particular expression actually changes 
# it in place depends on the operation.

# It just does not mean that every assignment involving a mutable object creates a new object. 
# += has its own in-place operation semantics.

# Three distinct operations

# x = x + [5]
#        ↓
# new list → rebind x

# x += [5]
#        ↓
# mutate existing list

# x.append(5)
#        ↓
# mutate existing list

# x += [item] can avoid creating a new list for the entire accumulated result on every iteration, 
# because the existing list is extended in place.
# That can reduce unnecessary allocations and copying.
# However, for building a list one item at a time, the most idiomatic choice is usually:
# x.append(item)

# deeper principle

# x = x + [item]
#         ↓
# create another list containing the combined contents

# x += [item]
#         ↓
# modify existing list in place

# x.append(item)
#         ↓
# modify existing list in place

# This is an excellent example of why mutable vs immutable + operation semantics + object identity all connect together.


# The core model

# Mutable object
#     │
#     ├── operation may mutate it
#     │       └── append(), extend(), list += ...
#     │
#     └── operation may instead create another object
#             └── list + list

# Immutable object
#     │
#     └── cannot mutate existing object
#             └── operation produces another value/object
#                 and the name may be rebound




# Mutable object inside an immutable object

# x = ([10, 20], 30)

# "The tuple is immutable, so nothing inside it can change."
# But that's not quite correct.
# A tuple is immutable, meaning its own elements/bindings cannot be changed.
# But an element can itself be a mutable object.


x = ([10, 20], 30)
print()
print(x[0])
print(x[1])

print(x[0][0])
print(x[0][1])

x[0][0] = 34 # mutable element 
x[0][1] = 36 # mutable element
# x[1] = 344
print(x)

print()
x[0].append(45)
print(x)

# x
# │
# ▼
# ┌─────────────────┐
# │  [10, 20]  │ 30 │
# └──────┬──────────┘
#        │
#        ▼
#     list object

# x[0] gives us access to the list object.

# Then:

# x[0].append(30)

# mutates that list:
# x
# │
# ▼
# ┌─────────────────────┐
# │ [10,20,30] │ 30     │
# └───────┬─────────────┘
#         │
#         ▼
#      same list object

# The tuple's structure is still:

# (element 0, element 1)

# It still contains:

# (list object, integer 30)

# We did not replace element 0 with another object.
# We changed the state of the list object that element 0 already referred to.

# Now compare this

# x[0] = [1, 2, 3]

# This does produce an error:
# TypeError: 'tuple' object does not support item assignment

# Why?
# Because now we're trying to change the tuple's structure:

# Before:
# tuple → [10,20] , 30

# After desired:
# tuple → [1,2,3] , 30
#           ↑
#      replace element 0

# That is forbidden because the tuple is immutable.

# So the crucial distinction is:
# Immutable container ≠ immutable objects inside the container.
# And this leads to a very useful general rule:
# Tuple
#   │
#   ├──► immutable object
#   │       → cannot change that object's state
#   │
#   └──► mutable object
#           → the object itself may still be mutated

# This is one of those Python concepts that is much easier to understand through object references 
# than through simply memorizing "tuples are immutable.

# Final Exercise

a = [10]
b = a

c = (a, 20)

a.append(30)

b = [40]

print(a)
print(b)
print(c)
print(c[0] is a)

# c[0] is a is True not merely because they both currently contain [10, 30],
# but because c[0] and a refer to the exact same list object.


a = [10, 30]
c = ([10, 30], 20)

print(a, id(a)) 
print(c[0], id(c[0]))

# Here,
# c[0] == a   # True (True because we are just checking whether both the values are same)
# But
# c[0] is a   # False (False because c[0] and a refer to different list object and not the same list object)

# That's the distinction between equality (==) and identity (is)

# Your core mental model is now:
# Names → references → objects → identity → state → mutation/rebinding → object lifetime

# And the central distinction:
# Mutation changes an existing object's state. Rebinding changes which object a name refers to.