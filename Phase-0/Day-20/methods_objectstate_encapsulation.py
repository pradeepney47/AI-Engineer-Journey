# Methods, Object State, and Encapsulation

# dog1.rename("Rocky")
#         ↓
# Dog.rename(dog1, "Rocky")
#         ↓
# self = dog1
# new_name = "Rocky"
#         ↓
# self.name = new_name
#         ↓
# dog1.name = "Rocky"

class Dog:
    def __init__(self, name):
        self.name = name

    def rename(self, new_name):
        self.name = new_name

dog1 = Dog("Bruno")

# method changes the object's state
# method rename changes the instance attribute name
dog1.rename("Rocky")

print()
print(dog1.name)

dog2 = Dog("Runo")
dog2.rename("Rooky")

print()
print(dog2.name)

# a method is also an attribute of the class
# So, rename is an attribute of the class Dog

# Dog
# │
# ├── name?      ← no class attribute called name
# │
# └── rename     → function object
#                  ↓
#                  def rename(self, new_name):
#                      self.name = new_name

# it gives the function object representing the rename method defined on the class
# It gives the rename function stored as an attribute of the Dog class.
print()
print(Dog.rename)

# Python retrieves the function from Dog and binds dog2 as self, 
# producing a bound method.
print()
print(dog2.rename)

# Three useful levels

# Dog.rename
#     ↓
# function object

# dog2.rename
#     ↓
# bound method
#     ↓
# self is already bound to dog1

# dog2.rename("Rocky")
#     ↓
# actually calls the method
#     ↓
# dog2.name becomes "Rocky"

# Concept:

# functions are first-class objects
# A method doesn't stop being a function object 
# just because it is defined inside a class. 
# The class stores it as an attribute.

print(Dog.rename(dog1, "BooBoo")) #prints None
print(dog1.name) #prints BooBoo

# dog1.rename("BooBoo")
#         ↓
# Python supplies dog1 as self

# Dog.rename(dog1, "BooBoo")
#         ↓
# you supply dog1 explicitly

# both are same
# dog1.rename("BooBoo") is same as Dog.rename(dog1, "BooBoo")

# dog1.rename("BooBoo") (this is the actual oop syntax so use this way)
# Dog.rename(dog1, "BooBoo") (this is just a conceptual understanding of what happens inside)

# Dog.rename
#     → function stored on the class

# dog1.rename
#     → bound method associated with dog1

# dog1.rename("BooBoo")
#     → method is actually executed

class Dog:
    species = "Canine"          # class attribute

    def __init__(self, name):   # class attribute → a function/method
        self.name = name        # instance attribute

    def bark(self):             # class attribute → a function/method
        print("Woof!")

# Dog
# │
# ├── species   → "Canine"       ← class attribute
# ├── __init__  → function       ← class attribute / method
# └── bark      → function       ← class attribute / method

# __init__ itself is an attribute of the class

# we can write this way as well
# Dog.__init__
# Dog.bark
# Dog.species
# Python retrieves those attributes from the Dog class

# self.name creates an attribute on the particular instance, not on the class

# Names assigned in the class body become entries in the class's namespace. 
# Methods such as __init__ are therefore attributes of the class. 
# Assignments through self create attributes on the instance.

# __init__ is a method, but it is also an attribute of the class whose value 
# is a function object.

# That's exactly why Dog.__init__ can be accessed like an attribute.

# self.x = ...       → instance attribute

class Dog:
    species = "Canine"       # class attribute

    def __init__(self, name):# class attribute → a function/method
        self.name = name     # instance attribute

    def bark(self):          # class attribute whose value is a function
        # local variables inside methods aren't class attributes
        sound = "bow bow"    # local variable, neither class nor instance attribute
        print("Woof!")

# self.something → instance attribute.
# Names defined directly in the class body → class attributes/methods.

# __init__ and bark are attributes of the class; their values are function objects.

# Dog
# │
# ├── __init__  → function object
# │
# ├── bark      → function object
# │
# └── ...

# Dog.bark
#    ↓
# function object

# dog1.bark
#    ↓
# bound method
#    ↓
# self = dog1

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Woof!")

dog1 = Dog("Hehe")
print()
print(dog1.bark)

# Dog.__init__
# Dog.bark
# Python's descriptor mechanism turns that function into a bound method, 
# with dog1 bound as self.

# __init__ works similarly as a function stored on the class, 
# although Python invokes it automatically during initialization.

# def __init__(...) and def bark(...) create function objects 
# that are stored under those names in the class namespace, 
# making them class attributes; when accessed through an instance, 
# they behave as bound methods.


# Object State
# Object state = the current values of its instance attributes

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

dog_1 = Dog("Puppy", 4)
print()
print(type(dog_1.birthday))
dog_1.birthday()
print()
print(dog_1)
print()
print(dog_1.name, dog_1.age)

# print()
# print(type(dog_1))
# print()
# print(type(Dog.__init__(dog1, "Puppy", 4)))
# print()
# print(type(dog1.name))
# print()
# print(type(Dog.birthday(dog_1)))
# print()

# Example

# Class
#  ↓
# defines attributes + methods
#  ↓
# creates separate instances
#  ↓
# each instance has its own state
#  ↓
# self identifies the current instance
#  ↓
# methods can read/change that instance's state

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

dog1 = Dog("Bruno", 5)
dog2 = Dog("Max", 7)

dog1.birthday()
dog1.birthday()
dog2.birthday()

print(dog1.age)
print(dog2.age)

# Encapsulation
# Keeping an object's state and the operations that manage that state together

# BankAccount
# │
# ├── balance       → state
# │
# └── deposit()     → behavior that changes the state

# Object = state + behavior that operates on that state

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(1000)
account_1 = BankAccount(505)
account.deposit(500)

print()
print(account.balance)

# encapsulation here is primarily about organizing and controlling access to state 
# through an object's interface, rather than making the state absolutely inaccessible

account.balance = -500
print(account.balance)
print(account_1.balance)

# Public vs Private vs Protected

# self.balance
#     → public attribute
#     → normal access is expected

# self._account_type
#     → "protected" by convention
#     → Python doesn't actually prevent access
#     → means: "this is intended for internal/subclass use"

# self.__pin
#     → name-mangled attribute
#     → Python changes its internal name
#     → provides stronger protection against accidental access

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self._account_type = "Savings"
        self.__pin = 1234

myaccount = BankAccount(6174)
print()
print(myaccount.balance) # prints
print(myaccount._account_type) # prints and _ is a programmer convention (not access control)

#python name mangles to discourage direct access to prevent accidental name collisions
# this is not true security
# __pin python may name mangle it as _BankAccount__pin
# print(myaccount.__pin) # AttributeError
print(myaccount._BankAccount__pin)

# name
#  ↓
# public
# "Use it normally."

# _age
#  ↓
# single underscore
# "Internal-use convention; but accessible."

# __secret
#  ↓
# double underscore
# "name-mangled to reduce accidental access/name collisions."


class Dog:
    def __init__(self):
        self.name = "Bruno"
        self._age = 5
        self.__secret = "🐾"

dog = Dog()
print()
print(dog.name)
print(dog._age)
# print(dog.__secret)
print(dog._Dog__secret)



