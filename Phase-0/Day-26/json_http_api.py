# JSON + HTTP + APIs

import requests

# Python program
#       ↓
#      HTTP
#       ↓
#      API
#       ↓
#  external service
#       ↓
#     JSON
#       ↓
# Python objects

# This connection is foundational for the AI projects you want to build later, 
# especially when your Python application starts communicating with LLM APIs and other services

# An important day for your AI Engineer path because we're moving from Python running locally 
# to Python communicating with other systems

# Mental Model

# Your AI application
#        ↓
#       API
#        ↓
# LLM / database / external service
#        ↓
#       API
#        ↓
# Your application

# 1. JSON
# JavaScript Object Notation
# Despite the name, you will use JSON heavily with Python

# This is data that represents structured information
# name   → "Pradeep"
# age    → 36
# skills → ["Python", "AI"]

# which is expressed in JSON format
# </> JSON
# {
#   "name": "Pradeep",
#   "age": 36,
#   "skills": ["Python", "AI"]
# }

# Python can represent this JSON data as

user = {
    "name": "Pradeep",
    "age": 36,
    "skills": ["Python", "AI"]
}


# There is an important distinction between JSON and Python 

# JSON             Python
# ────             ──────
# JSON object      dict
# JSON array       list
# JSON string      str
# JSON number      int/float
# JSON true        True
# JSON false       False
# JSON null        None

# JSON is a data interchange format
# Python dict/ list/ str/ int/ float/ True/ False/ None is a Python object/data structure

# JSON and Python look similar but they are not the same

# 2. Why API's use JSON?

# Suppose your Python application asks a weather service:
# "What is the weather?"
# The service needs to send structured information back.

# It could respond:
# {
#   "temperature": 30,
#   "humidity": 72,
#   "condition": "Cloudy"
# }

# Your Python application receives that data and can turn it into Python objects:
# data = {
#     "temperature": 30,
#     "humidity": 72,
#     "condition": "Cloudy"
# }

# So conceptually:
# External API
#      │
#      │ JSON
#      ↓
# Python application
#      │
#      │ Python dict/list/etc.
#      ↓
# Your code

# This is why JSON is so important for API development.

# 3. JSON serialization and deserialization

# Serialization (Python object → JSON)

# Python dict
#  ↓
# JSON

# Deserialization (JSON → Python object)

# JSON
#  ↓
# Python Dict

# Python's standard library has a module called json for this

import json

user = {
    "name": "Pradeep",
    "age": 36
}
print(type(user)) #dictionary
print(user)

# serialisation
json_text = json.dumps(user) #Convert a Python object into a JSON string
print()
print(type(json_text)) #string
print(json_text)

# deserialisation
data = json.loads(json_text) #Take JSON text and convert it into a Python object
print()
print(type(data)) #dictionary
print(data)

# json.dumps()
# Python → JSON
# dump  → Python → JSON

# json.loads()
# JSON → Python
# load  → JSON → Python

# 5. HTTP
# JSON is the data format.
# HTTP is the communication protocol.

# Imagine:
# Python application
#        │
#        │ HTTP request
#        ↓
#      API server
#        │
#        │ HTTP response
#        ↓
# Python application

# The request might contain JSON. 
# The response might contain JSON.

# 6. HTTP methods

# Method	Typical meaning

# POST	    Create/send data
# GET	    Retrieve data
# PUT	    Update/ Replace data
# PATCH	    Partially update data
# DELETE	Delete data

# Example
# GET /users/123 means roughly like "Give me user 123."
# POST /users means roughly like "Create a new user using the data I'm sending."

# 7. API
# Now we can define an API more precisely.
# An API (Application Programming Interface) is an interface through which one software system can interact with 
# another according to defined rules.

# For an HTTP API, you might have:
# GET https://example.com/users/123

# The server processes the request and returns something like:

# </>JSON
# {
#   "id": 123,
#   "name": "Pradeep"
# }

# Your Python program doesn't need to know how the server internally retrieved the user.

# Our Python program only needs to know:
# Where to send the request
# What request to make
# What data to send
# What response to expect
# That's the power of an API abstraction.

# Exercise

# Consider API response in JSON
# </> JSON
# {
#   "name": "Alice",
#   "age": 30,
#   "active": true,
#   "skills": ["Python", "SQL"]
# }

# Then the eqiuvalent Python object conceptually will be
# </> Python
# {
#     "name": "Alice",
#     "age": 30,
#     "active": True,
#     "skills": ["Python", "SQL"]
# }

# dict
# │
# ├── name   → str
# ├── age    → int
# ├── active → bool
# └── skills → list
#               │
#               ├── str
#               └── str

# This nested-data model is extremely important for API work. 
# API responses are often dictionaries containing lists, dictionaries containing dictionaries, 
# lists of dictionaries, and so on.

# Let us connect JSON to an actual API using a public test API
# We'll make a simple GET request from Python

# The important flow is:
# requests.get(...)
#        ↓
# HTTP GET request
#        ↓
# API server
#        ↓
# HTTP response
#        ↓
# response object


# The flow 

# HTTP response
#       ↓
# response.text
#       ↓
# JSON text
#       ↓
# response.json()
#       ↓
# Python dict


# HTTP
# │
# ├── Request
# │   ├── method
# │   ├── URL
# │   ├── headers
# │   └── optional body
# │
# └── Response
#     ├── status code
#     ├── headers
#     └── body
#           │
#           └── could be JSON, HTML, text,
#               image, binary data, etc.



# HTTP response example

