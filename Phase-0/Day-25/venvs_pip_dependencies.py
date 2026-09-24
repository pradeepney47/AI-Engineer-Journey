# Virtual Environments, pip, Dependencies

# This is important for AI engineering because your projects will depend on packages 
# such as NumPy, Pandas, PyTorch, FastAPI, etc. 
# You need to control which packages and versions belong to which project

# Imagine we have 2 projects
# Project A → needs numpy 1.x
# Project B → needs numpy 2.x

# If both projects use the same global Python environment, you can get conflicts

# Instead our ideal solution would be

# Project A
#    └── .venv
#        ├── Python
#        └── packages

# Project B
#    └── .venv
#        ├── Python
#        └── packages

# Each project gets its own isolated environment
# One project → one environment → its own dependencies

# Virtual Environment
# A virtual environment is an isolated Python environment associated with a project
# It allows you to install packages for one project without affecting other projects
# The two projects can have different dependencies

# AI-Engineer-Journey/
# │
# ├── Phase-0/
# │   └── Day-25/
# │       ├── .venv/
# │       └── main.py
# │
# └── another-project/
#     ├── .venv/
#     └── main.py

# without a virtual environment

# Your computer
#      │
#      └── Global Python
#              │
#              ├── requests
#              ├── numpy
#              ├── pandas
#              └── ...

# A virtual environment is not another operating system
# It is essentially an isolated Python environment with its own
# Python executable, package installation location, installed dependencies

# /AI-Engineer-Journey/Phase-0/Day-25
# python3 -m venv .venv #bash commnad creates virtual environment
# source .venv/bin/activate #activates the virtual environment with visual indication

# with a virtual environment

# Your computer
# │
# ├── Global Python
# │
# └── Your Project
#        │
#        └── .venv
#             │
#             ├── Python
#             ├── requests
#             ├── numpy
#             └── pandas

# What is pip?
# pip is Python's package installer

# python -m pip install requests
# Install the requests Python package into the currently selected Python environment

# Python
#   │
#   └── pip
#        │
#        ├── requests
#        ├── numpy
#        ├── pandas
#        └── ...

# pip is a package-management tool, not a Python library itself

# this Python
#     ↓
# run its pip
#     ↓
# install package

# python → one environment
# pip    → another environment

# import requests

# pip doesn't really contain requests

# .venv
# │
# ├── Python interpreter
# │
# └── Installed packages
#       └── requests

# pip is the tool that installs and manages those packages

# So, conceptually

# .venv
#    │
#    ├── Python
#    │
#    ├── pip ────── installs/manages ──────┐
#    │                                      ↓
#    └── site-packages                 requests

# python -m pip install requests
# Use this Python → run its pip → install requests
# And because .venv is active, python refers to the Python interpreter associated with that environment

# deactivate #this bash command will deactivate the virtual environment

# Exercise

# Project A
# └── .venv
#     └── requests

# Project B
# └── .venv
#     └── numpy

# You activate Project A's .venv and run:
# python -m pip install pandas

# Project A
# └── .venv
#     ├── requests
#     └── pandas   ← installed here

# .venv is the dedicated environment for Project A, 
# and pandas is one of the dependencies installed into that environment

# Project B
# └── .venv
#     └── numpy    ← unaffected

# Because you activated Project A's .venv, this:

# python -m pip install pandas

# Project A's Python
#         ↓
# Project A's pip
#         ↓
# Project A's .venv
#         ↓
# pandas

# Project B's .venv doesn't know or care that you installed pandas in Project A.

# This is the fundamental purpose of virtual environments

# Without isolation:

# Global environment
# ├── requests
# ├── pandas
# ├── numpy
# ├── torch
# ├── fastapi
# ├── ...

# Everything gets mixed together


# With isolation:

# AI Project
# └── .venv
#     ├── numpy
#     ├── pandas
#     └── torch

# Web Project
# └── .venv
#     ├── fastapi
#     └── requests

# Each project controls its own dependencies

# virtual environment → isolates dependencies

# What is requirements.txt?
# How do I tell another computer exactly which dependencies my project needs?

# Virtual environment
#         ↓
# isolates dependencies
#         ↓
# pip
#         ↓
# installs/manages dependencies


# But there is a practical problem.
# Suppose you build a project and install: numpy, pandas, requests, fastapi

# Then you give the project to someone else.
# How do they know what packages your project requires?
# That's what requirements.txt is for.

