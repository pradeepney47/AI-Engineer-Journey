# Day 30: Python Engineering Mini-Project
# Project: CLI API Data Explorer
#
# Application logic / CLI entry-point logic

import asyncio
import logging
import sys

from api_client import APIError, NetworkError, get_user, get_users


logging.basicConfig(level=logging.INFO)


def main():
    print()
    print("Project: CLI API Data Explorer")
    print()

    if len(sys.argv) < 3:
        user_message()
        return

    resource = sys.argv[1]

    if resource == "user":
        if len(sys.argv) > 3:
            user_message()
            return

        try:
            resource_id = int(sys.argv[2])
        except ValueError:
            print("Resource ID must be an integer")
            return

        try:
            data = get_user(resource_id)
        except NetworkError:
            print("Check your network connection!")
            return
        except APIError:
            print("The API request failed!")
            return

        if data is None:
            print("Check whether the user ID typed is correct!")
            return

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

        data = asyncio.run(get_users(user_ids))

        for user_id, user in zip(user_ids, data):
            # isinstance(object, type)
            # isinstance() is a built-in Python function used to check an object's type.
            # Is user an instance of NetworkError?
            # isinstance(what_object, what_type)
            # object → user
            # type   → NetworkError
            # help(isinstance)
            # x = 10
            # isinstance(x, int)
            # isinstance(x, str)
            
            if isinstance(user, NetworkError):
                print(
                    f"Could not retrieve user {user_id}. "
                    "Check your network connection!"
                )
                continue

            if isinstance(user, APIError):
                print(f"API request failed for user {user_id}!")
                continue

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