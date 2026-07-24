# integer -> whole number
# float -> decimel number
# string -> text
# bool -> True/ False values

# Python is dynamically typed language because 
# we do not explicitly mention the data type of 
# the variable. Python figures it out by itself.

# integer
x = 5 
# string
y = "10"
# print(x+y) this will throw error

# type conversion from string to integer
print(int(y))

# type conversion from integer to string
print(type(x))
x = str(x)
print(x, type(x))

name = "Pradeep"
age = 36
height = 170.5
is_learning = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_learning))

x = 10
y = 10.0
z = "10"
print()
print(type(x))
print(type(y))
print(type(z))

# 10 and 10.0 same?
# they are mathematically equal that is why it returns true
# but individually 10 is integer type and 10.0 is float type
print(10 == 10.0)

name = "Pradeep"
age = 28

# print(name + age) error because can only concatenate str (not "int") to str

name = "Pradeep"
age = 36

print(name + " " + str(age))
print(name, age)

name = "Pradeep"
age = 35

age = age + 1

print(name)
print(age)