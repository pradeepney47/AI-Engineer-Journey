# Python Collections: List, Tuple, Sets, Dictionary

# List - Ordered and Duplicate values allowed but mutable (indexing supported 
# because of positional relationship)

# Tuple - Fixed Ordered and Duplicate values allowed but immutable (indexing supported
# because of positional relationship)

# Set - Unorderd and Unique values only allowed (indexing not supported
# because it is about unique membership and not positional relationhip)

# Dictionary - Mapping keys to values

# tuple
# identical to list but the difference is tuple being immutable whereas list is mutable
# List is mutable (collection can be changed after it is created)
# Tuple is immutable (collection cannot be changed after it is created)
# List and Tuple are ordered collections


# list
numbers = [10, 20, 30]
numbers[0] = 100
print(numbers) # the result is [100, 20, 30]

# # tuple
# numbers = (10, 20, 30)
# numbers[0] = 100
# print(numbers) # TypeError

# Why tuple needed then?

# x = 10, y = 20 (representing a coordinate)
point = (10, 20) #this is a fixed group of value which is not intended to change

for value in point:
    print(value) # value can be read but cannot be modified

# Just like list, tuple can contain different data type values in it

person_1 = ["Pradeep", 36, "India"] #list
person_2 = ("Kumar", 26, "India") #tuple

for value in person_1:
    print(value)

for value in person_2:
    print(value)

# Tuple Unpacking (accessing the value in the Tuple in python)

# Instead of 
# person = ("Pradeep", 36, "India")
# name = person[0]
# age = person[1]
# country = person[2]
# print(name, age, country)

person = ("Pradeep", 36, "India")
# number of variables should match the number of values in the tuple
name, age, counntry = person # tuple unpacking


# Tuple Unpacking with variable
# Tuple object is immutable
# But the variable can be reassigned

point = (10, 20)
xx, yy = point
print (xx, yy)
xx = 50 # rebinding a variable
print(xx, yy) # prints (50, 20) because xx is a variable that refers to 50 instead of 10
print(type(xx))
print(point) #immutable so the point still is (10, 20)
print(type(point))

# Sets
# Set is primarily about uniqueness and not about order
# Unordered but uniqueness collection
# a set can contain only unique values inside the collection and repeated values
# A set represents a collection of unique values where membership matters more than position.
# A set is designed around membership and uniqueness, not positional indexing
visited = {"Chennai", "Tokyo", "Singapore"} # collection of unique values


numbers = {10, 20, 30}
numbers.add(40) # adds a value 40 to the set collection
numbers.add(20) # wont get added to the collection because it is a duplicate value
print(numbers)

# Membership test

print(20 in numbers) # returns boolean value
print(50 in numbers) # returns boolean value

# checking if Tokyo is a member in collection
if "Tokyo" in visited: 
    print("Already visited")

# remove operation
numbers.remove(30) # removes a value 30 from the set collection
print(numbers)
# numbers.remove(100) # key error (because the value does not exist in the set)
# print(numbers)

# discard operation
numbers.discard(100) # value is not in the set but it does not throw key error
print(numbers)

numbers = {10, 20, 30}

numbers.discard(20)
numbers.discard(50)

print(numbers)

# check and remove from the set collection
if 30 in numbers:
    numbers.remove(30)
print(numbers)

# union operation in set collection

a = {1, 2, 3}
b = {3, 4, 5}

c = a | b # set union (OR in boolean logic or every value unique from both set)
print(c) # the value 3 appears only once after union operation for set collection 

d = a.union(b)
print(d)

e = a & b # set intersection (AND in boolean logic or common values unique from both set)
print(e)

f = a.intersection(b)
print(f)

# Difference operation in set collection
# give me the set of values from one set that are not in the other set
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a - b
d = b - a
print(c, d)

# Subset opeartion in set collection

small = {2, 4}
large = {1, 2, 3, 4, 5}

print(small.issubset(large)) # returns boolean value
print(small <= large) # returns boolean value

# superset operation in set collection

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print(a.issuperset(b))
print(b.issuperset(a))

