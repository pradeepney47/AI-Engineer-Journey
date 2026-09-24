# Part 2: API Client
# API client logic

import logging
import asyncio

import requests

def get_user(user_id: int) -> dict:
    logging.info("Fetching user %s", user_id)
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # API endpoint to fetch a specific user from users resource type path
    try:
        response = requests.get(url)
        # checks the status code and raises the appropriate exception (raises HTTPError when one occurs)
        response.raise_for_status()
        print(response.headers["Content-Type"])
        return response.json()
    # Part 4: Error handling from requests and response
    except requests.HTTPError as e:
        # print() is User-facing output
        # print("HTTP Error:", e)
        # Part 5: Logging 
        # logging is Developer/application diagnostics
        logging.error("HTTP Error: %s", e)
        return None

    except requests.ConnectTimeout as e:
        # print("Connection Timeout:", e)
        # Part 5: Logging
        logging.error("Connection Timeout: %s", e)
        return None
        
    except requests.ConnectionError as e:
        # print("Connection Error:", e)
        # Part 5: Logging
        logging.error("Connection Error: %s", e)
        return None

    except requests.RequestException as e:
        # print("Request Failed:", e)
        # Part 5: Logging
        logging.error("Request Failed: %s", e)
        return None


async def get_users(user_ids: list[int]):
    tasks = [
        asyncio.to_thread(get_user, user_id)
        for user_id in user_ids
    ]

    return await asyncio.gather(*tasks)