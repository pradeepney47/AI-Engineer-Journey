# Modules Imports Packages

# Python file is a module
# we split our code into separate files and let them work together

# project/
# ├── main.py
# └── calculator.py

# calc.py
#      ↓
#    module
#      ↓
#  imported by
#      ↓
# main.py

#Python makes the imported module available under the name
import calc 

# import calc
#         ↓
# calc.add()

# from calc import add
#         ↓
# add()

#We can also import specific things
from calc import add

#Look inside the calc module and retrieve the add function and calls that function
# . is accessing something associated with an object/module
# accessing the add attribute from the module object calc
result = calc.add(4,5) 

# add is directly available in this current module
result_spec = add(23, 45)

print(result, result_spec)

# Mental model so far

# Python project
# │
# ├── main.py (can use that functionality without needing to redefine it)
# │
# └── calculator.py (organizes related functionality)
#         │
#         ├── add()
#         ├── subtract()
#         └── multiply()

# example scenario that is important for an AI Engineer

# ai_engineer_project/
# │
# ├── main.py
# ├── config.py
# ├── models.py
# │
# ├── api/
# │   └── client.py
# │
# ├── services/
# │   └── ...
# │
# └── tests/
#     └── ...

# Importing math tools

import math_tools #math_tools is a module object

multiply_two = math_tools.double(6)
print(multiply_two)

from math_tools import add


# from math_tools import add doesn't mean we copied the function's source code into main.py.
# Conceptually, Python gives the current module a name add that refers to the 
# function object defined in math_tools.

# math_tools module
#       │
#       └── add ─────────┐
#                        ↓
#                  function object
#                        ↑
#                        │
# main module             │
#       │                 │
#       └── add ──────────┘


# module object
#       ↓
#    . attribute
#       ↓
#    function
#       ↓
#     call()

sum = add(3, 4)

print(sum)

# main.py
#    │
#    │ import
#    ↓
# math_tools module
#    │
#    ├── add → function
#    └── double → function

# Compare Module object with OOP concept

# In OOP
# phone.battery.charge()
# │      │       │
# │      │       └── method
# │      └── Battery instance
# └── Phone instance

# In Module
# math_tools.add()
# │          │
# │          └── function defined in module
# └── module object

# This distinction—function vs method—is worth keeping. 
# A function becomes a bound instance method when accessed through an instance 
# in the appropriate class/descriptor context; a module-level function like 
# math_tools.add isn't an instance method.

# Packages

# Packages organize related modules into directories.
# Example: api/client.py


# project/
# ├── main.py
# │
# └── api/
#     ├── client.py
#     └── parser.py

# Here api is a package, containing modules such as client.py and parser.py.

# from api.client import get_data

# api # is a package
#  ↓
# client # it is a module
#  ↓
# greet

# from package.module import function

from api.client import greet
result = greet()

# uppercase in this module is a name that refers to the function defined in client.py
from api.client import uppercase

# Day22/
# │
# ├── modules_imports_packages.py
# │
# └── api/              ← package
#     │
#     └── client.py         ← module
#           │
#           └── uppercase()  ← function


result = uppercase("pradeep")
print(result)

# example

# AI-Engineer-Journey/                           ← parent directory
# │
# ├── Phase-0/                                   ← directory
# │   │
# │   └── Day-22/                                ← project root directory
# │       │
# │       ├── modules_imports_packages.py        ← module
# │       ├── calc.py                            ← module
# │       ├── math_tools.py                      ← module
# │       └── api/                               ← package
# │           └── client.py                      ← module
# │
# └── Phase-1/                                   ← directory