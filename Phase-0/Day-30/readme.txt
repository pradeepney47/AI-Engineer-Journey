# Day 30: Python Engineering Mini-Project
# Project: CLI API Data Explorer

# To build a small command-line application that takes a 
# user ID, calls an HTTP API, processes the JSON response, and displays useful information


# Terminal
#    │
#    │ python app.py user 1
#    ▼
# Python CLI
#    │
#    ▼
# API client
#    │
#    │ HTTP request
#    ▼
# External API
#    │
#    │ JSON response
#    ▼
# Python
#    │
#    ├── validate
#    ├── process
#    └── display
#    ▼
# Terminal

# Example

# python app.py user 1

# could eventually produce

# User ID: 1
# Name: Leanne Graham
# Username: Bret
# Email: Sincere@april.biz

# Phase 0 Python concepts itegration is the goal through this project:

# Python fundamentals
#       ↓
# Functions
#       ↓
# OOP
#       ↓
# Modules / packages
#       ↓
# Type hints
#       ↓
# Virtual environments
#       ↓
# Dependencies
#       ↓
# HTTP + requests
#       ↓
# JSON
#       ↓
# Environment variables
#       ↓
# Error handling
#       ↓
# Logging
#       ↓
# Testing
#       ↓
# Debugging

# and asyncio


# Parts of the Project

# Part 1
# Project structure and CLI input

CLI input
   ↓
sys.argv
   ↓
argument count validation
   ↓
value validation
   ↓
usable Python values


# Part 2 (Now we connect our CLI to an actual API)
# API client

python app.py user 1
        ↓
    Python app
        ↓
    HTTP GET request
        ↓
      API
        ↓
    JSON response
        ↓
    Python dict



main()
  │
  │ user_id = 1
  ↓
get_user(user_id)
  │
  │ HTTP request
  ↓
API
  │
  │ HTTP response
  ↓
JSON / other response body
  ↓
get_user() returns Python data
  ↓
main() displays it






python app.py user 1
        ↓
sys.argv
        ↓
resource = "user"
resource_id = 1
        ↓
get_user(1)
        ↓
URL becomes
https://jsonplaceholder.typicode.com/users/1
        ↓
requests.get(url)
        ↓
Response object
        ↓
response.json()
        ↓
Python dict
        ↓
data
        ↓
print(data)



API
├── /users
├── /posts
├── /todos
├── /comments
├── /albums
└── /photos


For https://jsonplaceholder.typicode.com/users users is the API endpoint we are working on

this is why we use if resource == "user":

For https://jsonplaceholder.typicode.com/posts users is the API endpoint we are working on
we use if resource == "post":

/users, /posts, /todos are endpoints

More precisely, an endpoint is an API-accessible URL + HTTP method combination.

GET /users
GET /users/1
GET /posts
GET /posts/1
GET /todos
GET /todos/1
These are individual endpoints.

So:

/users
is a resource path or collection path, while:

GET /users
is an endpoint.

And:

GET /users/1
is another endpoint.


API
│
├── GET /users
│      → collection of users
│
├── GET /users/1
│      → one specific user
│
├── GET /posts
│      → collection of posts
│
├── GET /posts/1
│      → one specific post
│
└── GET /todos/1
       → one specific todo



The HTTP method matters.
For example, conceptually:
GET    /users/1   → retrieve user
POST   /users     → create user
PUT    /users/1   → replace/update user
DELETE /users/1   → delete user

Same path, different HTTP method, different endpoint/operation.

This distinction will become important when we build FastAPI later, 
because you'll be defining these routes yourself:

@app.get("/users/{user_id}")

At that point you'll move from:

"I'm consuming someone else's API."
to:

"I'm building an API for someone else to consume."
That's a major transition in your AI Engineer journey.



API
│
├── Resource types
│   ├── users
│   ├── posts
│   └── todos
│
└── Endpoints
    ├── GET /users
    ├── GET /users/1
    ├── GET /posts/1
    └── GET /todos/1


And our CLI:
python app.py user 1
is our application's interface, which we translate into:
user + 1
   ↓
GET /users/1
   ↓
HTTP response
   ↓
JSON
   ↓
Python dict




# Part 3
# JSON parsing and data extraction

We now have a complete data transformation chain:

CLI argument
"1"
   ↓ int()
