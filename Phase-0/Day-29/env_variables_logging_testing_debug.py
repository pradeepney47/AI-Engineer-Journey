# Environmental variables, logging, testing basics, and debugging

# Day 29: Python Engineering Practices
# 1. Environment Variables
#    os.getenv(), .env, secrets, configuration
# 2. Logging
#    logging, log levels, useful diagnostic information
# 3. Testing Basics
#    assert, unittest/pytest concepts, test structure
# 4. Debugging
#    Tracebacks, reading errors, print() debugging, debugger/breakpoints, inspecting variables, systematic debugging

# Error
#   ↓
# Read traceback
#   ↓
# Locate failure
#   ↓
# Inspect state
#   ↓
# Form hypothesis
#   ↓
# Test hypothesis
#   ↓
# Fix
#   ↓
# Test again


# That debugging workflow is particularly important for your AI engineering journey 
# because later you'll be debugging APIs, RAG pipelines, agents, async code, databases, 
# and production systems, not just syntax errors.



# 1. Environmental Variables
# os.getenv(), .env, secrets, configuration
print()

# In the bash type the command
# export API_KEY="abc123"

# Bash shell
#    ↓
# export API_KEY="abc123"
#    ↓
# Environment variable
#    ↓
# Python process starts
#    ↓
# os.getenv("API_KEY")
#    ↓
# "abc123"

import os
# Give or read the value associated with the environment variable named API_KEY
api_key = os.getenv("API_KEY")

if api_key is None:
    print("API Key is missing")
else:
    print(api_key)

# Python provides easy way to handle this
# "API Key is missing..." is the default value
api_key = os.getenv("API_KEY", "API Key is missing...")
print()
print(api_key)

# remove export value from bash
# type the following bash command
# unset API_KEY
# echo $API_KEY

# Useful bash commands

# export API_KEY="abc123"   # create/set it
# echo $API_KEY             # check it
# unset API_KEY             # remove it
# echo $API_KEY             # should now be empty

# unset removes it from the current shell environment. If you open a new terminal, 
# the variable will only be present again if something else sets it, such as your shell configuration or a .env loader.

# Reading from .env file the API_KEY
# Create a virtual environment and install dotenv
# In bash do this
# python -m pip install python-dotenv

# Also, just save the dependency using the following bash command
# python -m pip freeze > requirements.txt


# .env file
#    ↓
# load_dotenv()
#    ↓
# Python process environment

# load_dotenv() reads the .env file and makes those values available to the current Python process


# What goes into production?
# Usually, you don't rely on a .env file containing production secrets.
# A production deployment typically provides secrets through:
# deployment environment
#         ↓
# environment variables / secret manager
#         ↓
# os.getenv()
# So .env is particularly convenient for local development.


from dotenv import load_dotenv
print()
print(os.getenv("API_KEY")) #prints None

load_dotenv() #reads .env and loads API_KEY into the current Python process environment
print()
print(os.getenv("API_KEY")) #prints the api key




# from dotenv import load_dotenv
# import os

# load_dotenv()

api_key = os.getenv("API_KEY")

print(api_key)




# With load_dotenv()

# .env file
#    ↓
# load_dotenv()
#    ↓
# process environment
#    ↓
# os.getenv("API_KEY")
#    ↓
# value

# And without load_dotenv()

# Without load_dotenv()
#     ↓
# .env is just a file
#     ↓
# os.getenv() does not automatically read it


# Remember this always

# Create project
#     ↓
# Create .venv
#     ↓
# Activate .venv
#     ↓
# Install packages
#     ↓
# Write code


# One important engineering habit
# Create .gitignore:
# .venv/
# .env
# This means:
# - .venv/ → don't commit your local virtual environment
# - .env → don't commit your secrets
# Then check:
# git status
# Neither should appear as files to commit.





# 2. Logging
# logging, log levels, useful diagnostic information

# Logging?
# Logging means recording information about what your program is doing while it runs
# logging gives the message a severity level

# Severity level of the logging message moving from less to more
# DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL

# DEBUG      → detailed information for debugging
# INFO       → normal program events
# WARNING    → something unexpected, but program can continue
# ERROR      → something failed
# CRITICAL   → serious failure

# Example in AI applicaton about logging 

# logging.debug("Retrieved 5 documents")
# logging.info("Starting RAG query")
# logging.warning("Only 2 relevant documents found")
# logging.error("LLM API request failed")


print()
import logging
# accessing the attribute
# object.method(keyword_arguemnt=value.attribute)
logging.basicConfig(level=logging.WARNING) # prints the severity and above this

# method call
# object.method(argument)
logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message") #prints this
logging.error("Error message") #prints this as well because it is above Warning (as we configured level=logging.WARNING earlier)

# Mental Model

# basicConfig(level=WARNING)
#         ↓
# configure logging
#         ↓
# DEBUG    → hidden
# INFO     → hidden
# WARNING  → shown
# ERROR    → shown



# Logging Mental Model

# 1. Configure logging
#        ↓
# logging.basicConfig(level=...)

# 2. Emit log messages
#        ↓
# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical()

# Also,
# logging.WARNING  → value/constant
# logging.warning() → method call



# basicConfig() is normally something you configure once, near the beginning of your program.

# And this is another example of why runtime state matters. The exact same line can behave differently depending 
# on what has already happened in the current Python process.


# import logging
print()
logging.basicConfig(level=logging.INFO)

logging.debug("A")
logging.info("B")

