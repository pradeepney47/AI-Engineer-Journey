# Python Evaluation and Expression Behavior

# Expression evaluation and order
# Operator precedence and grouping
# Short-circuit evaluation
# Evaluation of function arguments
# Final tracing exercise

print()
x = 10
y = 20

x = x + y
print(x)


# Look up x → 10
# Look up y → 20
# Apply + → 30
# Bind/rebind x to the resulting object


# Evaluate RHS
#     ↓
#     10 + 20
#     ↓
#     30
#     ↓
# Bind x → 30

# This is also why the expression is perfectly valid even though x appears on both sides. 
# The old binding of x is used while evaluating the RHS, and only afterward is x rebound.



# Evaluation with operator precedence and grouping

result = 2 + 3 * 4
print()
print(result)

# 2 + 3 * 4
#     │
#     └── 3 * 4 = 12
#          │
#          ▼
#        2 + 12 = 14
# So:
# result = 14
# And your final step is also right: the resulting value is then bound to result.
# One important distinction
# Precedence determines grouping, not necessarily the physical sequence in which Python performs every operation.
# For example:
# 2 + 3 * 4
# is grouped as:
# 2 + (3 * 4)
# because * has higher precedence than +.
# Parentheses can explicitly change that:
# (2 + 3) * 4
# Now:
# 2 + 3 = 5
# 5 * 4 = 20
# So:
# 2 + 3 * 4  → 14
# (2 + 3) * 4 → 20

print()
result = 10 - 2 * 3 + 4
print(result)

# operators at the same precedence level are evaluated left-to-right for these arithmetic operators.
# Your grouping is:
# 10 - (2 * 3) + 4
#        ↓
# 10 - 6 + 4
#        ↓
# (10 - 6) + 4
#        ↓
# 4 + 4
#        ↓
# 8
# Therefore:
# result = 8
# One useful distinction
# There are three ideas here:
# 1. Precedence
# Determines which operators bind more tightly.
# * before + and -
# 2. Associativity
# When operators have the same precedence, determines grouping.
# 10 - 6 + 4
# ↓
# (10 - 6) + 4
# 3. Parentheses
# Explicitly determine grouping.
# 10 - (2 * 3 + 4)
# would produce a different result.
# So the mental model is:
# Precedence → grouping → evaluation → resulting object → binding.



# Short-circuit evaluation
# This is particularly important later when you're writing API, agent, and data-processing code

x = False
result = x and 10

# Python evaluates the left operand first:
# x
# ↓
# False
# For and, if the left side is falsy, Python already knows the whole logical result cannot be truthy, 
# so it short-circuits and does not evaluate the right side.
# Therefore:
# result ───► False
# But there is a subtle Python detail
# and and or don't necessarily return True or False. They return one of their operands.
# For example:
# result = 10 and 20
# Since 10 is truthy, Python evaluates and returns the second operand:
# result = 20
# And:
# result = 0 or 50
# 0 is falsy, so Python evaluates and returns:
# result = 50


# A and B
# │
# ├── A falsy  → return A
# └── A truthy → evaluate and return B

# A or B
# │
# ├── A truthy → return A
# └── A falsy  → evaluate and return B


# This is why short-circuiting is useful in real code, for example:

# user and user["name"]

# If user is None, Python doesn't attempt user["name"].

# Topic 3 checkpoint

a = 0 and 100
b = 25 and 100
c = 0 or 100
d = 25 or 100

# a = 0
# b = 100
# c = 100
# d = 25
# Your reasoning is now correct at the operand level, not just the Boolean level.
# The pattern
# For and:
# A and B

# A falsy  → A
# A truthy → B
# For or:
# A or B

# A truthy → A
# A falsy  → B
# And importantly, B is evaluated only when Python needs it.
# For example:
# result = False and some_function()
# some_function() is never called.

# This becomes very useful when working with APIs:
# user = get_user()

# name = user and user["name"]

# If get_user() returns None, Python stops at user and never attempts the dictionary access.




# Evaluation of function arguments

print()

def show(a, b):
    print(a, b)

show(10 + 5, 20 * 2)

