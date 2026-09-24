# Day 30: Python Engineering Mini-Project


# Project: CLI API Data Explorer
# To build a small command-line application that takes a 
# user ID, calls an HTTP API, processes the JSON response, and displays useful information

# Application logic / CLI entry-point logic


from api_client import get_user
import sys
import logging

logging.basicConfig(level=logging.INFO)

print()
print("Project: CLI API Data Explorer")
print()

# Part 1: CLI

def main():

    # cli argument validation
    
    if len(sys.argv) != 3:
        print("Usage: python app.py <resource> <id>")
        print()
    else:
        resource = sys.argv[1]
        try:
            resource_id = int(sys.argv[2])
        except ValueError:
            print("Resource ID must be an integer")
        else:
            # user is one resource type, and post and todo are other resource types exposed by the same API
            # Part 3: Connecting CLI and API Client and fetching the data from API

            if resource == "user":
                # print("Resource: ", resource)
                # print("ID: ", resource_id)
                data = get_user(resource_id)
                # Part 4: Error handling from CLI and response (None from HTTP Error)
                # When a function can fail, the caller needs to know how failure is represented
                # guarding against an invalid/missing result
                # print(data)
                # print(type(data))
                if data is None:
                    print("Check whether the user id typed is correct!")
                    # return
                else:
                    print("User ID: ", data["id"])
                    print("Name: ", data["name"])
                    print("User Name: ", data["username"])
                    print("Email: ", data["email"])
            else:
                print("Check whether the resource typed is correct!")


# If this file is being run directly, execute main()
if __name__ == "__main__":
    main()