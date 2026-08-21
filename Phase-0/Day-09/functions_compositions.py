# multiplication

def multiply(a, b):
    return a * b

result = multiply(6, 7)
print(result)

# One function's returned value becomes another function's argument.
# functions within functions or composition

def add_five(number):
    return number + 5

def triple(number):
    return number * 3

result = triple(add_five(10))
print(result)

# Functions as reusable transformations

numbers = [2, 4, 6, 8]

def double(number):
    return number * 2

doubled_list = []
# loop controls iteration
for number in numbers:
    doubled_list = doubled_list + [double(number)] #function controls transformation
print(doubled_list)


# Return True if number is even and False if the number is odd
# function can also return boolean value

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(10))
print(is_even(7))

# Boolean-returning function can directly control another function or an if:
# if is_even(number):
#     print("Even")

# Is this number even function (centralized decision)
def is_even(number):
    return number % 2 == 0
print(is_even(10))
print(is_even(7))

# get even numbers (function within function)
# Which number in this collection are even
def get_even_numbers(numbers):
    even_list = []
    for number in numbers:
        # delegating to another function to make a decision
        if is_even(number):
            even_list = even_list + [number]
    return even_list

numbers = [5, 8, 12, 7, 15, 20]

result = get_even_numbers(numbers)

print(result)

# Function delegation for transformation
# Functions as reusable transformations

# double the number
def double(number):
    return number * 2
# accumulate the transformed values into a list
def get_doubled_numbers(numbers):
    doubled_list = []
    for number in numbers:
        # delegating to another function for transformation
        doubled_list = doubled_list + [double(number)]
    return doubled_list

numbers = [3, 5, 8, 10]
result = get_doubled_numbers(numbers)
print(result)

# Function delegation for Decision + Transformation + Accumulation
# [16, 24, 40]

# Filter 
def is_even(number):
    return number % 2 == 0

# Transformer 
def double(number):
    return number * 2

# Collection processing function which has two function calls with different jobs
def get_even_doubled(numbers):
    doubled_list = []
    for number in numbers:
        if is_even(number):
            # Accumulator
            doubled_list = doubled_list + [double(number)]
    return doubled_list

numbers = [3, 8, 5, 12, 7, 20]

result = get_even_doubled(numbers)

print(result)

# get large even doubled numbers
# [24, 40]

# Filter, Decision, Transformation, Accumulation

def get_large_even_doubled(numbers):
    large_even_doubled = []
    for number in numbers:
        # filter
        if number > 10:
            # decision delegation to another function
            if is_even(number):
                # accumulation
                large_even_doubled = large_even_doubled + [double(number)] # transformation delegation to another function
    return large_even_doubled

numbers = [12, 5, 20, 8, 15, 3, 25, 10]

result = get_large_even_doubled(numbers)

print(result)