# Conceptually:
# show(10 + 5, 20 * 2)
#         │       │
#         │       └── evaluate → 40
#         └────────── evaluate → 15
#                   ↓
#              call show(15, 40)
#                   ↓
#           bind a → 15
#           bind b → 40
#                   ↓
#              print(a, b)
# One important correction to your wording:
# a = 10 + 5, b = 20 * 2
# These aren't literally assignments occurring before the function call.
# Rather, Python evaluates the argument expressions first, obtains the resulting objects, 
# and then binds the parameter names during the function call:
# 10 + 5  → 15 ──► a
# 20 * 2  → 40 ──► b
# This connects directly to Day 34's parameter-binding model.

# Argument evaluation order
# Python evaluates function arguments left to right.
# For example:
# show(10 + 5, 20 * 2)
# conceptually:
# 1. evaluate 10 + 5 → 15
# 2. evaluate 20 * 2 → 40
# 3. call show(15, 40)
# 4. bind a → 15
# 5. bind b → 40
# 6. execute function body


# Example
print()
def first():
    print("first")
    return 10

def second():
    print("second")
    return 20

def show(a, b):
    print(a, b)

show(first(), second())

# Exact trace

# Python encounters:

# show(first(), second())

# It evaluates arguments left to right.

# 1. Evaluate first()
# first
# and it returns 10.

# 2. Evaluate second()
# second
# and it returns 20.


# 3. Call show(10, 20)

# Parameter binding:

# a ───► 10

# b ───► 20

# Then:
# print(a, b)

# prints:
# 10 20

# Why this matters

# Function calls have a very useful mental sequence:

# Evaluate arguments
#        ↓
# Obtain argument objects
#        ↓
# Bind parameters
#        ↓
# Execute function body
#        ↓
# Return result

# That sequence will become especially useful when we later trace nested function calls, 
# callbacks, API calls, and eventually agent/tool execution.



# Exercise

# Final Day 35 tracing challenge
# It will combine:
# evaluation order
# precedence
# short-circuiting
# function arguments
# mutation/rebinding

print()
numbers = [1, 2]

def add(items, value):
    items.append(value)
    return items

def calculate(x, y):
    return x * 2 + y

result = calculate(
    len(numbers),
    add(numbers, 10)[-1]
)

print(numbers)
print(result)


# Exactly correct. All six answers are correct. This is a good integration trace because 
# you handled evaluation order, mutation, indexing, parameter binding, and arithmetic together.
# Exact trace
# Initial state:
# numbers ───► [1, 2]
# Python evaluates the arguments to calculate() left to right.
# 1. First argument
# len(numbers)
# numbers refers to [1, 2].
# len([1, 2]) → 2
# So the first argument is 2.
# 2. Second argument
# add(numbers, 10)[-1]
# Call:
# add(numbers, 10)
# Parameter binding:
# items ────┐
#           ├──► [1, 2]
# numbers ──┘

# value ───► 10
# Then:
# items.append(value)
# mutates the shared list:
# numbers ───► [1, 2, 10]
# add() returns that same list.
# Then:
# [-1]
# gets the last element:
# [1, 2, 10][-1] → 10
# So the second argument is 10.
# 3. Call calculate
# We now effectively have:
# calculate(2, 10)
# Parameter binding:
# x ───► 2
# y ───► 10
# Then:
# x * 2 + y
# Precedence gives:
# (2 * 2) + 10
# 4 + 10
# 14
# So:
# result ───► 14
# Final state
# numbers ───► [1, 2, 10]
# result  ───► 14
# Therefore:
# [1, 2, 10]
# 14


# Your Day 35 mental model is:
# Python evaluates expressions according to grouping and evaluation rules, 
# produces objects as results, binds names to those results, and function calls evaluate arguments
# before binding parameters and executing the body.

# Python Operator Precedence


# Function calls absolutely are part of Python's expression precedence model. 
# I omitted them from the table, which was an important omission.
# In Python's official precedence table, function calls, subscriptions/indexing, 
# and attribute access are near the highest-precedence level, grouped with primary expressions.



