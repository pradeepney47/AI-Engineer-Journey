# Part 2: API Client
# API client logic

import logging
# import asyncio

import requests

def get_user(user_id: int) -> dict:
    logging.info("Fetching user %s", user_id)
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # API endpoint to fetch a specific user from users resource type path
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        logging.error("HTTP Error: %s", e)
        return None

    except requests.ConnectTimeout as e:
        logging.error("Connection Timeout: %s", e)
        return None
        
    except requests.ConnectionError as e:
        logging.error("Connection Error: %s", e)
        return None

    except requests.RequestException as e:
        logging.error("Request Failed: %s", e)
        return None


def get_users(user_ids: list[int]) -> list:
    user_collection = []
    for user_id in user_ids:
        # try:
        # user_collection += [get_user(user_id)]
        user_collection.append(get_user(user_id))
        # except requests.HTTPError:
        #     print(f"User ID {user_id} does not exist!")
        #     continue
    return user_collection