1
   ↓
get_user(1)
   ↓
HTTP GET /users/1
   ↓
JSON response
   ↓ response.json()
Python dict
   ↓ ["name"]
"Leanne Graham"



# Part 4
# Error handling

GET /users/9999
       ↓
server
       ↓
HTTP 404 response
       ↓
requests.get() returns a Response object
       ↓
response.raise_for_status()
       ↓
HTTPError raised



get_user(resource_id)
        ↓
   ┌────┴────┐
   ↓         ↓
dict       None
   ↓         ↓
display    message
fields     + return


Two different failure points
1. We successfully communicate with the server, but the server says something went wrong:
GET /users/9999
       ↓
Server responds
       ↓
404 Not Found
       ↓
HTTPError


2. We cannot successfully complete the HTTP communication:
GET /users/1
       ↓
Network/DNS/connection/timeout problem
       ↓
No usable HTTP response
       ↓
RequestException


And remember the class relationship
Catch the most specific exception first, then progressively broader exceptions.
Otherwise, if a broad parent catches an exception first, Python never reaches the more specific handler below it

RequestException
├── HTTPError
├── ConnectionError
│   └── ConnectTimeout
└── Timeout


So we can handle them
print() is fine for user-facing CLI output


# Part 5
# Logging

User-facing output → print()
Developer/application diagnostics → logging

Logging is better for diagnostics because it gives us levels and timestamps and can later 
write to files or monitoring systems

DEBUG    detailed developer information
INFO     normal application events
WARNING  something unexpected, but application can continue
ERROR    an operation failed
CRITICAL serious failure

The logging level is a minimum severity threshold.
If this is the configuraiton 
logging.basicConfig(level=logging.WARNING)
then WARNING means "show WARNING and anything more severe."


Then main() can continue to handle user-facing output with print().
One subtle point: basicConfig() is normally intended as application-level configuration, 
not something each module should independently configure. Later, when we split this project into multiple files, we'll use the more professional pattern with:

logger = logging.getLogger(__name__)

and configure logging centrally in the application entry point.
For Day 30, though, logging.basicConfig(level=logging.INFO) at the top of app.py is exactly what you need.




# Part 6
# Testing

"I can automatically verify that a piece of my program behaves correctly."


Our first candidate is:
def get_user(user_id: int):
    ...

But there's a problem.

If our test calls the real API every time, then our test depends on:

Internet connection
API availability
API response
network latency

That's not ideal. So before we write a test, we need to learn one concept: mocking an external dependency.

Create test_app.py and write test code

from app import get_user

def test_get_user():
    data = get_user(1)
    
    assert data["id"] == 1

and then run pytest 

pytest
  ↓
test_get_user()
  ↓
get_user(1)
  ↓
requests.get(...)
  ↓
external API
  ↓
JSON
  ↓
dict
  ↓
assert
  ↓
PASSED

How do we test get_user() without depending on the real internet?

Mocking..

For a unit test, we'd rather control the API response ourselves.

Mocking

A mock is a controlled stand-in for a real dependency.

Instead of:

test
 ↓
get_user()
 ↓
real requests.get()
 ↓
Internet
 ↓
JSONPlaceholder


We want:

test
 ↓
get_user()
 ↓
mock requests.get()
 ↓
fake response

Now our test doesn't need the internet.

First, understand the substitution

Our production code contains:

response = requests.get(url)

During the test, we want to temporarily replace:

requests.get

with something we control.

Python's standard library already provides mocking:

from unittest.mock import patch

No pip install needed.


mock_get
   ↓
stands in for requests.get

mock_get.return_value
   ↓
stands in for the Response object

fake_response.json.return_value
   ↓
stands in for the data returned by response.json()


So our test execution becomes:
get_user(1)
   ↓
requests.get(url)
   ↓
mock_get(url)
   ↓
fake_response
   ↓
fake_response.json()
   ↓
{
    "id": 1,
    ...
}

One more important piece
We haven't configured:
fake_response.raise_for_status()
And that's okay for this test, because calling an unconfigured mock method does not raise an exception.

So our test can now run without touching the internet.

Run:
pytest

and tell me whether it passes. Then we'll make the mock verify that requests.get() 
was called correctly, which is where mocking becomes much more useful.