# | Priority | Operator / Construct                         | Example           | Meaning                                          |
# | -------: | -------------------------------------------- | ----------------- | ------------------------------------------------ |
# |        1 | `()`                                         | `(2 + 3)`         | Parentheses / explicit grouping   
# |        2 |                                              |                   | Subscription / indexing
# |        2 |                                              |                   | Function call
# |        2 |                                              |                   | Attribute access
# |        2 | `**`                                         | `2 ** 3`          | Exponentiation                                   |
# |        3 | `+x`, `-x`, `~x`                             | `-5`              | Unary operators                                  |
# |        4 | `*`, `/`, `//`, `%`                          | `10 * 2`          | Multiplication, division, floor division, modulo |
# |        5 | `+`, `-`                                     | `10 - 3`          | Addition, subtraction                            |
# |        6 | `<<`, `>>`                                   | `x << 2`          | Bit shifts                                       |
# |        7 | `&`                                          | `a & b`           | Bitwise AND                                      |
# |        8 | `^`                                          | `a ^ b`           | Bitwise XOR                                      |
# |        9 | `\|`                                         | `a \| b`          | Bitwise OR                                       |
# |       10 | `<`, `<=`, `>`, `>=`, `==`, `!=`, `is`, `in` | `x == 10`         | Comparisons, identity, membership                |
# |       11 | `not`                                        | `not x`           | Logical NOT                                      |
# |       12 | `and`                                        | `x and y`         | Logical AND                                      |
# |       13 | `or`                                         | `x or y`          | Logical OR                                       |
# |       14 | `if ... else`                                | `x if ok else y`  | Conditional expression                           |
# |       15 | `lambda`                                     | `lambda x: x + 1` | Lambda expression                                |



# Primary expressions
#     ↓
# attribute access / indexing / function calls
#     ↓
# **
#     ↓
# unary operators
#     ↓
# arithmetic
#     ↓
# comparisons
#     ↓
# not
#     ↓
# and
#     ↓
# or

# For what we're doing right now, the most important subset is:
# ()
#  ↓
# **
#  ↓
# unary + / -
#  ↓
# * / // %
#  ↓
# + -
#  ↓
# comparisons
#  ↓
# not
#  ↓
# and
#  ↓
# or
# And remember:
# Precedence determines grouping. Associativity determines grouping when operators have the same precedence.
# For example:
# 10 - 2 * 3 + 4
# becomes:
# 10 - (2 * 3) + 4
#         ↓
# 10 - 6 + 4
#         ↓
# (10 - 6) + 4
#         ↓
# 8

# Useful version of Python Operator Precedence

# | Priority | Construct               | Example     |
# | -------: | ----------------------- | ----------- |
# |        1 | Parentheses / grouping  | `(a + b)`   |
# |        2 | Subscription / indexing | `items[0]`  |
# |        2 | Function call           | `func(x)`   |
# |        2 | Attribute access        | `obj.value` |
# |        3 | `**`                    | `2 ** 3`    |
# |        4 | Unary `+`, `-`, `~`     | `-x`        |
# |        5 | `*`, `/`, `//`, `%`     | `x * 2`     |
# |        6 | `+`, `-`                | `x + 2`     |
# |      ... | ...                     | ...         |
# |       12 | `not`                   | `not x`     |
# |       13 | `and`                   | `x and y`   |
# |       14 | `or`                    | `x or y`    |


# For example, in our Day 35 challenge:

# add(numbers, 10)[-1]

# Python needs to deal with:

# add(numbers, 10)    → function call
#         ↓
# returns [1, 2, 10]
#         ↓
# [-1]                → subscription/indexing
#         ↓
# 10

# And in:
# calculate(len(numbers), add(numbers, 10)[-1])
# you can see why these constructs are fundamental to expression evaluation.

# One nuance: parentheses have multiple roles. (a + b) is grouping, while func(a) is a function call. 

# They aren't the same precedence operation even though both use parentheses syntactically.
# So yes, your question caught a genuine omission in my table. For your Python mental model, remember 
# the top-level chain as:

# Primary expressions
#     ↓
# attribute access / indexing / function calls
#     ↓
# **
#     ↓
# unary operators
#     ↓
# arithmetic
#     ↓
# comparisons
#     ↓
# not
#     ↓
# and
#     ↓
# or
# For the complete authoritative table, the Python documentation is the right reference. 
# Python expression precedence documentation