# ┌─────────────────────────────────┐
# │ Status line                     │
# │ HTTP/1.1 200 OK                 │
# ├─────────────────────────────────┤
# │ Headers                         │
# │ Content-Type: application/json  │
# │ ...                             │
# ├─────────────────────────────────┤
# │ Body                            │
# │                                 │
# │ {                               │
# │   "id": 1,                      │
# │   "name": "Leanne Graham"       │
# │ }                               │
# └─────────────────────────────────┘

# Accessing the HTTP response

# Status line can be accessed as response.status_code
# Headers can be accessed as response.headers
# Body can be accessed as response.text will be given as python str or 
# if accessed as response.json() parses that same body as JSON and gives a Python object (dictionary)

# HTTP response body can contain any format. It could be plain text or HTML or JSON or XML, etc.
# Content-Type: text/plain or Content-Type: text/html or Content-Type: application/json or Content-Type: application/xml, etc.

# Same HTTP response body
#           │
#           ├── response.text
#           │       ↓
#           │   Python str
#           │   containing JSON text
#           │
#           └── response.json()
#                   ↓
#             JSON parsing
#                   ↓
#              Python object



#                  HTTP
# Your Python ───────────────→ API server
#              GET /users/1

# Your Python ←─────────────── API server
#               HTTP response
#                    │
#                    ↓
#           requests creates
#           a Response object
#                    │
#           ┌────────┼─────────┐
#           ↓        ↓         ↓
#    status_code    text      json()
#           ↓        ↓         ↓
#          200      str       dict
#                    │          │
#                    │          │
#              JSON text     parsed data

# or

#                    HTTP
# Python ─────────────────────────→ API
#        GET /users/1

# Python ←───────────────────────── API
#               Response
#                  │
#                  ↓
#         Response object
#                  │
#        ┌─────────┼──────────┐
#        ↓         ↓          ↓
#  status_code   text       json()
#        │         │          │
#        ↓         ↓          ↓
#       200      str       Python dict
#                          │
#                          ↓
#                   Your application


# or

# API server
#    │
#    │ HTTP response
#    │
#    ├── status: 200
#    │
#    └── body: JSON-formatted text
#               │
#               ↓
#         requests library
#               │
#               ↓
#        Response object
#               │
#        ┌──────┴────────┐
#        ↓               ↓
# response.text    response.json()
#        ↓               ↓
#      str              dict

# And JSON is just one common format for the body.
# For your AI Engineer journey, you'll encounter JSON extremely frequently 
# because LLM APIs, web APIs, tool calls, and many backend services commonly exchange structured data using JSON. 
# But now you know the deeper principle: The API contract tells you what to expect, and the HTTP Content-Type header 
# tells you what representation the server is providing.

# Important hierarchy

# HTTP
# │
# ├── Request
# │   ├── Method
# │   ├── URL
# │   ├── Headers
# │   └── Optional Body
# │
# └── Response
#     ├── Status code
#     ├── Headers
#     └── Body
#          └── JSON / HTML / text / binary / ...


# JSON specifically:

# Python object
#     ↓ serialize
# JSON
#     ↓
# HTTP request body

# HTTP response body
#     ↓
# JSON parsing
#     ↓
# Python object

#






# HTTP Requests
# what your application actually sends to the server
# requests constructs an HTTP request for you


# An HTTP request has several parts

# HTTP REQUEST
# │
# ├── Method
# ├── URL
# ├── Headers
# └── Body (optional)

# 1. Method
# GET
# POST
# PUT
# PATCH
# DELETE

# 2. URL
# https://jsonplaceholder.typicode.com/users/1

# Conceptually we can see the request as

# https://
#    ↓
# protocol/scheme

# jsonplaceholder.typicode.com
#    ↓
# host

# /users/1
#    ↓
# path

# URL tells the client where to send the request and which resource/endpoint it wants

# 3. Headers

# Headers are metadata about the request.
# Content-Type: application/json
# which means:
# "The body I'm sending is JSON."
# It can also send things such as:
# Authorization: ...
# Accept: application/json


# headers = {
#     "Accept": "application/json"
# }

# requests.get(url, headers=headers)

# Accept means roughly:
# "I would like the response in this format."

# Content-Type
# What format is the body I'm sending?
# Accept
# What format would I like the response to be?

# 4. Request body

# A request may have a body, but it doesn't have to.
# Your GET request:
# requests.get(url)
# doesn't need a body.

# But imagine you're creating a user.
# You might send:
# user = {
#     "name": "Alice",
#     "age": 30
# }
# and make:
# requests.post(url, json=user)

# Now something interesting happens.
# You gave requests a Python dictionary:
# user
# but you're telling requests:
# json=user
# The library handles the JSON serialization for you.

# Conceptually:
# Python dict
#     ↓
# requests
#     ↓
# JSON
#     ↓
# HTTP request body
# The request might look conceptually like:
# POST /users HTTP/1.1
# Content-Type: application/json

# {
#     "name": "Alice",
#     "age": 30
# }

# Why json= is convenient?

# We can manually write the program to convert dictionary to JSON as

# import json

# user = {
#     "name": "Alice",
#     "age": 30
# }

# body = json.dumps(user)

# requests.post(
#     url,
#     data=body,
#     headers={"Content-Type": "application/json"}
# )

# but there is an easy way because requests handles that

# requests.post(url, json=user)

# which handles the JSON serialization and appropriate content type for you.

# So, we can replace this part easily body = json.dumps(user) with the use of json = user

# OUTBOUND
# Python dict
#     ↓
# json=
#     ↓
# JSON request body
#     ↓
# HTTP
#     ↓
# Server


# INBOUND
# Server
#     ↓
# HTTP
#     ↓
# JSON response body
#     ↓
# response.json()
#     ↓
# Python object


