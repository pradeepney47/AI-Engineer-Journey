# Instance and Class Attributes differences

# dog1.species
#     ↓
# Does dog1 itself have "species"?
#     ↓
# No
#     ↓
# Look at Dog's class attributes
#     ↓
# species = "Canine"
#     ↓
# Return "Canine"

# So the class attribute remains one attribute on the class, 
# while both instances can access it through normal attribute lookup


# Dog
# └── species = "Canine"       ← still unchanged

# dog1
# ├── name = "Bruno"
# └── species = "Wolf"         ← shadows Dog.species

# dog2
# └── name = "Max"
#                               ← no own species

# An instance attribute can shadow a class attribute with the same name
class Dog:
    species = "Canine" #species is a shared class level attribute

    def __init__(self, name):
        self.name = name #self.name is an instance attribute (changes as per instance)

dog1 = Dog("Bruno")
dog2 = Dog("Max")

print()
print(dog1.species) #prints Canine because species is a shared class level attribute
print(dog2.species) #prints Canine because species is a shared class level attribute


# dog1.species = "Wolf" do not modify the class attribute
# it just createa a new instance attribute on dog1 that shadows 
# the class attribute for that particular instance
dog1.species = "Wolf"

print()
print(dog1.species) #prints Wolf
print(dog2.species) #prints Canine
print(Dog.species) #prints Canine

# Dog("Max")
#    ↓
# new dog2 instance
#    ↓
# __init__(dog2, "Max")
#    ↓
# dog2.name = "Max"       ← initial state
#    ↓
# dog2.name = "BooBoo"    ← later state change (this does not affect any other instance)

# What happens if we change Dog.species itself after the instances already exist?
# neither dog1 nor dog2 has its own species attribute, 
# both instances fall back to the class Dog to look the species attribute their

# dog1.species
#     ↓
# dog1 has no species
#     ↓
# Dog.species
#     ↓
# "Wolf"

# dog2.species
#     ↓
# dog2 has no species
#     ↓
# Dog.species
#     ↓
# "Wolf"

class Dog:
    species = "Canine"

    def __init__(self, name):
        self.name = name

dog1 = Dog("Bruno")
dog2 = Dog("Max")

Dog.species = "Wolf" #changes the class attribute

print()
print(dog1.species) #prints Wolf
print(dog2.species) #prints Wolf
print(Dog.species) #prints Wolf

# Class and Instance attributes Mental Model

# Class attribute
#     ↓
# stored on the class
#     ↓
# shared through attribute lookup

# Instance attribute
#     ↓
# stored on a particular instance
#     ↓
# belongs only to that instance

# Same name?
#     ↓
# instance attribute shadows class attribute

# ------

# How they Look up

# instance.attribute
#       ↓
# check instance
#       ↓
# if not found → check class