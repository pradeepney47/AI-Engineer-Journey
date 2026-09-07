# Boolean Logic

# AND OR NOT

# AND
age = 16
has_id = True

if age >= 18 and has_id:
    print("Allowed")
else:
    print("Not allowed")


# short-circuit evaluation
# AND short circuits when first value is Falsy

# 10 and 20   # 20
# 0 and 20    # 0

def square_number(number):
    return number ** 2

age = 16

if age >= 18 and square_number(4): #short-circuit evaluation
    # False and anything is False so evaluation stops there itself
    print()
    print("Allowed")

# and doesn't necessarily return True or False
# and returns one of its operands

# 10 is truthy so Python evaluates second operand and returns 20
result = 10 and 20
print(result) #returns operand and not boolean

# 0 is falsy so Python stops evaluation and returns 0
result = 0 and 20
print(result) #returns operand and not boolean

# OR

# A or B is True when at least one of A or B is True

# 10 or 20    # 10
# 0 or 20     # 20

age = 16
has_parent = True
print(type(has_parent))
if age >= 18 or has_parent:
    print("Allowed")
else:
    print("Not allowed")

# Short-circuiting with OR
# OR short circuits when first value is Truthy
x = True
print(type(x))
result = x or (10 / 0)

print(type(result)) #returns operand and not boolean
print()
print(result)
print()


# NOT
# returns boolean always

not 10       # False
not 0        # True
not "hello"  # False
not ""       # True
not []       # True
not [1, 2]   # False
not True # returns False
not False # returns True

print(not True)
print(not False)

x = 10
result = not x

print(result)

# and → stops at the first falsy value
# or  → stops at the first truthy value
# not → reverses truthiness and returns True/False

# Predict the output

age = 16
has_id = True

result = not (age >= 18 and has_id)
print(result)

# and → both must be truthy
# or  → at least one must be truthy
# not → reverses truthiness

# and / or → short-circuit and return operands
# not      → evaluates truthiness and returns True/False

x = 10
y = 0

result = x > 5 and y > 0 or x == 10

print(result)

# Boolean precedence is NOT AND OR

# A and B or C -> (A and B) or C

result = True or False and False
print(result)

# Truth Table

# AND
# and is True only when both inputs are True

# TRUE AND TRUE = TRUE
# TRUE AND FALSE = FALSE
# FALSE AND TRUE = FALSE
# FALSE AND FALSE = FALSE

# OR
# or is False only when both inputs are False

# TRUE OR TRUE = TRUE
# TRUE OR FALSE = TRUE
# FALSE OR TRUE = TRUE
# FALSE OR FALSE = FALSE

# AND → True only when both are True
# OR  → True when at least one is True
# NOT → reverses True ↔ False

# NOT

# False   True
# True    False

A = True
B = False
C = True

result = A and (B or C)
print(result)

print(result)

A = True
B = False
C = True

result = (A and B) or (not C)
print(result)

# Boolean Logic is A and B, A or B, not A, etc
# Bitwise Operations is A & B, etc (&, |, ^, ~, <<, >>) that operates on binary values 