# Dictionaries
# It is collection type that asks what values are there in this key?
# Map key to value where key is used to look up the associated value
# Dictionary is not index -> value but key -> value
# Dictionaries are a poweful collection that is useful to represent structured information
# Dictionary collection is mutuable and the values can be read, inserted, updated, and deleted

person = {"name": "Pradeep", "age": 36, "country": "India"}

print(person["name"])
print(person["age"])
print(person["country"])
print()
# print(person["location"]) # keyError because location as a key does not exist in the person dictionary

# Three Dictionary patterns to remember

# One: To get key from the dictionary collection
# Python's default iteration is over the keys

for key in person:
    print(key) # prints the key of each item in the dictionary
print()

# Two: To get values from the dictionary collection

for key in person:
    print(person[key]) # prints the value of each item in the dictionary
print()

# Three: To get the key and value from the dictionary collection

for key in person:
    print(key, person[key])
print()

for key, value in person.items(): # unpacking key and value pairs
    print(key, value)


# object.method()/ object.attribute
# . essentially lets us access an attribute or method associated with an object.

# An object is essentially a value/entity that Python can work with and that has a type

x = 10 # 10 is an integer object
name = "Pradeep" # Pradeep is a string object
numbers = [10, 20, 30] # list object
print(type(numbers))
person = {"name": "Alice", "age": 25} # dicitionary object
point = (10, 20) # tuple object

# class
# A class is a blueprint/type from which objects can be created

# int, str, list, dict are all class
# 10, "Pradeep", [1, 2, 3], {"a": 10} are all object (instance of the class)

# . (after the . comes the attribute which is associated with an object)

list = [] # list is a class
print(type(list))
list = [10] # object or list object which is an instance of the class list
list.append(10) # append is a method or (special type of attribute) associated with the object

print(list)

print(numbers.count(20))

# Attributes doesnt not necessarily means function
name = "Pradeep"
# callable attributes
print(name.upper()) # method/ function which is a special type of attribute
print(name.lower()) # method/ function which is a special type of attribute
print(name.replace("pra", "Pra")) # method/ function which is a special type of attribute

# Attributes that are non-callable
print()
print(type(person)) # person is a dictionary object or an instance of class dictionary
print()
# person.name # can use custom attribute if the dict object had name attribute
# person.age # can use custom attribute if the dict object had age attribute

# In Python everything is an object even class objects too

class Persona:
    pass

per = Persona()

print(type(Persona))
print(type(per))

# What about modules?
# module can be treated as object too when imported
import math
print(math.sqrt(25))

print(type(math))
print()
print(person)

# Dictionary operations
# keys() operation

print(person.keys()) # returns view objects

# values() operation
print(person.values()) # returns view objects

print()

# keys() access key of the dictionary collection
for key in person.keys():
    print(key)
print()

# values() access value of the dictionary collection
for value in person.values():
    print(value)
print()

# items() for unpacking the key and value from dictionary collection
for key, value in person.items():
    print(key, value)
print()

# Iterating over list gives an element
# Iterating over tuple gives an element
# Iterating over set gives a unique element
# Iterating over dictionary gives key by default
# Iterating over dictionary gives key through .keys()
# Iterating over dictionary gives value through .values()
# Iterating over dictionary gives key-value pair through .items()

person = {
    "name": "Alice",
    "age": 26,
    "country": "India"
}

for key, value in person.items():
    print(key)
print()

for key, value in person.items():
    print(value)
print()

for key, value in person.items():
    print(key, value)
print()

# safe look up in Dictionary using get() without keyError
print(type(person))
# person["city"] #keyError is raised when key is absent in the dictionary
# Instead of stopping the flow of the program
# get() will safely look up if the value is present in the dictionary
# returns None if the key "city" is absent in the dictionary
print(person.get("city"))

person = {
    "name": "Alice",
    "age": 26,
    "country": "India"
}

print(person.get("name"))
print(person.get("city"))

# get(key, default_value)
# if key is in the dictionary then return that value else return default value provided next to it

