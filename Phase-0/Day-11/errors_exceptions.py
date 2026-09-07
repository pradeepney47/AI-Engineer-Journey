# Errors, Exceptions and others

# Exception: When python executes the program something went wrong

numbers = [10, 20, 30]

# print(numbers[5]) #raises an IndexError as list index 5 is out of the range
# unless python program handles this abnormal event will stop the flow of the program
# as it is just not a false condition that it can skip but an abnormal event 
# that blocks execution of further lines of code
print("Hello")
print(numbers[1])
# print(numbers[5])

# How to handle this abnormality or exception?
try:
    print(numbers[2]) #executes
    print(numbers[5]) #delegates the exception to be handled by except block
    print(numbers[0]) #skips execution
except:
    print("Something went wrong") #executes

print("Done") #executes

# except captures broad errors

# What if we need specific errors to be captured?
# specific exception type capture (by explicitly mentioning the error type to except)
# IndexError
# KeyError
# TypeError
# ValueError
# ZeroDivisionError

try:
    print(numbers[0])
    print(numbers[10])
except IndexError:
    print("Invalid Index")

# try:
    # print(numbers[10])
    # print(numbers["1"]) #TypeError
# except IndexError:
    print("Invalid index")
print("Done")

# IndexError → wrong/nonexistent index position
# KeyError   → nonexistent dictionary key
# TypeError  → inappropriate type for the operation

# Multiple except blocks

# Try this → if something goes wrong, identify the exception type → 
# execute the first matching handler.


# try:
#     # code that might fail
# except SpecificError:
#     # handle that error
# except AnotherError:
#     # handle another error

data = [10, 20, 30]

try:
    print(data["1"])
except IndexError:
    print("Invalid Index")
except TypeError:
    print("Wrong Type")


person = {
    "name": "Alice",
    "age": 25
}

try:
    print(person["city"])
except IndexError:
    print("Invalid Index")
except KeyError:
    print("Invalid Key")
except TypeError:
    print("Wrong Type")

print("Done")

# try/except and else

# try:
#     # risky operation
# except SomeError:
#     # what to do if it fails
# else:
#     # what to do if it succeeds

try:
    print("Try")
except:
    print("Error")
else:
    print("Success") #else executes only if try block executes without any exception

numbers = [10, 20, 30]

try:
    print(numbers[1])
except IndexError:
    print("Invalid index")
else:
    print("Lookup successful")

print("Done")


person = {
    "name": "Alice",
    "age": 25
}

try:
    age = person["age"] # executes
except KeyError:
    print("Age is missing") #skips
else:
    print("Age:", age) #executes because try executed successfully


# finally
# finally runs whether an exception occurs or not
# try
#  │
#  ├── success ──→ else
#  │
#  └── exception → except
#                     │
#                     └────┐
#                          ↓
#                       finally
# finally is commonly used for cleanup, such as closing files or releasing resources


# try:
#     # attempt risky operation (attempts to execute)
# except SomeError:
#     # handle failure (executes if a matching exception occurs)
# except SomeOtherError:
#     #handle failure (executes if a matching exception occurs)
# else:
#     # successful try (executes if try block completes without exception)
# finally:
#     # always execute (almost always executes, regardless of success/failure)


numbers = [10, 20, 30]
print()
try:
    print(numbers[5])
except IndexError:
    print("Invalid index")
else:
    print("Lookup successful")
finally:
    print("Finished")
print()
# So far we dealt with natural exceptions that Python produces

# raise (raising exceptions ourself with raise)

def divide(a, b):
    # if b == 0:
        # manually raising an exception
        # raise ValueError("b cannot be zero") #deliberate error signalling
    # else:
    return a/b

# result = divide(2, 0)
# print(result)

result = divide(4, 5)
print(result)
print()

# Check age
# raise allows a function to signal that something is invalid, 
# while try/except allows the calling code to decide how to handle that situation
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

    return age

# # case 1
# result = check_age(-5) #exception raised but no handler to handle it so program stops

