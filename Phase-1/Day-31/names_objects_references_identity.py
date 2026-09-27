# Names, objects, references, and identity

# Names are labels 
# Objects are actual things

# x is a name bound to an object 10
x = 10

# y is a name that bounds to the same object 10
y = x

# print

print()
print(x)
print(y)

# object identity
print(x is y)

# Exercise
print()
x = 10
y = x
# x is a name that rebinds to another object 20 
# (this is not replacing the object 10 because object 10 is still there)
x = 20 
# y = x
print(x)
print(y)
print(x is y)


# Python's built-in function
# id()
# id() is an integer that uniquely identifies an object during that object's lifetime
# Do not treat 4391069048 as some permanent ID attached to the value 10
print()
x = 10
y = x

x = 20

# identity of the object that x refers to
print(id(x))
# identity of the object that y refers to
print(id(y))

print(id(x) == id(y))
print(x is y)

# Tracing Exercise

x = 10
y = x
z = y

y = 20

print(x)
print(y)
print(z)

print(x is z)
print(x is y)

# Names point to objects. Assignment binds or rebinds names. 
# Objects have identity. Multiple names can refer to the same object. 
# Rebinding one name does not automatically affect the other names.


# Reference relationship:
# x ─────► object
# Identity:
# object ─────► 4391069048
# So when we say:
# "y references the same object as x"
# we mean:
# x ───────► object ◄─────── y
# When we say:
# "The object's identity is 4391069048"
# we mean:
# object
#    │
#    └── identity → 4391069048
# One final subtlety
# Don't think of Python as literally storing:
# x = memory_address_4391069048
# That's an implementation-level way of imagining it.
# At the Python language level, the safest model is:
# Names are bound to objects, and objects have identities.


# Do not treat id() as "the memory address."
# In CPython, which is the standard Python implementation you're using on your Mac, id()
# is typically the object's memory address.
# So you may encounter explanations like:
# "id() returns the memory address of the object."
# That's approximately true for CPython.
# But Python itself guarantees something slightly different:
# id() returns a unique identity for the object during its lifetime.
# Other Python implementations do not have to represent that identity as a raw memory address.
# Therefore, the best mental model is:
# id(object)
#      ↓
# object's identity number
# rather than:
# id(object)
#      ↓
# memory address
# The latter happens to be how CPython commonly implements it.




# Mental Model

# 1. NAME
#    x, y

# 2. OBJECT
#    10, 20, [1, 2], {"name": "Alice"}, ...

# 3. BINDING
#    x = 10
#    means x → object 10

# 4. IDENTITY
#    identifies the particular object
#    x is y → same object?