What you've learned
You now have the basic testing model:
Production code
     │
     ├── depends on → external API
     │
     ↓
   Mock it
     │
     ├── control the fake response
     ├── test returned data
     └── verify dependency interaction
That distinction between testing output and testing interactions with dependencies is 
important in real backend and AI engineering.


You have now tested the complete CLI → application flow without touching the real API:


CLI input
   ↓
fake sys.argv
   ↓
main()
   ↓
fake get_user()
   ↓
assert get_user(1) was called






1. Test real function
       ↓
2. Mock external API
       ↓
3. Control fake response
       ↓
4. Test successful response
       ↓
5. Test HTTP error path
       ↓
6. Verify dependency calls
       ↓
7. Mock CLI input
       ↓
8. Test main() flow





# Part 7
# Refactoring into a clean project structure

Day-30/
├── app.py
├── test_app.py
├── requirements.txt
└── .venv/

As the application grows, this becomes harder to maintain. We already have two distinct responsibilities:

CLI/application flow

API communication

So let's separate them.


app.py
  │
  │ imports
  ↓
api_client.py
  │
  │ requests.get()
  ↓
External API

app.py → application/CLI logic
api_client.py → HTTP/API communication


app.py
│
│  Application logic
│  "What does the user want?"
│  "What should we do with the result?"
│
↓
api_client.py
│
│  External API communication
│  "How do I call the API?"
│
↓
JSONPlaceholder API




Why app.py isn't server logic?

A server is something that listens for incoming requests.
For example, later with FastAPI:

React
   │
   │ HTTP request
   ↓
FastAPI server
   │
   ↓
Python application logic
   │
   ↓
External APIs / Database / LLM


FastAPI would expose an HTTP endpoint such as:
GET /users/1

and your Python application would respond to incoming requests.
Our current app.py doesn't do that.

It is simply:

Terminal
   ↓
app.py

The terminal starts the program. app.py reads sys.argv, decides what to do, 
calls api_client.py, and prints the result.



The distinction to remember

Module	            Role
app.py	            Application / CLI entry point
api_client.py	      Client for an external API
JSONPlaceholder	   External API server
FastAPI, later	      Our API server


And this connects directly to what we discussed earlier:

Client and server describe roles in a communication relationship.

Later, your FastAPI application will be a server when React calls it, but simultaneously a client when 
it calls an LLM API or another external service.
So one application can absolutely be both a server and a client, depending on which side of the communication 
you're looking at.


The key is that "client" and "server" are roles in a particular communication relationship, not permanent identities of a file or application.
For your future Nutrition Agent:

React frontend
     │
     │ HTTP request
     ▼
FastAPI backend
     │
     │ application logic
     ├──────────────► PostgreSQL
     │
     ├──────────────► LLM API
     │
     └──────────────► Nutrition API
Here:
React = client to FastAPI
FastAPI = server to React
FastAPI/application = client to PostgreSQL/LLM/nutrition APIs
PostgreSQL / LLM API / Nutrition API = servers from your application's perspective
And you can separate the code:
backend/
├── main.py
├── api/
│   └── routes.py          ← HTTP server/API boundary
├── services/
│   └── nutrition.py       ← application/domain logic
├── clients/
│   ├── llm_client.py      ← external API client
│   └── nutrition_client.py
└── database/
    └── ...
So FastAPI is not synonymous with "backend logic." It is primarily the HTTP/API layer through which your 
application exposes functionality.
This distinction will become very useful when we reach FastAPI and AI backends later in the journey.






# Part 8
# Small async improvement







# Part 9
# Final review








Async from fresh eyes
Why synchronous get_users() waits
What async actually changes
asyncio.to_thread()
asyncio.gather()
Trace our actual user IDs through the async flow
Integrate it into the project
Error handling
api_client.py: network/API failures
app.py: invalid input/application-level failures
Test with internet available
Test with internet unavailable
Decide which layer should handle what
Code structure
Input validation → routing → execution → result handling → presentation
Examine whether our current main() follows that natural flow
Refactor only where it genuinely improves clarity
Testing from fresh eyes
Unit tests
Mocking HTTP
Testing success/failure paths
Testing async behavior
Project review
Python engineering concepts we actually used
Architecture and separation of concerns
What we learned from the project
Final cleanup
Naming
Type hints
Comments/docstrings where useful
README/documentation if needed
Final run and tests