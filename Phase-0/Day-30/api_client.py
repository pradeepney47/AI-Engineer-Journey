# Day 30: Python Engineering Mini-Project
# Part 2: API Client
#
# API communication and API error handling

import asyncio
import logging

import requests


class NetworkError(Exception):
    """Raised when the client cannot communicate with the server."""
    pass


class APIError(Exception):
    """Raised when an API request fails for an unexpected reason."""
    pass


def get_user(user_id: int) -> dict | None:
    logging.info("Fetching user %s", user_id)

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    except requests.HTTPError as e:
        logging.error("HTTP Error: %s", e)
        return None

    except requests.ConnectTimeout as e:
        logging.error("Connection Timeout: %s", e)
        raise NetworkError("Could not connect to the server") from e

    except requests.ConnectionError as e:
        logging.error("Connection Error: %s", e)
        raise NetworkError("Could not connect to the server") from e

    except requests.RequestException as e:
        logging.error("Request Failed: %s", e)
        raise APIError("API request failed") from e


async def get_users(
    user_ids: list[int],
) -> list[dict | None | NetworkError | APIError]:

    tasks = [
        asyncio.to_thread(get_user, user_id)
        for user_id in user_ids
    ]

    results = await asyncio.gather(
        *tasks,
        return_exceptions=True,
    )

    return results