#prints C (now this is treshold because "The logging system is already configured, so it won't reconfigure it.")

# Once basicConfig() has configured the logging system, subsequent basicConfig() calls don't normally reconfigure it.


logging.warning("C") 
logging.error("D") #prints this
logging.critical("E") #prints this




# If you ran exactly the fresh code we discussed, INFO should appear. 
# If you got only C D E, there is almost certainly a logging configuration already active in that Python process.
# The most likely reason is that you previously ran something like:
# logging.basicConfig(level=logging.WARNING)

# and then changed it to:
# logging.basicConfig(level=logging.INFO)


# Mental Model for logging

# First basicConfig()
#         ↓
# configure logging
#         ↓
# already configured
#         ↓
# Second basicConfig()
#         ↓
# ignored

# But there is forced reconfiguration of logging too 
logging.basicConfig(level=logging.INFO, force=True)
print()
logging.debug("A")
logging.info("B") #Now this forced version prints this (so a forced reconfiguration of logging is possible)
logging.warning("C") #prints this
logging.error("D") #prints this
logging.critical("E") #prints this

# But ideally we do not use this forced version
# Instead
# Configure logging once, near the start of the program, before emitting log messages.

# Logging records runtime events.
# Levels: DEBUG → INFO → WARNING → ERROR → CRITICAL
# basicConfig(level=...) establishes the threshold.
# Configure logging before emitting messages.
# basicConfig() normally doesn't reconfigure an already-configured logging system.
# logging.warning() is a method call.
# logging.WARNING is a value/constant.




# 3. Testing Basics
# assert, unittest/pytest concepts, test structure

# Verify that the code behaves the way it is expected

# if not condition:
#     raise AssertionError

print()

def add(a, b):
    return a + b

# Assertion test
assert add(3, 2) == 5 # pass the assertion test

try:
    assert add(3, 2) == 6 # raise AssertionError
except AssertionError:
    print("Failed the testing")


# Exercise
print()
def multiply(a, b):
    return a * b

try:
    assert multiply(3, 4) == 13
    print("Test passed")
except AssertionError:
    print("Test failed")


# In testing, we usually want a failed assertion to fail the test, rather than manually printing "Test failed"
# In our example if the result is 13, the assertion fails and the testing framework reports the failure and this is where
# pytest is useful

# pytest test

# As project grows, you don't want to manually run dozens or hundreds of assertions.
# pytest is a testing framework that discovers and runs your tests for you.

# In the Zsh bash terminal use the following command to create and write to a file named math_test.py
# cat << 'EOF' > math_test.py 

# The function name starts with test_.
# def test_multiply():
# Pytest uses naming conventions to discover tests.

# from the terminal run pytest

# The important conceptual flow is:
# pytest
#    ↓
# finds test_math.py
#    ↓
# finds test_multiply()
#    ↓
# runs it
#    ↓
# assertion is True
#    ↓
# PASSED

# math_test.py . 

# The dot after py means the test is passed

#  In failure case

# math_test.py F                                                                                                                                           [100%]

# =========================================================================== FAILURES ===========================================================================
# ________________________________________________________________________ test_multiply _________________________________________________________________________

#     def test_multiply():
# >       assert multiply(3, 4) == 13
# E       assert 12 == 13
# E        +  where 12 = multiply(3, 4)

# math_test.py:6: AssertionError
# =================================================================== short test summary info ====================================================================
# FAILED math_test.py::test_multiply - assert 12 == 13
# ====================================================================== 1 failed in 0.03s =======================================================================


# Mental Model

# Write code
#    ↓
# Write test
#    ↓
# pytest
#    ↓
# Pass? ── Yes → ✓
#    │
#    No
#    ↓
# Read failure information
#    ↓
# Find the problem
#    ↓
# Fix code
#    ↓
# Run pytest again




# 4. Debugging
# Tracebacks, reading errors, print() debugging, debugger/breakpoints, 
# inspecting variables, systematic debugging

# Syntax error      → Python cannot understand the code
# Runtime error     → program crashes while running
# Logical error     → program runs but gives the wrong result


print()

def calculate_total(price, quantity):
    total = price + quantity # there is a bug here in the code (logical error)
    return total

result = calculate_total(100, 3)

print(result)


# breakpoint() - this is python's built in debugger (Pause execution of the program so I can inspect the current state)

def calculate_total(price, quantity):
    total = price * quantity
    breakpoint() #python pauses the execution further and opens the debugger so I can inspect the current state
    return total

result = calculate_total(100, 3)
print(result)


# calculate_total(100, 3)
#         ↓
# price = 100
#         ↓
# quantity = 3
#         ↓
# total = 300
#         ↓
# breakpoint()
#         ↓
# ⏸ PAUSE
#         ↓
# inspect variables / step through code
#         ↓
# return total

# Mental Model for Debugging using breakpoint()

# Observe
#    ↓
# Locate
#    ↓
# Inspect
#    ↓
# Identify
#    ↓
# Fix
#    ↓
# Test again


# Other debugging concepts include

# There is a lot more to debugging, including:
# - Breakpoints
# - Stepping over / into / out of functions
# - Inspecting variables
# - Call stack
# - Watch expressions
# - Conditional breakpoints
# - Exception debugging
# - Reading tracebacks
# - Debugging loops
# - Debugging async code
# - Debugging API requests
# - Debugging tests
# - IDE debugging
# - Logging-based debugging
# - Remote debugging
# - Profiling and performance debugging