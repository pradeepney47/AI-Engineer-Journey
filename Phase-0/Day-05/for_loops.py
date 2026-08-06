# count even numbers

numbers = [3, 8, 12, 5, 10, 7, 20]

count_even = 0 # use of counter

for number in numbers:
    if number%2 == 0:
        count_even = count_even + 1

print(count_even)


# find the average

numbers = [10, 20, 30, 40]

total = 0 # use of accumulator

for number in numbers:
    total = total + number
average = total/len(numbers)

print(average)

# search name 

names = ["Alice", "Bob", "Charlie", "David"]

search_name = "Alice"
message_found = "The name " +search_name + " exists in the names list"
message_not_found = "The name " +search_name + " doesn't exist in the names list"

found = False # use of flag

for name in names:
    if name == search_name:
        found = True
        break

if found:
    print(message_found)
else:
    print(message_not_found)


# find the largest value

numbers = [3, 8, 12, 5, 10, 7, 20]

large_number = numbers[0] # use of tracker

for number in numbers:
    if number > large_number:
        large_number = number
print(large_number)

# find the smallest value

numbers = [3, 8, 12, 5, 10, 7, 20]

small_number = numbers[0] # use of tracker

for number in numbers:
    if number < small_number:
        small_number = number
print(small_number)

# find the highest score
# find the name of the student with the highest score
# find the average score
# find the number of students who scored 90 or above

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95),
    ("Eva", 88)
]

highest_score = students[0][1] # use of tracker
high_score_student = students[0][0] # use of tracker
total = 0 # use of accumulator
count_high_score = 0 # use of counter (scores 90 and above)

for student in students:
    total = total + student[1]
    if student[1] > highest_score:
        highest_score = student[1]
        high_score_student = student[0]
    if student[1] >= 90:
        count_high_score += 1
score_average = total/len(students)

print(highest_score)
print(high_score_student)
print(score_average)
print(count_high_score)