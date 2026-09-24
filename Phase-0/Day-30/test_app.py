
from unittest.mock import patch
from app import get_user, main
import requests


# @patch("app.requests.get")
@patch("api_client.requests.get")
def test_get_user(mock_get):
    fake_response = mock_get.return_value

    fake_response.json.return_value = {
        "id": 1,
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com"
    }

    data = get_user(1)

    mock_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    assert data["id"] == 1


# @patch("app.requests.get")
@patch("api_client.requests.get")
def test_get_user_not_found(mock_get):
    fake_response = mock_get.return_value

    fake_response.raise_for_status.side_effect = requests.HTTPError(
        "404 Client Error"
    )

    data = get_user(999)

    assert data is None


# @patch("app.get_user")
# @patch("sys.argv", ["app.py", "user", "1"])
@patch("app.get_user")
@patch("sys.argv", ["app.py", "user", "1"])
def test_main(mock_get_user):
    mock_get_user.return_value = {
        "id": 1,
        "name": "Test User",
        "username": "testuser",
        "email": "test@example.com"
    }

    main()

    mock_get_user.assert_called_once_with(1)


# # Not Mocking Test but test with external API
# import asyncio

# from api_client import get_users


# def test_get_users():
#     result = asyncio.run(get_users([1, 2, 3]))

#     assert len(result) == 3
#     assert result[0]["id"] == 1
#     assert result[1]["id"] == 2
#     assert result[2]["id"] == 3


import asyncio
from unittest.mock import patch

from api_client import get_users


@patch("api_client.get_user")
def test_get_users(mock_get_user):
    mock_get_user.side_effect = [
        {"id": 1, "name": "User 1"},
        {"id": 2, "name": "User 2"},
        {"id": 3, "name": "User 3"},
    ]

    result = asyncio.run(get_users([1, 2, 3]))

    assert len(result) == 3
    assert result[0]["id"] == 1
    assert result[1]["id"] == 2
    assert result[2]["id"] == 3