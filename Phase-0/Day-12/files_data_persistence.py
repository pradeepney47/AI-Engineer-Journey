# Files and Data Persistence
# data that can survive after the program ends
# Python program -> write data -> file.txt -> program ends -> data still exists

# 1 Opening a file
# open is a python built-in method
# r is read mode

# manual way of reading the file
file = open("data.txt", "r")
content = file.read()
print(type(file))
print(content)
print(type(content))
file.close()
print()

# automatic way reading the file using "with"
# with -> open resource -> use resource -> leave block -> automatically clean up
# file is an object representing an open connection/interface to the file

with open("data.txt", "r") as file: #handles the closing of file automatically
    content = file.read() #returns string
print(type(file)) #type of file is class
print(content)
print(type(content))
print()
# FUNCTION
# open()
#   │
#   │ returns
#   ▼
# OBJECT
# file object
#   │
#   ├── read()       ← method
#   ├── readline()   ← method
#   ├── close()      ← method
#   └── ...

# xyz.read()

# xyz
#  ↓
# file object
#  ↓
# read() method
#  ↓
# execute reading
#  ↓
# return string

# open()                 → function
#    ↓
# creates/obtains       → file object
#    ↓
# file object belongs to → a file-related class/type
#    ↓
# xyz                    → reference to that object


# CLASS / TYPE
#      │
#      │ defines behavior
#      ▼
# OBJECT / INSTANCE
#      │
#      ├── methods
#      ├── attributes/state
#      └── data

# ---

# FUNCTION
#      │
#      │ can create/return
#      ▼
# OBJECT
# A function can return an object, but that does not make the object an instance of the function

# dict object
#    │
#    ├── get()
#    ├── keys()
#    ├── values()
#    └── items()

# file object
#    │
#    ├── read()
#    ├── readline()
#    ├── write()
#    └── close()

#  readline()
# only reads one line per call
# so each call advances the file position by one line

with open("data.txt", "r") as file:
    line1 = file.readline() #"Alice\n" this is what is read from data.txt line 1
    line2 = file.readline()
    line3 = file.readline()
    line4 = file.readline()

print(line1) #print adds another new line apart from "Alice\n"
print(line2.strip()) #strips empty spaces around string
print(line3, end="") #ensures not to print a new line
print("\n") #prints new line
print(line4)
# print(repr(line4))
# print(line5)

# readlines()
# returns the text read as a list of strings

with open ("data.txt", "r") as file:
    lines = file.readlines()
print(type(lines))
print(lines)
print()

# file object is also iterable just like for loop works in list as list is iterable
# no need for readlines()

with open("data.txt", "r") as file:
    for line in file:
        print(line, end="")

# what happens during a for loop depends on what kind of object we are iterating over

# list  ends up with elements
# tuple ends up with elements
# set   ends up with elements
# dict  ends up with keys
# file  ends up with lines

# open → read → readline → readlines → iterate

# open -> append

file = open("data.txt", "a")
file.write("\nHi! I am learning to write.")
file.close()

# Rewriting existing content
# "w" mode rewrites the entire file

with open("data.txt", "w") as file:
    file.write("Hi, I am learning Python\n")


# Append (update the file and does not rewrite the file entirely)
# "a" writing in append mode
with open("data.txt", "a") as file:
    file.write("\nHello!")
    file.write("\nIt's me.")
    file.write("\nBye!")

# writelines()
# accepts iterable of strings 
# writeline() does not add \n so we explicitly give it
# also in write new .txt file is created if already does not exist
names = ["Alice\n", "Bob\n", "Charlie\n", "David\n"]
artists = ["MJ\n", "Enrique\n", "Taeyeon\n", "Katseye\n"]

with open("data.txt", "w") as file:
    file.writelines(names)

with open("test.txt", "w") as file:
    file.writelines(artists)

# tell() and seek()

# tell() - gives the current position of the file cursor
print()
with open("data.txt", "r") as file:
    print(file.tell()) # gives the cursor position in a specific line
    print(file.readline())
    # print(file.readline())
    print(file.tell())

# seek()
# moves the cursor (changes the current position)
print()
with open("data.txt", "r") as file:
    print(type(file))
    print(file.readline()) #reads the line and moves the cursor forward
    print(file.seek(7)) #moves the cursor backward or forward depending on the position value
    print(file.tell()) #tells where the cursor position is now
    print(file.readline()) #prints that line
    print(file.tell()) #tells where the cursor position is now
    print("Done")
    #repr shows the entire character in the line (returns internal state of the object as it is)
    print(repr(file.readline())) 

# readline()
#     ↓
# cursor moves forward

# tell()
#     ↓
# ask where cursor currently is

# seek()
#     ↓
# move cursor somewhere else



# Practical File Processing
# Process the txt file into a list of dictionary 

# [{"name": "Alice", "age": 25}, 
# {"name": "Bob", "age": 30}, 
# {"name": "Charlie", "age": 26}, 
# {"name": "David", "age": 29}]
print()
people = []
with open("group.txt", "r") as file:
    # print(file.readline())
    # people = []
    for line in file:
        name, age = line.split(",")
        # print(type(name), type(age))
        # print(line)
        age = int(age)
        person = {"name": name, "age": age}
        # print(person)
        people.append(person)
        # print(people)
print(people)

# Handling FileNotFoundError
# Remember IndexError KeyError ValueError TypeError
# try     → attempt
# except  → if specified exception occurs
# else    → if try succeeds
# finally → regardless

# Files have FileNotFoundError
print()
try:
    # with open("group.txt", "r") as file:
    #     data = file.read()
    with open("students.txt", "r") as file:
            data = file.read()
except FileNotFoundError:
    print()
    print("File not found in the specified path")
else:
    print()
    print("File read successfully")
    print()
    print(data)
finally:
    print()
    print("File Handled")
print()


# Exercise
people = []
try:
    with open("people.txt", "r") as file:
        # data = file.read()
        # print(type(file), type(data))
        for line in file:
            # print(line, type(line), type(file))
            line = line.strip()
            name, age = line.split(",")
            age = int(age)
            person = {"name": name, "age": age}
            people.append(person)
except FileNotFoundError:
    print()
    print("File not found in the specified path")
else:
    print()
    print("File read successfully!")
    # print(data)
    # for line in file:
    #     print(line)
    print()
    print(people)
    print()
finally:
    print("File handling done!")
print()