# Example

# user = {
#     "name": "Alice",
#     "age": 30
# }

# response = requests.post(
#     "https://example.com/users",
#     json=user
# )

# Content-Type ≠ response format
# Accept ≈ preferred response representation

# Mental Model fundamental request/response + JSON 

#                  REQUEST
# Your app ─────────────────────────→ Server
#           │
#           ├── Method: POST
#           ├── URL: /users
#           ├── Content-Type: application/json
#           ├── Accept: application/json
#           │
#           └── Body
#                ↓
#           JSON data


#                  RESPONSE
# Your app ←───────────────────────── Server
#           │
#           ├── Status code: 201
#           ├── Content-Type: application/json
#           └── Body
#                ↓
#           JSON data
#                ↓
#        response.json()
#                ↓
#           Python object



# Query parameters vs Request body

# when you start calling real APIs you will constantly see URLs like:
# /users?country=India&limit=10
# and it's important to understand why that data is in the URL rather than the body

# Query Parameters
# They're commonly used to filter, search, sort, paginate, optional configuration of a GET request 
# or customize what resource you're asking for.

# https://example.com/users?country=India&limit=10 # URL
# ?country=India&limit=10 # this is the query part or string in the URL

# contains query parameters
# country = India
# limit   = 10

# Conceptually

# /users
#    │
#    └── resource/path

# ?country=India&limit=10
#    │
#    └── query parameters

# How requests do this query parameter?

# params = {
#     "country": "India",
#     "limit": 10
# }

# response = requests.get(
#     url,
#     params=params
# )

# requests constructs the query string for you like ?country=India&limit=10 adding it after url

# Conceptually:
# Python dict
#     ↓
# params=
#     ↓
# URL query parameters
#     ↓
# HTTP GET request


# Mental Model
# HTTP request
# │
# ├── URL
# │    └── query parameters
# │
# ├── Headers
# │    └── metadata
# │
# └── Body
#      └── data being sent


# params = {
#     "page": 2,
#     "limit": 20
# }

# response = requests.get(
#     "https://example.com/users",
#     params=params
# )

# params=:
# requests.get(url, params=params)
# puts the values into the URL's query string:
# https://example.com/users?page=2&limit=20
#                               ↑
#                          query parameters


# Mental Model to keep in mind

# requests.get(
#     url,
#     params=...
# )

#        ↓

# URL
# └── ?key=value&key=value


# requests.post(
#     url,
#     json=...
# )

#        ↓

# Request body
# └── JSON


# Let us connect this to something you'll see constantly in AI APIs

# Path parameters vs query parameters vs request body

# /users/123 is path parameter

# vs

# /users?country=India is query parameter

# vs

# request body in JSON format
# {
#     "name": "Alice",
#     "age": 30
# }

# Understanding why data goes in each location is an important part of becoming comfortable with APIs


# https://example.com
#        │
#        └── /users/123       ← path
#               │
#               └── ?active=true  ← query


params = {
    "page": 2,
    "limit": 10
}

user = {
    "name": "Alice",
    "age": 30
}

response = requests.post(
    "https://example.com/users/123",
    params=params,
    json=user
)

# https://example.com/users/123?...
# └──────┬──────┘└──────┬─────┘
#       host            path


# The API defines what these parameters mean.
# Typically:
# page=2
# means:
# Give me the second page of results.
# and:
# limit=10
# means:
# Return at most 10 results.
# So conceptually:
# /users/123?page=2&limit=10
#           └──────┬──────┘
#           query parameters
# But notice something interesting:
# We're requesting:
# /users/123
# which sounds like one specific user.
# Therefore, whether page and limit make sense here depends entirely on how that particular API endpoint is designed. 
# The URL is syntactically valid, but the API may ignore those parameters or reject them.


# HTTP gives you the mechanisms. The API documentation defines their meaning.

# 3. Request body
# user = {
#     "name": "Alice",
#     "age": 30
# }
# is a Python dictionary.
# Then:
# json=user
# tells requests to serialize that data as JSON for the request body.

# Conceptually:
# Python dict
#      ↓
# JSON serialization
#      ↓
# HTTP request body

# 4. What does 123 represent?

# It's specifically a path segment whose meaning is defined by the API.
# In this example, the API has presumably designed:
# /users/{id}
# where {id} is a user identifier.
# Therefore:
# /users/123
#        ↑
#    user ID
# So the request means approximately:
# "Operate on the user identified by 123."
# Because this is a POST, the exact meaning still depends on the API's contract.
#  It could mean "perform some operation for user 123", for example. We shouldn't 
#     assume every /users/123 endpoint has the same behavior.


# https://example.com/users/123?page=2&limit=10

# https://example.com
# └──────┬──────┘
#        host

# /users/123
# └──────┬────┘
#       path
#        │
#        └── 123 = path parameter/value

# ?page=2&limit=10
# └──────┬────────┘
#      query

# Then separately:
# {
#     "name": "Alice",
#     "age": 30
# }
# is the request body.

# So the complete request can be visualized as:
# HTTP REQUEST
# │
# ├── URL
# │   ├── Host: example.com
# │   ├── Path: /users/123
# │   └── Query: page=2&limit=10
# │
# ├── Headers
# │
# └── Body
#     └── JSON
#         {
#             "name": "Alice",
#             "age": 30
#         }

# Path identifies the resource/operation, 
# query parameters modify or constrain the request, 
# and the body carries data being submitted.

# The exact semantics are ultimately determined by the API's contract/documentation.

# HTTP Status codes

# HTTP status codes
# When your Python code sends a request, the server returns a status code telling you what happened.