# case 2
try:
    result = check_age(-5) #exception raised and the handler can handle the exception
except ValueError:
    print("Invalid age") #exception is handled 
print()

# Raise different exception types

def set_age(age):
    # isinstance is a built-in method
    # returns True if the specified object is of the specified type, otherwise False
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    if age < 0:
        raise ValueError("Age cannot be negative")

    return age

# result = set_age("twenty") # TypeError
# print(result)
# result = set_age(-5) #ValueError
# print(result)
result = set_age(36)
print(result)
print()

# Catching ValueError
try:
    result = check_age(-5)
except ValueError:
    print("Invalid age")


# try:
#     ...
# except ValueError:
#     ...
# except TypeError:
#     ...
# except KeyError:
#     ...
# except IndexError:
#     ...

try:
    age = int("hello")
except ValueError as error: #actual exception object is captured
    print(error)


# except ValueError: # cathcing ValuError (catch/ handle the exception)
# raise ValueError("Age cannot be negative") # raising ValueError (create/ raise exception)

# raise ValueError
#        ↓
#    exception
#        ↓
# except ValueError
#        ↓
#     handle it


# Most errors in application code are these
# ValueError → Exception
# TypeError  → Exception
# KeyError   → Exception
# IndexError → Exception
print()
try:
    numbers[5] #IndexError is an Exception
except Exception:
    print("Something went wrong")

# Exception
#     │
#     └── IndexError

# order of except blocks matters
print()
try:
    numbers[5]
except Exception:
    print("General error") #this will execute because Exception is above in the order (class)
except IndexError:
    print("Index error") #this wont execute because it is in sub-order (sub-class)

# So, better approach is to place the specific error at the top
# Prefer specfic first then general because the first matching handler wins
# except IndexError:     ← specific
# except ValueError:     ← specific
# except Exception:      ← general fallback
print()
try:
    numbers[5]
except IndexError: # now this executes first 
    print("Index error")
except Exception:
    print("General error")
print()
# assert
# used when I expect this condition to be true at this point in the program
# commonly useful for catching programming mistakes during development

x = 10
assert x > 5
print("A") 
print()

y = 3
# assert y > 5 # False so further execution stops as AssertionError is raised
print("B")
print()

# Python automatically detects #handle exception
#         ↓
# IndexError / KeyError / TypeError / ValueError

# try:
#     ...
# except ValueError:
#     ...

# raise ValueError("Invalid value") #deliberately raise one

# assert value >= 0 #assert an assumption

# Exercise

# people = [{
#     "name": "Alice",
#     "age": 25
#     },
#     {
#     "name": "Bob",
#     },
#     {
#     "name": "Charlie",
#     "age": -5        
#     }]

# def get_age(person):

#     for key, value in person.items():
#         if key is False:
#             raise KeyError("Invalid Key")
#         elif int(value) < 0:
#             raise ValueError("Invalid Value")
#         else:
#             age = person["age"]
#             return age

# person1 = {"name": "Alice", "age": 25}
# person2 = {"name": "Bob"}
# person3 = {"name": "Charlie", "age": -5}

# try:
#     result = get_age(person1)
#     result = get_age(person2)
#     result = get_age(person3)
# except KeyError:
#     print("Age is missing")
# except ValueError:
#     print("Age cannot be negative")
# else:
#     print("Age is ", result)
# finally:
#     print("Done")

# print()


def get_age(person):
    try:
        age = person["age"]

        if age < 0:
            raise ValueError("Age cannot be negative")

        return age

    except KeyError:
        print("Age is missing")


person1 = {"name": "Alice", "age": 25}
person2 = {"name": "Bob"}
person3 = {"name": "Charlie", "age": -5}


try:
    result = get_age(person1)
except ValueError:
    print("Age cannot be negative")
else:
    print("Age is", result)

try:
    result = get_age(person2)
except ValueError:
    print("Age cannot be negative")
else:
    print("Age is", result)

try:
    result = get_age(person3)
except ValueError:
    print("Age cannot be negative")
else:
    print("Age is", result)

finally:
    print("Done")