# 1. Think of requests.txt as dependency list

# requests
# numpy
# pandas

# "This project requires these Python packages."

# Someone can then install them with:

# python -m pip install -r requirements.txt

# -r means: Read the requirements from this file.

# requirements.txt
#        ↓
#       pip
#        ↓
# install all listed dependencies

# 2. But there's an important detail: versions

# You can specify versions:

# requests==2.32.5
# numpy==2.3.3
# pandas==2.3.2

# Now you're saying:
# "This project expects these particular versions."

# Why does that matter?
# Imagine you built your application using: numpy==2.3.3
# Six months later, someone installs the project and gets:numpy==3.x

# The newer version might behave differently or introduce incompatibilities.
# So, pinning versions can make the environment more reproducible.

# 3. Creating it with pip

# Suppose your .venv currently contains: numpy, pandas, requests
# You can generate a requirements file with:
# python -m pip freeze > requirements.txt

# Read this as

# pip freeze
#      ↓
# show installed packages + versions
#      ↓
# >
#      ↓
# write that output into
# requirements.txt

# For example:
# numpy==2.3.3
# pandas==2.3.2
# requests==2.32.5

# 4. Why this matters for your AI Engineer journey
# Later I will have project strucutre like this

# AI Agent
# ├── FastAPI
# ├── OpenAI SDK
# ├── Pydantic
# ├── NumPy
# ├── PostgreSQL client
# ├── LangGraph
# └── ...

# Your project shouldn't depend on:
# "Whatever happens to be installed on my laptop."

# Instead, you want:
# Project
#    │
#    ├── source code
#    ├── requirements.txt
#    └── .venv  ← local environment

# The .venv is your local working environment.
# The requirements.txt records the project's dependencies so the environment can be recreated.

# python -m pip freeze > requirements.txt
# This records the packages and versions installed in the currently active environment

# python -m pip install -r requirements.txt
# reads that file and installs the listed dependencies into the currently active environment

# this allows another developer to recreate a compatible dependency environment.

# Mental Model

# Project/
# │
# ├── .venv/                 ← Python environment (This is the environment in which your code runs, including the Python interpreter and installed third-party packages.)
# │   ├── Python
# │   ├── pip
# │   └── installed packages
# │
# ├── main.py                ← your source code
# ├── models.py              ← your source code
# ├── services/              ← your source code
# │   └── user_service.py
# │
# ├── requirements.txt       ← dependency specification (This is a record/instruction of what dependencies the project needs.)
# └── README.md

# Analogy

# Your project
# │
# ├── Source code       → the machine design
# ├── requirements.txt  → list of components needed
# └── .venv             → your workshop containing those components

# You generally do not put your source code inside the workshop's installed-package area.
# And there's another important practical rule:
# You normally do NOT commit .venv to Git.

# You commit:
# main.py
# requirements.txt
# README.md
# ...
# but not the entire .venv.

# Another developer can then do:
# python3 -m venv .venv
# source .venv/bin/activate
# python -m pip install -r requirements.txt
# and recreate their own environment.
# That is a very important real-world development workflow, and you'll use it constantly as an AI engineer.

# pip install -r requirements.txt
# It recreates the specified package environment by installing the dependencies and versions listed in requirements.txt
# It doesn't reproduce the .venv itself. It creates/uses an environment and installs the specified dependencies into it.

#               PROJECT
#                  │
#        ┌─────────┼─────────┐
#        ↓         ↓         ↓
#    source      .venv    requirements
#     code     environment     list
#      │           │            │
#    YOUR       Python +      WHAT
#    CODE       packages      PROJECT NEEDS

# What actually prevents Git from committing .venv?
# A .gitignore file.
# For example:
# # .gitignore

# .venv/

# Now Git is instructed:
# Ignore the .venv directory and its contents.
# So:
# Project/
# │
# ├── .venv/              ← ignored by Git
# ├── main.py             ← tracked
# ├── requirements.txt    ← tracked
# └── .gitignore          ← tracked

# Why .venv is usually ignored
# Because there's no reason to upload your entire local Python environment to GitHub.
# Instead, you upload:
# requirements.txt
# and another developer creates their own:
# .venv
# from that dependency specification.
# So remember:
# . = hidden
# .gitignore = tells Git what not to track
# And .venv/ is conventionally named with a dot because it is a local project-support directory 
# that you normally do not need cluttering the project view.

