import requests
# import json

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
print()
print(type(response))
print()
print(response.status_code)
print()
print(type(response.text))
print()
print(response.text)
print()
print(response)
print()
print(type(response.headers))
print()
print(response.headers["Content-type"]) # we can see the HTTP response format for the body is JSON
print()
print(response.headers)
# data = json.loads(response.text) # this is same as  saying data = response.json()

# data = json.loads(response.text) # converts JSON string to Python object (dictionary)
# data = response.json() # convinently converts JSON string to Python object (dictionary)

# 1. json.loads(response.text) versus 2. response.json()

# 1. json.loads(response.text) 

# response.text
#       ↓
# JSON string
#       ↓
# json.loads()
#       ↓
# Python dict

# 2. response.json()

# response.json()
#       ↓
# Python dict


data = response.json()

print()
print(type(data))
print()
print(data)

# HTTP is the communication protocol. JSON is one possible representation of the data being transmitted.
# And requests does NOT automatically convert every response into a Python object

