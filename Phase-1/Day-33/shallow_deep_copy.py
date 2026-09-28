# Shallow copy and Deep copy

# If I want another object with the same contents, when do I get an independent object, 
# and when do nested objects remain shared?


# Shallow copy
# .copy()
print()
# a is a list that contains immutable integers
a = [10, 20]
# b is a list and it is a new object 
# shallow copy
b = a.copy() 

print(a)
print(b)
print(a is b)

print()
a.append(30)
print(a)
print(b)

print()
# a is a list that contains mutable lists as elements
a = [[10, 20], [30, 40]]
# b is a list and it refers to the same a[0] and a[1]
# shallow copy
b = a.copy()

print(a[0])
print(b[0])
print(a[0] is b[0])

# a ──► Outer List A
#        │
#        ├──► Inner List X [10, 20]
#        │
#        └──► Inner List Y [30, 40]


# b ──► Outer List B
#        │
#        ├──► Inner List X [10, 20]  ← SAME object
#        │
#        └──► Inner List Y [30, 40]  ← SAME object

print()
print(a is b)        # False
print(a[0] is b[0])  # True
print(a[1] is b[1])  # True

print()
print(id(a))
print(id(b))
print()
print(id(a[0]), id(a[1]))
print(id(b[0]), id(b[1]))

print()
a[0].append(50)
print(a)
print(b)

print()
# now we are rebinding a[0] instead of mutating the existing list object
a[0] = [100, 200]



# a[0].append(50)
#         ↓
# mutate shared inner object
#         ↓
# both see the change


# a[0] = [100, 200]
#         ↓
# rebind/replace a's reference
#         ↓
# b still points to the old inner object


print(a)
print(b)
print()
print(a, id(a))
print(b, id(b))
print()
print(a[0], a[1])
print(id(a[0]), id(a[1]))
print()
print(b[0], b[1])
print(id(b[0]), id(b[1]))

# An object is a value that exists at runtime, with its own identity, type, and state

# x = [10, 20] here x is a name bound to the object [10, 20]

# x ─────► [10, 20]
#              │
#              ├── identity
#              ├── type → list
#              └── state → [10, 20]

# Model

# Name ─────► Object
#               │
#               ├── identity
#               ├── type
#               └── state


# Deep copy
# copy.deepcopy()

# In Shallow copy 
a = [[10, 20], [30, 40]]
# creates a new list object b but shares the inner element list objects as same as a's inner list objects
b = a.copy()

# A deep copy goes one level further: it recursively copies the nested mutable objects too
# Python provides this through the copy module:

import copy

a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)

# Conceptually

# a ──► Outer A
#        │
#        ├──► Inner X [10, 20]
#        └──► Inner Y [30, 40]


# b ──► Outer B
#        │
#        ├──► Inner P [10, 20]
#        └──► Inner Q [30, 40]

# Nothing is shared between the corresponding mutable lists
print()
print(a is b)        # False
print(a[0] is b[0])  # False
print(a[1] is b[1])  # False

# Example for deep copy

a = [[10, 20], [30, 40]]
b = copy.deepcopy(a)

a[0].append(50)
print()
print(a)
print(b)
print()
print(a is b)          # False
print(a[0] is b[0])    # False
print(a[1] is b[1])    # False

# And importantly, mutating:
# a[0].append(50)
# has no effect on b, because a[0] and b[0] are different list objects


# Shallow vs deep copy
# You can now see the difference very clearly:

# SHALLOW COPY

# a ──► Outer A ──► Inner X
#                    ▲
# b ──► Outer B ─────┘

# versus:

# DEEP COPY

# a ──► Outer A ──► Inner X

# b ──► Outer B ──► Inner Y

# So:
# Shallow copy copies the outer object but preserves references to nested objects.
# Deep copy recursively creates copies of nested objects, so the copied structure is independent.

# One subtle point: "deep copy makes absolutely everything a completely new object" is not a rule. 
# Immutable objects such as integers may be reused because they cannot be mutated. The important guarantee 
# we're concerned with is independence of the mutable structure.

# Exercise

# import copy

a = [[10, 20], [30, 40]]

b = a.copy()
c = copy.deepcopy(a)

a[0].append(50)
b[1] = [100, 200]
c[0].append(60)
print()
print(a)
print(b)
print(c)
print()
print(a is b)
print(a[0] is b[0])
print(a[1] is b[1])
print(a[0] is c[0])

# Let's trace it.
# Initially:
# a = [[10, 20], [30, 40]]

# b = a.copy()
# c = copy.deepcopy(a)
# Structure:
# a ──► Outer A
#        ├──► Inner X [10,20]
#        └──► Inner Y [30,40]

# b ──► Outer B
#        ├──► Inner X [10,20]   ← shared with a
#        └──► Inner Y [30,40]   ← shared with a

# c ──► Outer C
#        ├──► Inner Z [10,20]   ← independent
#        └──► Inner W [30,40]   ← independent
# Then:
# a[0].append(50)
# a[0] and b[0] share Inner X, so both see the mutation:
# Inner X → [10,20,50]
# Then:
# b[1] = [100,200]
# This is rebinding/replacing the reference stored at position 1 of Outer B.
# It does not affect a[1].
# So:
# a → [[10,20,50], [30,40]]

# b → [[10,20,50], [100,200]]

# c → [[10,20], [30,40]]
# Then:
# c[0].append(60)
# Only c's independent Inner Z changes:
# c → [[10,20,60], [30,40]]
# Therefore the complete output is:
# [[10, 20, 50], [30, 40]]
# [[10, 20, 50], [100, 200]]
# [[10, 20, 60], [30, 40]]

# False
# True
# False
# False
# The last one:
# a[0] is c[0]
# is False because:
# a[0] ──► [10,20,50]

# c[0] ──► [10,20,60]
# They originated from the same values, but deep copy created a different inner list object for c.

# Day 31
# Names → Objects → References → Identity

# Day 32
# Objects → Mutable / Immutable
#        → Mutation vs Rebinding

# Day 33
# References to nested objects
#        → Shallow Copy
#        → Deep Copy