# The most important ones:

# Code	Meaning	                Typical interpretation
# 200	OK	                    Request succeeded
# 201	Created	                Resource was successfully created
# 400	Bad Request	            Your request is invalid
# 401	Unauthorized	        Authentication is required/invalid
# 403	Forbidden	            You are authenticated but not allowed
# 404	Not Found	            Resource/endpoint doesn't exist
# 500	Internal Server Error	Server encountered an error

#Python program
#      │
#      │ HTTP request
#      ▼
#    Server
#      │
#      │ HTTP response
#      ▼
# status_code + headers + body


# if response.status_code == 200:
#     print("Success")
# else:
#     print("Something went wrong")


# Raise for Status
# raise_for_status()

# Instead of manually checking every status code:
# if response.status_code != 200:
#     ...
# requests gives you:
# response.raise_for_status()
# If the response indicates an HTTP error such as 404 or 500, it raises an exception.


# For example:
# response = requests.get(url)

# response.raise_for_status()

# data = response.json()


# Mental model for raise for status

# request
#    ↓
# response
#    ↓
# raise_for_status()
#    ↓
# error? ── yes → exception
#    │
#    no
#    ↓
# parse JSON

# Example

# response = requests.get(url)
# response.raise_for_status()

# Case1: Success

# If the server returns: 200

# then: response.raise_for_status() does nothing and execution continues.

# data = response.json()
# print(data)

# So:
# 200
#  ↓
# raise_for_status()
#  ↓
# no exception
#  ↓
# continue

# Case2: HTTP Error

# If the server returns: 404
# then: response.raise_for_status() raises a requests exception, specifically an HTTP error exception.

# Execution stops at that line unless you handle the exception:
# try:
#     response.raise_for_status()
# except requests.HTTPError as e:
#     print("Request failed:", e)

# Mental model:
# status_code
#      ↓
# raise_for_status()
#      │
#      ├── 2xx → continue
#      │
#      └── 4xx/5xx → raise HTTPError

# One subtle point
# raise_for_status() does not parse the JSON.
# These are separate jobs:
# response.raise_for_status()  # Check HTTP success
# data = response.json()       # Parse JSON body
# That distinction is important in AI/backend engineering because you'll constantly be doing:
# request → validate response → parse data → use data


# When exception is not handled

# response = requests.get(url)   # server returns 404

# response.raise_for_status()

# print("Hello")

# This is the flow when exception is not handled

# requests.get()
#      ↓
# response = Response(404)
#      ↓
# raise_for_status()
#      ↓
# HTTPError raised
#      ↓
# no except block
#      ↓
# program stops
#      ↓
# "Hello" is NOT printed


# When the exception is handled

# try:
#     response.raise_for_status()
# except requests.HTTPError:
#     print("Request failed")

# print("Hello")

# This is the flow

# 404
#  ↓
# HTTPError
#  ↓
# except catches it
#  ↓
# "Request failed"
#  ↓
# "Hello"

# One important distinction

# There are actually two different failure categories we should keep separate:

# One is HTTP Error and the other is Python/ Runtime problem

# One silo

# HTTP error
#     ↓
# 404, 401, 500...
#     ↓
# raise_for_status()
#     ↓
# requests.HTTPError

# The other silo

# Python/runtime problem
#     ↓
# wrong code, invalid operation, etc.
#     ↓
# other Python exception

# This distinction becomes important when we build API clients.




# Request headers 
# another major part of HTTP and APIs

# What is a header?
# An HTTP request contains more than just a URL and possibly a body.
# Headers carry metadata about the request.

# Example

# headers = {
#     "Authorization": "Bearer abc123",
#     "Accept": "application/json"
# }

# response = requests.get(
#     "https://example.com/users",
#     headers=headers
# )

# Conceptually:

# HTTP Request
# │
# ├── Method       GET
# ├── URL          /users
# ├── Headers
# │    ├── Authorization: Bearer abc123
# │    └── Accept: application/json
# │
# └── Body         usually absent for GET

# Two headers to understand first
# Accept
# Tells the server:
# "This is the response format I would like to receive."
# "Accept": "application/json"
# means:
# Prefer JSON in the response.
# Content-Type
# Tells the server:
# "This is the format of the data I am sending in the request body."
# For example:
# "Content-Type": "application/json"
# means:
# The request body contains JSON.


# Accept
#     → What format do I want BACK?

# Content-Type
#     → What format am I SENDING?


# Exercise

# headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/json"
# }

# requests.post(
#     "https://example.com/users",
#     headers=headers,
#     json={"name": "Alice"}
# )

# "Content-Type": "application/json" # format that is being send to API server

# "Accept": "application/json" # format I expect from the API server


# "Content-Type": "application/json"
# # format of the data being sent to the API server

# "Accept": "application/json"
# # format of the response expected from the API server
# A useful mental shortcut:
# Content-Type = “What am I sending?”
# Accept = “What do I want back?”
# And notice something interesting in your earlier requests.post() example:
# requests.post(
#     url,
#     json={"name": "Alice"}
# )
# When you use json=, requests handles the JSON serialization and the appropriate Content-Type header for you. 
# You don't normally need to manually write it.


# Mental Model so far

# Python object
#      ↓
# json=
#      ↓
# JSON request body
#      ↓
# HTTP request
#      │
#      ├── Method
#      ├── URL
#      ├── Query parameters
#      ├── Headers
#      └── Body
#               ↓
#            API server
#               ↓
#          HTTP response
#               │
#               ├── Status code
#               ├── Headers
#               └── Body
#                        ↓
#                   response.json()
#                        ↓
#                   Python object




