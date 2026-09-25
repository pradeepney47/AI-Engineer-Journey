# Day 30: Python Engineering Mini-Project

# Project: CLI API Data Explorer
# To build a small command-line application that takes a 
# user ID, calls an HTTP API, processes the JSON response, and displays useful information

# Application logic / CLI entry-point logic

from api_client import get_user, get_users
import sys
import logging
# import asyncio

logging.basicConfig(level=logging.INFO)

print()
print("Project: CLI API Data Explorer")
print()

def main():

    if len(sys.argv) < 3:
        user_message()
        return
    
    resource = sys.argv[1]
    
    if resource == "user":
    
        if len(sys.argv) > 3:
            user_message()
            return
    
        else:
            try:
                resource_id = int(sys.argv[2])

            except ValueError:
                
                print("Resoruce ID must be an integer")
                return
    
            else:

                data = get_user(resource_id)
    
                if data is None:
                    print("Check whether the user ID typed is correct!")
                    return
    
                else:
                    print("User ID:", data["id"])
                    print("Name:", data["name"])
                    print("Username:", data["username"])
                    print("Email:", data["email"])
    
    elif resource == "users":
        try:
            user_ids = [int(value) for value in sys.argv[2:]]
        except ValueError:
            print("All user IDs must be integers")
            return
    
        else:

            data = get_users(user_ids)
            # print(type(data))
            # print(type(data[0]))
            # print()
            # print(data)
            # print()

            for user_id, user in zip(user_ids, data):
                
                if user is None:
                    print()
                    print(f"User ID {user_id} does not exist!")
                    continue

                print()
                print("User ID:", user["id"])                    
                print("Name:", user["name"])
                print("Username:", user["username"])
                print("Email:", user["email"])
    
    else:
        print("Unknown resource")

def user_message():
    print("Usage: python app.py user <id>")
    print("       python app.py users <id1> <id2> ... <idN>")
    print()

if __name__ == "__main__":
    main()