# which python 
# After activation of venv, you should see a path containing:
# .../Day-25/.venv/bin/python
# a useful verification whether the python runs in virtual environment or some other place

# Right now, your shell is using:
# Day-25's Python, not the global Python installation.

# This is the key mental model

# Day-25 project
# │
# ├── venvs_pip_dependencies.py
# ├── requirements.txt
# │
# └── .venv/
#     └── bin/
#         └── python  ← THIS is currently active

# And because this Python belongs to .venv, when you run:
# python -m pip install something
# that package gets installed into Day-25's environment.


# Day-25/.venv
# │
# ├── bin/
# │   └── python
# │
# └── lib/
#     └── python3.14/
#         └── site-packages/
#             └── pip

# You
#  │
#  │ python -m pip install ...
#  ↓
# Python inside Day-25/.venv
#  │
#  ↓
# pip inside Day-25/.venv
#  │
#  ↓
# packages installed into
# Day-25/.venv

# install requests

# python -m pip install requests
# python -m pip list

# Before:
# .venv
# └── pip
#     └── ...

# After:
# .venv
# ├── pip
# ├── requests
# ├── urllib3
# ├── certifi
# ├── charset-normalizer
# └── ...

# "Install requests and make sure everything requests needs is also available."
# Pip resolved those dependencies for you.

# Your application
#        │
#        ↓
#    requests          ← direct dependency
#     / |  |  \
#    ↓  ↓  ↓   ↓
# urllib3 ...        ← transitive dependencies

# This concept becomes very important in AI engineering, because later you'll install packages that 
# themselves have many dependencies.

# Your AI application
#        ↓
#     FastAPI
#        ↓
#    Starlette
#        ↓
#     ...

# and:

# Your AI application
#        ↓
#     AI SDK
#        ↓
#    HTTP libraries
#        ↓
#    other libraries

# python -m pip show requests
# and look for the Requires: contains dependency relationship required for requests that got automatically installed

# requests = your project's direct dependency
# The four underneath = dependencies of requests
# Pip installed all of them automatically.

# Create requirements.txt
# python -m pip freeze > requirements.txt
# cat requirements.txt

# pip freeze records everything installed in the environment, including transitive dependencies.
# So requirements.txt is essentially a snapshot of the environment's installed packages and versions.


# Day 25 Mental Model

# Create environment
#       ↓
# python3 -m venv .venv
#       ↓
# Activate environment
#       ↓
# source .venv/bin/activate
#       ↓
# Install dependency
#       ↓
# python -m pip install requests
#       ↓
# Inspect installed packages
#       ↓
# python -m pip list
#       ↓
# Record environment
#       ↓
# python -m pip freeze > requirements.txt

# There are two useful ideas here:
# pip list
# What's installed in my current environment?
# pip freeze
# Give me the installed packages and exact versions in a format I can use to recreate this environment.
# And:
# requirements.txt
# A file that specifies the dependencies and versions needed to recreate an environment.

# Let's prove that the environment is actually isolated.

# python -m pip uninstall requests

# When pip asks for confirmation, enter:
# y

# Then run:
# python -m pip list

# You should see that requests and its now-unneeded dependencies may disappear.
# But your requirements.txt file will still contain the original entries.


# That's an important distinction:
# requirements.txt
#       │
#       │ describes
#       ↓
# what the project requires

# .venv
#       │
#       │ contains
#       ↓
# what is currently installed
# So the file is a specification, while .venv is an actual environment.

# python -m pip install -r requirements.txt
# Pip reads the file and installs the specified packages and versions into your currently active .venv.
# Then verify:
# python -m pip list
# You should see requests again.

#  requirements.txt
#        │
#        │ specification
#        ↓
# python -m pip install -r requirements.txt
#        │
#        ↓
#      .venv
#        │
#        ├── requests
#        ├── urllib3
#        ├── certifi
#        ├── idna
#        └── charset-normalizer

# This is the practical meaning of reproducible environments.
# If you clone a Python project onto another machine, you don't need to copy your .venv. 
# You create a fresh .venv and install the project's dependencies from its specification.

# When you're finished working, you can leave the environment with:
# deactivate
# Your terminal's:
# (.venv)
# will disappear.
# Then, when you return to the project later:
# source .venv/bin/activate
# and you're back inside the project's environment.