# Authorization headers and API keys


# Authorization header
# Many APIs don't allow anyone to call them anonymously. They require some credential to identify or authenticate the caller.
# A common pattern is:
# headers = {
#     "Authorization": "Bearer YOUR_API_KEY"
# }

# response = requests.get(
#     "https://api.example.com/users",
#     headers=headers
# )
# The important part is:
# Authorization: Bearer YOUR_API_KEY


# Your Python program
#        │
#        │ "Here is my credential"
#        ▼
#     API server
#        │
#        ├── credential valid → process request
#        │
#        └── invalid/missing → reject request

# Why Bearer?
# Bearer is an authentication scheme.
# It essentially tells the server:
# "The credential following this word is the bearer token I am presenting."
# So:
# Authorization: Bearer abc123
#                  ↑       ↑
#                scheme   token

# The exact authentication mechanism depends on the API. Other APIs may use API keys in a custom header, 
# Basic authentication, OAuth, etc.
# Very important: don't hard-code secrets
# You should not do this:
# API_KEY = "sk-actual-secret-key-here"
# inside code that might be committed to GitHub.

# Example

# import os

# API_KEY = os.getenv("API_KEY")

# headers = {
#     "Authorization": f"Bearer {API_KEY}"
# }

# Environment variable
#         ↓
#     Python app
#         ↓
#  Authorization header
#         ↓
#      API server

# One useful distinction
# The API key/token and the Authorization header are not the same thing:
# API_KEY
#    ↓
# "abc123"
#    ↓
# f"Bearer {API_KEY}"
#    ↓
# "Bearer abc123"
#    ↓
# Authorization header
# This is the kind of small transformation you should be comfortable tracing because 
# you'll see it constantly when working with LLM APIs and other services.


# Environment variables + API keys + requests

# Python OS Module
# os is Python's standard-library module for interacting with the operating system

# import os
# It gives your Python program ways to interact with things the OS manages, such as:
# environment variables
# files and directories
# paths
# the current working directory
# operating-system information
# processes and other system-level functionality


# Python program
#       ↓
#     os module
#       ↓
# Operating System

# Why did we use it for API keys?
# Earlier:
# API_KEY = os.getenv("API_KEY")
# Here, os.getenv() asks the operating system:
# "Is there an environment variable called API_KEY?"
# For example, suppose your terminal has:
# API_KEY=abc123
# Then:
# import os

# API_KEY = os.getenv("API_KEY")

# print(API_KEY)
# gives:
# abc123
# So the important concept is:
# Environment variable
#         ↓
# Operating system environment
#         ↓
# os.getenv()
#         ↓
# Python variable
# Your Python program isn't magically finding the secret. 
# It is reading a value that has been made available to the process through the OS environment.

# Why is this useful for AI engineering?
# You'll frequently have things like:
# OPENAI_API_KEY
# DATABASE_URL
# REDIS_URL
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY
# You generally don't want these secrets directly inside your source code.
# Instead:
# import os

# api_key = os.getenv("OPENAI_API_KEY")


# One more os example
# You can also ask the OS where your Python program is currently operating:
# import os

# print(os.getcwd())
# getcwd() means get current working directory.
# For example:
# /Users/you/AI-Engineer-Journey/Phase-0/Day-26
# You can also inspect environment variables:
# print(os.environ)
# os.environ behaves roughly like a dictionary containing the environment variables available to your process.
# So:
# os.getenv("API_KEY")
# is essentially a convenient way to retrieve one particular environment variable.
# Important mental model
# Don't think:
# "os means operating system commands."
# Think:
# os is Python's interface to various operating-system facilities.
# We'll encounter it repeatedly as your projects become more sophisticated.




# os + environment variable + requests + authentication

# a small real-world API client

# import os
# import requests

# API_KEY = os.getenv("API_KEY")

# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Accept": "application/json"
# }

# response = requests.get(
#     "https://api.example.com/users",
#     headers=headers
# )

# response.raise_for_status()

# users = response.json()

# print(users)

# Let us trace the program

# Step 1: Read the secret
# API_KEY = os.getenv("API_KEY")
# Python asks the OS environment for API_KEY.
# OS environment
#      │
#      │ API_KEY = "abc123"
#      ▼
# Python
# API_KEY = "abc123"
# Step 2: Construct the headers
# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Accept": "application/json"
# }
# The resulting Python dictionary is conceptually:
# {
#     "Authorization": "Bearer abc123",
#     "Accept": "application/json"
# }
# Step 3: Send the HTTP request
# requests.get(
#     "https://api.example.com/users",
#     headers=headers
# )
# The request now contains:
# GET /users

# Authorization: Bearer abc123
# Accept: application/json
# The server checks the credential and processes the request.
# Step 4: Check for HTTP errors
# response.raise_for_status()
# For example:
# 200 → continue
# 401 → HTTPError
# 403 → HTTPError
# 404 → HTTPError
# 500 → HTTPError
# Step 5: Parse the response
# users = response.json()
# The JSON response becomes a Python object.
# For example:
# [
#   {"id": 1, "name": "Alice"},
#   {"id": 2, "name": "Bob"}
# ]
# becomes:
# [
#     {"id": 1, "name": "Alice"},
#     {"id": 2, "name": "Bob"}
# ]
# So you now have the complete chain:
# OS environment
#      ↓
# os.getenv()
#      ↓
# API key
#      ↓
# HTTP headers
#      ↓
# requests.get()
#      ↓
# API server
#      ↓
# HTTP response
#      ↓
# raise_for_status()
#      ↓
# response.json()
#      ↓
# Python data
# This is a very important AI-engineering pattern. Later, when you call an LLM API, 
# you'll be doing essentially the same thing, just with a more sophisticated API.

