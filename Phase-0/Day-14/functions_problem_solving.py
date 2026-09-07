# Problem Solving using Functions

# Given a problem, how do I decide what should become a function?

# Part 1: A function should represent a meaningful task

# A function should generally compute/produce a result; 
# the caller decides what to do with that result

# Calculate the average of the numbers

def calculate_average(numbers):
    total = 0 #initialization of the state
    for number in numbers: #iteration over the iterable
        total += number #accumulation (change of the state)
    return total/len(numbers) #final computation and return value

numbers = [10, 25, 7, 18, 30]
# numbers = []

try:
    average = calculate_average(numbers)
except ZeroDivisionError: #edge case
    print()
    print("Denominator cannot be Zero")
else:
    print()
    print(average)

# Find the largest number

# Initialize with the first element → traverse the remaining elements → 
# compare each with the current largest → update when necessary → return largest

def largest_number(numbers):
    if numbers != []:
        # large_number = 0 #unsafe initialization considering if the list has negative numbers
        large_number = numbers[0] #safe initialization
        for number in numbers:
            if number > large_number: #selecting the largest by comparison
                large_number = number #storing the largest after full iteration
        return large_number #return the largest number
    else:
        raise ValueError

# numbers = [10, 25, 7, 18, 30]
numbers = []

try:
    result = largest_number(numbers)
except ValueError:
    print()
    print("List cannot be empty")
else:
    print()
    print(result)


# Pythonic way to find the largest number

def largest_number(numbers):
    if not numbers:
        raise ValueError
    
    large_number = numbers[0] #safe initialization

    for number in numbers:
        if number > large_number: #selecting the largest by comparison                
            large_number = number #storing the largest after full iteration

    return large_number #return the largest number
    
numbers = [10, 25, 7, 18, 30]
# numbers = []

try:
    result = largest_number(numbers)
except ValueError:
    print()
    print("List cannot be empty")
else:
    print()
    print(result)

# Finding the smallest number

def smallest_number(numbers):
    if numbers:
        small_number = numbers[0]
        for number in numbers:
            if number < small_number:
                small_number = number
        return small_number
    else:
        raise ValueError("List cannot be empty")

numbers = [10, 25, 7, 18, 30]
# numbers = []

try:
    result = smallest_number(numbers)
except ValueError as error:
    print()
    print(error)
else:
    print()
    print(result)

# Find the second largest number 

def second_largest_number(numbers):
    if len(numbers) > 1:
        large_number = numbers[0]
        second_large_number = numbers[1]

        # deciding the initial states of large_number and second_large_number

        if large_number < second_large_number:
            large_number, second_large_number = second_large_number, large_number

        # for number in numbers:
        # iterating from index 2 as there is no need to iterate numbers[0] and numbers[1]
        # as we decided or sorted in the initialization

        for number in numbers[2:]: 

            if number > large_number:
                second_large_number = large_number
                large_number = number

            elif number > second_large_number and number < large_number:
                second_large_number = number

            elif number == large_number or number <= second_large_number:
                continue #skip the current iteration and move to next item in the iterable

        return second_large_number
    else:
        raise ValueError("List must contain at least two numbers!")

numbers = [10, 25, 7, 18, 30, 12]
# numbers = [10]
# numbers = []

try:
    result = second_largest_number(numbers)
except ValueError as error:
    print()
    print(error)
    print()
else:
    print()
    print(result)


# Count Occurrences

def count_occurrences(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count += 1
    return count

numbers = [2, 5, 2, 8, 2, 5]
target = 2

result = count_occurrences(numbers, target)
print()
print(result)

# Count even numbers

def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count

numbers = [2, 5, 2, 8, 2, 5, 10, 7, 14]

result = count_even(numbers)

print()
print(result)

# Count greater than 15


def count_greater_than_15(numbers):
    count = 0
    for number in numbers:
        if number > 15:
            count += 1
    return count

numbers = [3, 8, 11, 14, 21, 26, 30]

result = count_greater_than_15(numbers)

print()
print(result)

# Count even number greater than 10

def count_even_greater_than_10(numbers):
    count = 0
    for number in numbers:
        if number > 10 and number % 2 == 0:
            count += 1
    return count

numbers = [3, 8, 11, 14, 21, 26, 30, 35]

result = count_even_greater_than_10(numbers)

print()
print(result)