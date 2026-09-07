# Bitwise operations
# Bitwise Operations is A & B, etc (&, |, ^, ~, <<, >>) that operates on binary values 

# bitwise AND &

a = 6
b = 3

print(a&b)

# bitwise OR |

print(6|3)

# bitwise XOR ^

# 1 ^ 1 → 0
# 1 ^ 0 → 1
# 0 ^ 1 → 1
# 0 ^ 0 → 0

print(6^3)

# bitwise NOT ~
# Python integers for ~ works different and the identity for NOT is 
# ~x = -(x + 1)

# ~ flips the bits, but because Python integers are signed,
# the result is not simply the positive binary complement
# ~x is always exactly one less than -x

print(~5) #prints -6

print(~0)#prints -1

# left shift operator <<
# x << n shifts the binary representation of x left by n positions, 
# filling the new positions with zeros

# 101 << 1 -> 1010 -> 10

print(5 << 1) # 101 << 1 -> 1010 -> 10
print(3 << 1) # 011 << 1 -> 0110 -> 6

# shift left by 2
print(5 << 2) # 101 << 2 -> 10100 -> 20

# right shift operator >>
# A right shift moves the bits to the right

# 10100 >> 1 = 20 >> 1 -> 01010 = 10
print(20 >> 1)

# 11000 >> 2 -> 24 >> 2 -> 00110 = 6
print(24 >> 2)

# Notice the pattern:
# 11000₂ = 24
# shift right 1 → 01100₂ = 12
# shift right 2 → 00110₂ = 6
# So for positive integers, >> 2 is equivalent to integer division by \(2^2=4\)

# 10101 >> 1 -> 01010 -> 10
print(21 >> 1)


# Why bitwise operations matter?
# Computers represent integers internally as bits (0 and 1)
# Bitwise operators let us manipulate those bits directly
# eg.,
# 5  = 0101
# 3  = 0011

# 5 & 3 = 0001 = 1
# 5 | 3 = 0111 = 7
# 5 ^ 3 = 0110 = 6

# A common practical use is bit flags: storing several True/False settings inside one integer

# READ    = 001
# WRITE   = 010
# EXECUTE = 100
# permissions = 101 (READ + EXECUTE)


# Logical operators (and, or, not) reason about truth values, 
# while bitwise operators (&, |, ^, ~) manipulate the individual bits of integers