# Why do we call:
# response.raise_for_status()
# before
# response.json()
# rather than immediately parsing the JSON?

# raise_for_status() is primarily there to make your program fail explicitly when the HTTP request failed, 
# before you treat the response as successful data.
# Consider:
# response = requests.get(url)

# response.raise_for_status()

# users = response.json()
# Why this order?
# Imagine the server returns:
# 404 Not Found
# It may still send a response body. That body could even contain JSON such as:
# {
#     "error": "User not found"
# }
# So technically, this could work:
# users = response.json()
# But now you've parsed an error response as though it were your normal users data.
# Instead:
# response.raise_for_status()
# checks the HTTP status first.
# HTTP response
#      ↓
# Is status successful?
#      │
#      ├── No → raise HTTPError
#      │
#      └── Yes
#           ↓
#     response.json()
#           ↓
#     normal application data
# So the principle is:
# First establish that the HTTP operation succeeded, then interpret the response body as the expected data.
# And your point about try/except is also correct, but it's a separate concern.
# For example:
# try:
#     response.raise_for_status()
#     users = response.json()
# except requests.HTTPError:
#     print("HTTP request failed")
# Here try/except determines what your program does when an exception occurs.
# raise_for_status() determines whether an HTTP error becomes an exception.
# That's the distinction I want you to keep:
# raise_for_status()
# → detects HTTP failure and raises an exception

# try/except
# → catches an exception and decides how your program responds
# That's an important Python + API mental model.


# A GET request commonly asks the server for data.
# A POST request commonly sends data to the server, often to create something.


# user = {
#     "name": "Alice",
#     "age": 30
# }

# response = requests.post(
#     "https://api.example.com/users",
#     json=user
# )

# Python dictionary
#       ↓
#      json=
#       ↓
# JSON request body
#       ↓
# HTTP POST
#       ↓
# API server

# Conceptually, the request body becomes something like:

# {
#     "name": "Alice",
#     "age": 30
# }

# And requests handles the JSON serialization for you.
# Compare this with our earlier concepts:
# requests.get(
#     url,
#     params={"page": 2}
# )
# Here page=2 goes into the URL query string.
# Whereas:
# requests.post(
#     url,
#     json={"name": "Alice", "age": 30}
# )
# puts the data into the request body.


# So:
# params=  → URL query parameters
# json=    → JSON request body
# headers= → HTTP metadata

# requests.post(
#     "https://api.example.com/users",
#     params={"source": "mobile"},
#     json={"name": "Alice", "age": 30}
# )


# 1. URL 
# You said:
# https://api.example.com/users?source=mobile
# Correct.
# The params dictionary:
# params={"source": "mobile"}
# gets encoded into the query string:
# ?source=mobile
# So:
# Base URL:       https://api.example.com/users
# Query string:   ?source=mobile
# Final URL:      https://api.example.com/users?source=mobile
# 2. Request body 
# Correct.
# json={"name": "Alice", "age": 30}
# represents the data that will be sent in the request body as JSON.
# Conceptually:
# {
#     "name": "Alice",
#     "age": 30
# }
# 3. params , with one refinement
# Your idea of narrowing/constraining the request is good.
# But params aren't necessarily only for filtering/searching.
# They can be used for:
# Filtering       ?country=India
# Searching       ?q=python
# Pagination      ?page=2&limit=10
# Sorting         ?sort=name
# Configuration   ?format=json
# The API contract determines what each parameter actually means.
# So the stronger mental model is:
# Query parameters modify or constrain a request through the URL.
# 4. json 
# Exactly.
# json={"name": "Alice", "age": 30}
# takes the Python object and sends it as a JSON request body.
# requests handles the serialization for you.
# Conceptually:
# Python dict
#     ↓
# JSON serialization
#     ↓
# HTTP request body
# One small terminology improvement: json= itself doesn't simply "convert" the object in isolation. It tells requests:
# "Treat this Python object as JSON data for the request body."


# response = requests.post(
#     "https://api.example.com/users",
#     params={"source": "mobile"},
#     headers={
#         "Authorization": f"Bearer {API_KEY}",
#         "Accept": "application/json"
#     },
#     json={"name": "Alice", "age": 30}
# )


# POST
#  ↓
# Method: "I am submitting data"

# /users
#  ↓
# Path: which API resource/endpoint

# ?source=mobile
#  ↓
# Query: additional request parameter

# Authorization + Accept
#  ↓
# Headers: authentication + desired response format

# {"name": "Alice", "age": 30}
#  ↓
# JSON body: data being submitted

# response.raise_for_status()
# data = response.json()

# Check HTTP result
#       ↓
# If error → raise exception
#       ↓
# If successful → parse response body
#       ↓
# Python object



# dotenv

# If your API_KEY is already an actual environment variable, you only need:
# import os

# API_KEY = os.getenv("API_KEY")
# You do not need dotenv.
# python-dotenv is useful when you want to keep the variables in a local .env file during development.
# Without dotenv
# Suppose you set the environment variable in your terminal:
# export API_KEY="abc123"
# Then:
# import os

# API_KEY = os.getenv("API_KEY")
# works.
# The flow is:
# Terminal / OS environment
#         ↓
#     API_KEY=abc123
#         ↓
#     os.getenv()
#         ↓
#     Python
# No dotenv involved.
# With dotenv
# Suppose instead you have a .env file:
# API_KEY=abc123
# Python does not automatically read .env files.
# So you install python-dotenv and write:
# import os
# from dotenv import load_dotenv

# load_dotenv()

