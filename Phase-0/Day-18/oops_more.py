# Object Oriented Programming 

# __init__ initializes the initial state of a newly created instance, 
# usually by assigning initial values to its instance attributes

# self refers to the specific instance that the method is operating on
# inside __init__, self is the actual instance object
# self is literally a reference to that object during that method call
# self is the local parameter name through which a method accesses the current instance

class Dog:
    def __init__(self, name, age):
        print(self)
        self.name = name
        self.age = age

dog_1 = Dog("Doody", 3)
dog_2 = Dog("Sweety", 2)

dog_1.name = "Riri"

print()
print(dog_1)
print(dog_2)

print()
print(dog_1.name, dog_1.age)
print(dog_2.name, dog_2.age)


# Class Attribute vs Instance Attribute
# self identifies which instance receives the initialized/modified state

class Dog:
    species = "Canine"     # class attribute

    def __init__(self, name):
        self.name = name   # instance attribute

dog_3 = Dog("Susi")

print()

print(Dog.species) #class attribute
print(Dog.__init__(dog_1, "Susi"))
print(dog_3.name) #instance attribute