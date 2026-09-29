# Tracing Challenge
# Python mental-model/tracing

# Part 1: Names, objects, and identity
# Part 2: Mutation, rebinding, and copying
# Part 3: Function arguments
# Part 4: Scope and LEGB
# Part 5: Final integrated challenge


# Part 1: Names, Objects & Identity

print()
a = [10, 20]
b = a
# shallow copy
c = a.copy()

a.append(30)
b = [40, 50]

print(a) # [10, 20, 30]
print(b) # [40, 50]
print(c) # [10, 20]
print(a is c) # False
print(a[0] is c[0]) # True
print(a[0] == c[0]) # True
print(a[1] is c[1]) # True



# Part 2: Mutation, rebinding, and nested objects
print()
x = [[1, 2], [3, 4]]
# shallow copy
y = x.copy()

x[0].append(5)
x[1] = [100, 200]

print(x) # [[1, 2, 5], [100, 200]]
print(y) # [[1, 2, 5], [3, 4]]




# Part 3: Function arguments
print()
def modify(data):
    data[0].append(99)
    data = [[100]]
    return data

numbers = [[1, 2], [3, 4]]

result = modify(numbers)

print(numbers) # [[1, 2, 99], [3, 4]]
print(result) # [[100]]


# Part 4: Scope and LEGB

print()
value = 10 # global name

def outer():
    value = 20 # local name for outer()

    def inner():
        value = 30 # local name for inner()
        print(value) # prints 30 first

    inner()
    print(value) # prints 20 second

outer()
print(value) # prints 10 third




# Part 5: Final integrated challenge

print()
value = 10 # global name

def process(data):
    value = 20 # local name within process(data) and since value is nonlocal the mutated object is 25 and then 30

    def modify():
        # nonlocal name so, value is 20 initially but later it has become 25
        nonlocal value
        # += an in place operation and value binds to the object 25
        value += 5 # += an in place operation and value binds to the object 30 
        # append an in place operation so list element is mutable within the mutable list object data
        # data and numbers become [[1, 25], [2]]
        # data and numbers become [[1, 25, 30], [2]] and [[1, 25, 30], [100]] respectively
        # shallow copy so the data[0] shares the same mutable list object to the first element even though the
        # outer list of data is independent
        data[0].append(value) 
    modify() # at this point data and numbers become [[1, 25], [2]] and value is 25 (it is nonlocal name)

    data = data.copy() # data is now an independent mutable list object [[1, 25], [2]]
    data[1] = [100] # data now becomes [[1, 25], [100]]

    # at this point data = [[1, 25], [100]], numbers = [[1, 25], [2]], and value = 25 (nonlocal name)

    modify() # at this point data = [[1, 25, 30], [100]], numbers = [[1, 25, 30], [2]], and value = 30 (nonlocal name)
    
    # at this point numbers = [[1, 25], [2]]
    return data, value # data = [[1, 25, 30], [100]], value = 30


numbers = [[1], [2]]

result = process(numbers)

print(numbers) # numbers = [[1, 25, 30], [2]]
print(result, id(result)) # result = ([[1, 25, 30], [100]], 30)
print(value) # value = 10 (global name)
print(result[0], id(result[0]), id(result[0][0]), id(result[0][1]),
      result[1], id(result[1]))





# What object does data initially refer to?

# data initially refers to the object [[1], [2]] which share the same with the numbers
# data binds with the object during process(numbers) function call 

# What happens to numbers after the first modify()?
# After the first modify the numbers become [[1, 25], [2]]
# It does not share an object between modify and process in the same sense as data and numbers. nonlocal means:
# Don't create a new local value in modify; access and rebind the value belonging to the enclosing process scope.


# What happens when data = data.copy()?
# It creates a new independent mutable list object which data rebinds with

# What does nonlocal value mean when modify() is called the second time?
# nonlocal value means 25 while calling modify() the second time as during the first call the nonlocal shares
# the value not only within the scope of modify() but also within the scope of process(data) too. Therefore, the value
# is 25 which can be accessed from process(data) and modify() as the object shares across both these functions
# there is also rebinding even after the second time so, finally the rebounded object that refers to the value that
# can be accessed from modify() and process(data) is 30



# numbers = [[1, 25], [2]]
# result = ([[1, 25, 30], [100]], 30)
# value = 10

# Phase 1 mental model:

# Names
#   ↓
# Objects
#   ↓
# References / binding
#   ↓
# Identity
#   ↓
# Mutable vs immutable
#   ↓
# Mutation vs rebinding
#   ↓
# Shallow vs deep copy
#   ↓
# Function argument binding
#   ↓
# Scope / LEGB
#   ↓
# nonlocal / global
#   ↓
# Expression evaluation