# functions

# function defintion 
# parameter is number
def double(number):
    twice = number * 2
    print(twice)

# function call
# argument are 25 and 50
double(25)
double(50)

def text(num):
    print("Hello")

# text(4)
print("World")

def double(number):
    print(number * 2)

result = double(25)
print(result)

# return square of a number

def square(number):
    return number ** 2

result = square(4)
print(result)

# get the largest numbers greater than 10

def get_large_number(numbers):
    large_number = []
    for number in numbers:
        if number > 10:
            large_number = large_number + [number]
    return large_number

result = get_large_number([12, 5, 20, 8, 15, 3, 25])
print(result)

# return doesn't just give a value back
# It also controls the flow of execution by terminating the current function call.

# Once return executes, nothing below it in that function executes for that 
# particular call.

def classify(number):
    if number > 10:
        return "large"

    if number == 10:
        return "equal"

    return "small"

print(classify(15))
print(classify(10))
print(classify(7))

# return statement can be used as tracker as well but to return 
# the value once the desired one is found without using break statement

def find_first_even_number(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number

result = find_first_even_number([5, 7, 9, 12, 14, 20])
print(result)

# find the first largest number

def find_first_large(numbers):
    for number in numbers:
        if number > 10:
            return number
result = find_first_large([3, 7, 12, 20, 25])
print(result)

result = find_first_large([3, 7, 8, 9])
print(result)

# filter, transformer, and accumulator with function and return statements

def get_large_doubled(numbers):
    large_doubled_number = []
    # transform_number = []
    for number in numbers:
        # filter numbers (keep only numbers greater than 10)
        if number > 10:
            # transforming the number by multiplying the numbers greater than 10
            number = 2 * number
            # accumulate the transformed number to a list
            large_doubled_number = large_doubled_number + [number]
    # returning the accumulated value
    return large_doubled_number

result = get_large_doubled([12, 5, 20, 8, 15, 3, 25])
print(result)

# negative number tracker problem (greater than -10)

numbers = [-25, -8, -15, -30, -12, -5, -20]

largest_number = None
found = False

for number in numbers:
    if number < -10:
        if not found:
            largest_number = number
            found = True
        elif number > largest_number:
            largest_number = number

print(largest_number)