# Imagine you're processing data from an API later in your AI engineering work
# You don't know whether every person has a "city" field
# Instead of city = person["city"] which causes KeyError we can write city = person.get("city", "Unknown")
# we can safely get city → "Unknown" if the field is missing

print()
print(person.get("city", "Unknown"))
print()
print(person.get("age"))
print()
print(person.get("cage"))

# removing key-value pairs
# dictionary has their own removal behaviour unlike set which has remove and discard

person = {
    "name": "Alice",
    "age": 26,
    "country": "India"
}

del person["age"] #deletes the key and the value of the dictionary person

print()
print(person)

# add value to the dictionary

person["age"] = 26
print()
print(person)

# del person["city"] #raises KeyError 
# print()
# print(person)

print(person)

# pop in dictionary

age = person.pop("age") #pops the key value from the dictionary and stores in the variable
print()
print(age)
print()
print(person)

person = {
    "name": "Alice",
    "age": 26,
    "country": "India"
}


#look up in dictionary
person["name"] 

#safe look up in dictionary
person.get("name") 

person.get("city")

person.get("city", "Unknown")

# Add / Update in dictionary

person["city"] = "Chennai" #adds new key

person["age"] = 27 #updates existing key

# Remove in dictionary

del person["age"] #removes the key-value pair

x = person.pop("country") #removes it from dictionary and returns India by storing the value in x
print()
print(x)

# Inspect in dictionary

print(person.keys())
print(person.values())
print(person.items())


# iteration in dictionary
print()
for key in person:
    print(key)
print()
for value in person.values():
    print(value)
print()
for key, value in person.items():
    print(key, value)


# Dictionary use as an AI Engineer

# list of dictionaries
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 32}
]

# Let us use function/loop/filter

def get_adults(people):
    adults = []
    for person in people:
        if person["age"] >= 18: #filter
            adults += [person] 
            # adults += person #['name', 'age', 'name', 'age']
    return adults

result = get_adults(people)
print()
print(result)


people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Charlie", "age": 32},
    {"name": "David", "age": 15}
]

for person in people:
    # {"name": "Alice", "age": 25}["age"] iteration 1
    # {"name": "Bob", "age": 17}["age"] iteration 2
    # {"name": "Charlie", "age": 32}["age"] iteration 3
    print(person["age"])


print()
result = get_adults(people)
print(result)

# filter and accumulate in dictionary

def get_adult_names(people):
    adult_names = []

    for person in people:
        if person["age"] >= 18:
            adult_names = adult_names + [person["name"]]

    return adult_names

result = get_adult_names(people)
print()
print(result)


# JSON and API's

users = {
    "alice": {
        "age": 25,
        "country": "India"
    },
    "bob": {
        "age": 30,
        "country": "Japan"
    }
}
print()
print(users["alice"])
print()

# data["key1"]
# data["key1"]["key2"]
# data["key1"]["key2"]["key3"]

print(users["alice"]["age"]) #Each [] is another lookup into the object returned by the previous lookup

# JSON data

# {
#     "user": {
#         "name": "Alice",
#         "profile": {
#             "country": "India"
#         }
#     }
# }

# data["user"]["profile"]["country"]


# Review about the filter, accumulator, counter, and transformer in typical code
numbers = [3, 8, 5, 12, 7, 20]
# print(numbers)
print()
result = [] #empty list
count = 0 #initial value

for number in numbers:
    if number % 2 == 0: #filter
        result = result + [number * 2] #transformer and accumulator
        count = count + 1 #counter
print(result)
print(count)
print()
# List Comprehension
# List:
# [ expression for item in iterable ]
# List Comprehension creates list of values
# [ TRANSFORMATION  for ITEM in INPUT  if CONDITION ]
# [ expression (transformation)   for variable in iterable (loop)  if condition (filter) ]
# [ expression for item in iterable ]
# [ expression for item in iterable if condition ]
# List comprehension = expression + loop + optional filter  → new list.

list_result = [number * 2 for number in numbers if number % 2 == 0] #list comprehension
print(list_result)
print()

# Expansion of the list comprehension code without using attributes