# API_KEY = os.getenv("API_KEY")
# Now the flow is:
# .env file
#    ↓
# load_dotenv()
#    ↓
# environment variables available to process
#    ↓
# os.getenv("API_KEY")
#    ↓
# Python variable
# So your comment:
# "This reads the .env file and injects its keys into the system environment"
# is mostly right, but I'd make it more precise:
# load_dotenv() reads variables from the .env file and loads them into the environment of the current Python process.
# It doesn't permanently modify your operating system's global environment.
# Why have both?
# This is the key distinction:
# from dotenv import load_dotenv
# gives you the function that reads .env.
# load_dotenv()
# actually performs that loading.
# Then:
# os.getenv("API_KEY")
# retrieves the value from the process environment.
# So:
# dotenv
#   │
#   └── load_dotenv()
#           ↓
#       loads .env
#           ↓
#          os
#           │
#           └── getenv("API_KEY")
#                     ↓
#                 "abc123"
# And why is .env useful?
# For local development, you might have:
# .env
# API_KEY=abc123
# DATABASE_URL=postgresql://...
# and:
# .gitignore
# .env
# Therefore your secret stays on your machine and isn't committed to Git.
# For production, you would generally use the deployment environment's 
# secret/environment-variable mechanism rather than relying on a .env file.
# So remember:
# os.getenv() reads an environment variable. load_dotenv() is a 
# development convenience that loads variables from .env into the current process environment.


# In bash terminal
# export API_KEY="abc123"

import os

API_KEYY = os.getenv("API_KEYY")
print()
print(API_KEYY)

# What actually happened?
# Think of your terminal as launching your Python process with some information attached to it:
# Terminal
# │
# ├── PATH=/usr/bin:...
# ├── HOME=/Users/you
# ├── API_KEY=abc123   ← environment variable
# │
# └── starts Python
#        │
#        ↓
#    Python process
#        │
#        └── os.getenv("API_KEY")
#                     ↓
#                  "abc123"

# The key exists in the environment of the running process.
# It doesn't need to exist in:
# your .py file
# your .env file
# requirements.txt
# your source code
# Then what does .env solve?
# Typing this every time:
# export API_KEY="abc123"
# can be inconvenient.
# So developers commonly create:
# .env
# containing:
# API_KEY=abc123
# Then:
# from dotenv import load_dotenv
# load_dotenv()

# import os
# API_KEY = os.getenv("API_KEY")
# load_dotenv() effectively takes the values from .env and makes them available to the current Python process's environment.
# So there are two different ways to get the key into the process:

# WAY 1
# Terminal / deployment system
#         ↓
# Environment variable
#         ↓
# Python
#         ↓
# os.getenv()


# WAY 2
# .env file
#         ↓
# load_dotenv()
#         ↓
# Process environment
#         ↓
# os.getenv()

# And there's an important security point
# An environment variable isn't inherently "more secure" just because it isn't a file.
# The important idea is separating secrets from source code and managing them appropriately.
# For local development:
# .env → load_dotenv() → os.getenv()
# is convenient.




# For production:
# Cloud/hosting secret manager
#           ↓
#      environment
#           ↓
#       os.getenv()
# is much more common.



# So os.getenv() doesn't mean:
# "Go find my API key somewhere."
# It means:
# "Look in this Python process's environment for a variable named API_KEY."
# That is the crucial mental model.

# API error handling.
# We already saw:
# response.raise_for_status()
# Now we combine it with try/except.
# import requests

# try:
#     response = requests.get(url)
#     response.raise_for_status()

#     data = response.json()
#     print(data)

# except requests.HTTPError as e:
#     print("HTTP error:", e)

# except requests.RequestException as e:
#     print("Request failed:", e)
# There are two useful levels here.
# 1. HTTPError
# This handles HTTP responses where the server returned an error status such as:
# 401
# 403
# 404
# 500
# because raise_for_status() converts those HTTP error responses into an exception.
# 2. RequestException
# This is broader. It covers errors raised by the requests library itself, including HTTP-related exceptions.
# Think:
# requests.get()
#      │
#      ├── Couldn't communicate properly
#      │       ↓
#      │   RequestException
#      │
#      └── Got HTTP response
#              │
#              ├── 200 → continue
#              │
#              └── 404 → raise_for_status()
#                          ↓
#                      HTTPError
# One subtle point: HTTPError is a subclass of RequestException, so if you put the broader one first:
# except requests.RequestException:
# it would catch the HTTPError too. That's why the more specific exception is normally placed first.
# Tiny exercise
# Given:
# try:
#     response = requests.get(url)
#     response.raise_for_status()

# except requests.HTTPError:
#     print("HTTP error")

# except requests.RequestException:
#     print("Other request error")
# If the server returns 404, which except block executes?

# Your reasoning is correct, including the important point about specific before generic.
# except requests.HTTPError:
#     print("HTTP error")

# except requests.RequestException:
#     print("Other request error")
# With a 404:
# 404 response
#      ↓
# raise_for_status()
#      ↓
# HTTPError raised
#      ↓
# Python checks except blocks from top to bottom
#      ↓
# HTTPError matches
#      ↓
# "HTTP error"
# It never reaches the second except.
# And as you correctly said, if we reversed them:
# except requests.RequestException:
#     print("Other request error")

# except requests.HTTPError:
#     print("HTTP error")
# the broader RequestException would catch the HTTPError first, making the second block effectively unreachable for that exception.
# The general Python rule
# This isn't specific to requests.
# When using multiple except blocks:
# Put more specific exceptions before broader exceptions.
# For example:
# try:
#     ...
# except ValueError:
#     ...
# except Exception:
#     ...
# ValueError is more specific; Exception is broader.


