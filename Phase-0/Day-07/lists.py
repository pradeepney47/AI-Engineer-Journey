# lists - collection data structure

# List Transformation

# Doubled using list concatenation
numbers = [10, 20, 30, 40, 50]

doubled = [] # empty list

for number in numbers:
    number = 2 * number
    doubled = doubled + [number] # accumulator

print (doubled)

# Dubled using preallocation and assign by index

doubled = [0] * (len(numbers)) # prefilling the list with 0 values

for i in range (len(numbers)):
    doubled[i] = 2 * numbers[i]
print(doubled)

# List Filtering

numbers = [3, 8, 12, 5, 10, 7, 20]

# filter the collection and generate a list that contains even number
filter_even = []
for number in numbers:
    if number % 2 == 0:
        # order of operands determines where the new value appears 
        # when the list is appended

        filter_even = filter_even + [number] # appends the number to the back
        # filter_even = [number] + filter_even # appends in the front

print(filter_even)

# Filtering and Transformation

# Filter the even numbers from the list, double them and generate a new list
# With two loops
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers = even_numbers + [number]

doubled_numbers = []

for number in even_numbers:
    number = 2 * number
    doubled_numbers = doubled_numbers + [number]


print(even_numbers)
print(doubled_numbers)

# Filter the even numbers from the list, double them and generate a new list
# In one loop

even_doubled = []

for number in numbers:
    if number % 2 == 0:
        even_doubled = even_doubled + [number * 2]
print(even_doubled)


# Modifying a collection (list) while iterating it
large_numbers = []
for number in numbers:
    if number > 10:
        large_numbers = large_numbers + [number]
print(large_numbers)

# Filtering, Transforming, Accumulating, and Tracking

numbers = [12, 5, 20, 8, 15, 3, 25]

large_doubled = []
find_large = 0

for number in numbers:
    if number > 10: # filtering 
        double_number = 2 * number # transforming
        large_doubled = large_doubled + [double_number] # accumulator
        # number > numbers[0] # not a correct tracker logic
        if number > find_large: # tracker
            find_large = number 
print()
print(large_doubled)
print(find_large)

# Find the largest number less than -10
# Solving it inefficiently with O(n**2) time and O(n) space complexities
# -25, -15, -30, -12, and -20 are lesser than -10
# Among these 5 items the largest is -12

numbers = [-25, -8, -15, -30, -12, -5, -20]

filter_number = []
largest_number = 0

for number in numbers:
    if number < -10:
        filter_number = filter_number + [number]
        for number in filter_number:
            if number >= -12:
                largest_number = number
print(largest_number)


# bad logic with logical and operator
largest_number = numbers[0]
less_number = -10
found = False

for number in numbers:
    if number > largest_number and number < less_number:
        largest_number = number
print(largest_number)


# efficient way

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