result_e1 = []
for number in numbers:
    if number % 2 == 0:
        result_e1 = result_e1 + [number * 2]
print(result_e1)
print()

# Expansion of the list comprehension code using attributes (append)

result_e2 = []
for number in numbers:
    if number % 2 == 0:
        result_e2.append(number * 2)
# print(result_e2.append(number*2)) # none
print(result_e2)
print()

numbers = [5, 12, 8, 15, 20, 3]

# List Comprehension with expression (transformation) and condition (filtering)
result = [number * 4 for number in numbers if number > 10]
print(result)
print()

# List Comprehension with expression (transformation) without condition (filtering)
result = [number * 4 for number in numbers]
print(result)
print()

# List Comprehension without expression (transformation) with condition (filtering)
# expression is just number or item that is it
result = [number for number in numbers if number > 10]
print(result)
print()

# Use Comprehension in the code when operation is simple and readable
# Use normal or expanded loop structure when the loop contains complicated branching, multiple steps, side effects, logging, error handling, etc

# List Comprehension (we can use our functions too)

# double the number function
def double(number):
    return number * 2

# even number check function
def is_even(number):
    return number % 2 == 0

result = [double(number) for number in numbers if is_even(number)]

print(result)
print()

# Normal code looks like
def get_doubled_number(numbers):
    double_number = []
    for number in numbers:
        if is_even(number):
            double_number = double_number + [double(number)]
    return double_number

result_n = get_doubled_number(numbers)
print(result_n)
print()

# Comprehension can replace the explicit loop + accumulation, 
# while a function can package and reuse the whole operation.
# And this distinction will become important when we later discuss 
# when to use functions vs comprehensions.



# Dictionary Comprehension creates a dictionary of key-value pairs
# Dictionary:
# { key_expression: value_expression for item in iterable }
# an empty dicitonary is defined as {}
# # Dictionary Comprehension expression with iteration and without condition
numbers = [2, 4, 6, 8]
result = {number: number * 10 for number in numbers}
print(result)
print()

# Dictionary Comprehension expression with iteration and condition
numbers = [2, 4, 6, 8]
result = {number: number * 10 for number in numbers if number > 4}
print(result)
print(type(result))
print()

# Dictionary Comprehension without expression with iteration and condition
numbers = [2, 4, 6, 8]
result = {number: number for number in numbers if number > 4}
print(result)
print()

# Set Comprehension
# Creates a set of values
# Set:
# { unique value expression for item in iterable }

# an empty set is defined as set()

# LIST COMPREHENSION
# [number * 2 for number in numbers]

# SET COMPREHENSION
# {number * 2 for number in numbers}

# DICTIONARY COMPREHENSION
# {number: number * 2 for number in numbers}

numbers = [1, 2, 2, 3, 3, 4]
result = {number * 2 for number in numbers}
print(result)
print(type(result))
print()

# There is no such thing as Tuple Comprehension
# We can use generator to convert a certain result to Tuple collection type

# Generator expression
# (number * 2 for number in numbers)

result = tuple(number * 2 for number in numbers)
print(type(result))
print(result)
print()

# Exercise

people = [
    {"name": "Alice", "age": 25, "country": "India"},
    {"name": "Bob", "age": 17, "country": "Japan"},
    {"name": "Charlie", "age": 32, "country": "India"},
    {"name": "David", "age": 15, "country": "USA"},
    {"name": "Eva", "age": 28, "country": "India"}
]

# Want a Dictionary containing only adults from India where 
# person name is the key and person age becomes the value

# Expected output

# {
#     "Alice": 25,
#     "Charlie": 32,
#     "Eva": 28
# }

# Dictionary Comprehension, List of Dicitonaries, Nested Dictionary Lookup, Filtering with if

result = {person["name"]: person["age"] for person in people if person["country"] == "India"}
print(result)
print(type(result))
print()

# Normal Dictionary code

print(people)
dict_person = {}
for person in people:
    if person["country"] == "India":
        dict_person[person["name"]] = person["age"]
print()
print(dict_person)
print(type(dict_person))
print()