# Mini API client

# First, imagine we want a function:
# def get_user(user_id: int):
#     ...
# Its job is:
# user_id
#    ↓
# construct API URL
#    ↓
# send GET request
#    ↓
# check HTTP status
#    ↓
# parse JSON
#    ↓
# return Python data
# Before we write it, one final conceptual question:
# If our function is:
# def get_user(user_id: int):
# and we want to request user 123 from:
# https://api.example.com/users/123
# what part of the URL is determined by user_id?


# user_id determines the path value:
# https://api.example.com/users/123
#                               ↑
#                            user_id
# So inside the function, we'd construct it with an f-string:
# def get_user(user_id: int):
#     url = f"https://api.example.com/users/{user_id}"
# If:
# get_user(123)
# then:
# url = "https://api.example.com/users/123"
# Notice how the Python argument flows directly into the URL:
# get_user(123)
#      ↓
# user_id = 123
#      ↓
# f".../users/{user_id}"
#      ↓
# https://api.example.com/users/123


# Now let's add the request
# def get_user(user_id: int):
#     url = f"https://api.example.com/users/{user_id}"

#     response = requests.get(url)

#     response.raise_for_status()

#     return response.json()


# This is already a legitimate basic API client function.


# Trace it:
# get_user(123)
#       ↓
# construct URL
#       ↓
# requests.get(url)
#       ↓
# Response object
#       ↓
# raise_for_status()
#       ↓
# response.json()
#       ↓
# Python object returned
# One thing is missing
# Our API might require authentication.

# So we could add:
# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Accept": "application/json"
# }

# and then:

# response = requests.get(url, headers=headers)
# Now the function is becoming much closer to the sort of code you'll encounter when working with real APIs.
# Next, we'll put the environment variable, authentication, error handling, and function together into one small client, '
# 'and then you'll trace it yourself.


# Small API client program

# import os
# import requests

# API_KEY = os.getenv("API_KEY")

# def get_user(user_id: int):
#     url = f"https://api.example.com/users/{user_id}"

#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Accept": "application/json"
#     }

#     try:
#         response = requests.get(
#             url,
#             headers=headers
#         )

#         response.raise_for_status()

#         return response.json()

#     except requests.HTTPError as e:
#         print("HTTP error:", e)

#     except requests.RequestException as e:
#         print("Request failed:", e)


# Trace this Small API client program
# Suppose:
# API_KEY = "abc123"
# and we call:
# user = get_user(123)
# 1. Function receives the argument
# get_user(123)
#      ↓
# user_id = 123
# 2. URL is constructed
# https://api.example.com/users/123
# 3. Headers are constructed
# {
#     "Authorization": "Bearer abc123",
#     "Accept": "application/json"
# }
# 4. requests.get() sends the request
# GET /users/123

# Authorization: Bearer abc123
# Accept: application/json
# 5. Server responds
# Suppose it returns:
# 200 OK
# 6. raise_for_status()
# response.raise_for_status()
# Nothing happens because 200 is successful.
# 7. Parse JSON
# response.json()
# Suppose the body is:
# {
#     "id": 123,
#     "name": "Alice"
# }
# It becomes a Python dictionary:
# {
#     "id": 123,
#     "name": "Alice"
# }
# 8. Return it
# return response.json()
# Therefore:
# user = get_user(123)
# results in:
# user == {
#     "id": 123,
#     "name": "Alice"
# }
# Now the important failure path
# Suppose the server returns:
# 401 Unauthorized
# Then:
# requests.get()
#      ↓
# Response(401)
#      ↓
# raise_for_status()
#      ↓
# HTTPError
#      ↓
# except requests.HTTPError
#      ↓
# print("HTTP error:", e)
# The return response.json() line is never reached.


# Trace for user id 456 assuming that the server returns 404 error
# in the same small client program code

# 456
#  ↓
# user_id = 456
#  ↓
# URL = ".../users/456"
#  ↓
# Authorization = "Bearer xyz789"
#  ↓
# GET request
#  ↓
# Server
#  ↓
# 404 Not Found
#  ↓
# Response object with status_code = 404
#  ↓
# raise_for_status()
#  ↓
# HTTPError
#  ↓
# except requests.HTTPError
#  ↓
# print error
#  ↓
# function ends
#  ↓
# returns None implicitly

# Day 26: Mini Exercise

# Write a function def get_user(user_id: int):
# It should:
# Read the API key from the environment.
# Construct the URL using user_id.
# Create an Authorization header using the Bearer scheme.
# Make a GET request.
# Raise an exception if the HTTP request returns an error status.
# Parse the response JSON.
# Return the resulting Python object.
# Catch an HTTP error and print it.

import os
import requests

API_KEY = os.getenv("API_KEY")


def get_user(user_id: int):
    url = f"https://api.example.com/users/{user_id}"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data

    except requests.HTTPError as e:
        print("HTTP error:", e)

# os.getenv()
#      ↓
# API key
#      ↓
# Authorization header
#      ↓
# GET request
#      ↓
# URL path /users/{user_id}
#      ↓
# Response object
#      ↓
# raise_for_status()
#      ↓
# HTTPError if needed
#      ↓
# response.json()
#      ↓
# Python object
#      ↓
# return


# One small engineering note
# Your function catches only:
# except requests.HTTPError
# That's perfectly fine for what we practiced.
# Later, for production-quality API clients, we can also handle things such as:
# network failures
# timeouts
# connection errors
# malformed JSON
# missing API keys
# We don't need to add all of that now. The goal of Day 26 was to establish the core API mental model first.