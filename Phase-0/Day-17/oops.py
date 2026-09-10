# Object Oriented Programming

# class - blueprint
# object - something that is built out of that blueprint

# Class describes what "something" (eg.,) Student is supposed to have

# Creates a class called Student
# Student is a class object

# Class object (defines what a Student instance is)
# Student is an instance of class type
class Student:
    pass

# Two separate objects student_1 and student_2 created out of the same class Student
# a new object that is referenced to a class

# instance object
student_1 = Student() #student_1 is an object of class Student (a class object)

# instance object
student_2 = Student() #student_2 is an object of class Student (a class object)

print()
print(type(Student)) #class type

# type
#  ↑
#  │
# Student          ← class object
#  ↑
#  │
# student_1         ← instance
# student_2         ← instance

def student():
    pass

print()
print(type(student)) #class function

# Attributes (two types - class attribute and instance attribute)
# Where does that data actually live — in the class or in the individual object?

# Dog (class)
# │
# ├── dog1 (instance)
# │     └── name → "Max"
# │
# └── dog2 (instance)
#       └── name → "Payne"

class Dog:
    pass

dog1 = Dog()
dog2 = Dog()

# same attributes of the same class can have differenct values
# attribute here is name for the class Dog
# name is an instance attribute because we assigned it through instance of the class object

# instance attribute
dog1.name = "Max"
dog2.name = "Payne"

# class attribute
# can be shared and accessed by its instance objects
class Dog:
    species = "Canine" #class attribute

# self and __init__

# self
# self is not a special keyword in Python
# It's the conventional parameter name

class Dog:
    # self refers to the particular object that called the method
    def bark(self):
        print("woof")

dog1 = Dog()
dog2 = Dog()

# how does Python know that this particular call is associated with dog1
# Conceptually Python sees Dog.bark(dog1) because self refers to the particular object that called the method

# dog1.bark()
#       ↓
# Dog.bark(dog1)
#       ↓
# self → dog1

dog1.bark()

# how does Python know that this particular call is associated with dog2
# Conceptually Python sees Dog.bark(dog2) because self refers to the particular object that called the method

# dog2.bark()
#       ↓
# Dog.bark(dog2)
#       ↓
# self → dog2

dog2.bark()

print()

class Cat:
    # This method expects the instance on which it is being called
    def meow(self):
        print(self)

cat1 = Cat()
cat2 = Cat()

cat1.meow()
cat2.meow()

# Why self is useful?
# self lets the method modify the particular object's state

# Connecting self to object state (remember self is just a convention we can use any word)

# Dog
# │
# │  class
# │
# ├── dog1  → instance of Dog
# │     └── name = "Max"
# │
# └── dog2  → instance of Dog
#       └── name = "Payne"

# self is simply the method's reference to whichever instance is currently calling the method

class Dog:
    def set_name(self, name):
        self.name = name #instance attribute
        self.species = "Canine" #instance attribute

dog1 = Dog()
dog2 = Dog()

dog1.set_name("Max") #instance attribute
dog2.set_name("Payne") #instance attribute

# dog1.nature = "soft" #instance attribute

print()
print(dog1.name) 
print(dog2.name)
print()
print(dog1.species)
print(dog2.species)
print()
# print(dog1.nature)

# Why Python gives us __init__ so we don't have to create attributes manually 
# with separate set_name() calls?

# Python gives us a cleaner way to initialize an object's attributes when the object is created

# __init__

# Conceptually we can see __init__

# Dog.__init__(dog1, "Bruno", 5)
            #  ↑
            #  self

class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Bruno")

print()
print(dog1.name)

# another example

# self.name = name means take the value received through the name parameter 
# and store it in the name attribute of the current instance

class Game:
    def __init__(self, name, age):
        self.name = name
        self.age = age

player1 = Game("Max", 33) #instance 1

player2 = Game("Payne", 30) #instance 2

print()
print(player1.name, player1.age)
print()
print(player2.name, player2.age)

# Exercise
# Each instance has independent state
# why does __init__ look like a function call?
# Dog("Bruno", 5) is a class call.
# We are not explicitly writing __init__(dog1, "Bruno", 5)

# Python's object-creation machinery handles that process for you

# dog1 = Dog("Bruno", 5)
#           ↓
#      create instance
#           ↓
#      initialize instance
#           ↓
#  __init__(dog1, "Bruno", 5)
#           ↓
#  self → dog1


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Bruno", 5) #class call
dog2 = Dog("Max", 3) #class call

dog1.age = 6 #instance attribute age for dog1

print()
print(dog1.age) #prints 6 and not 5
print(dog2.age) #prints 3