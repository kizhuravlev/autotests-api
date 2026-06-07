import httpx
from httpx_module.tools.fakers import random_user_email
from httpx_module.tools.urls import (
    BASE_URL,
    USERS_ROUTE,
    AUTH_ROUTE
)

create_user_payload = {
  "email": random_user_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(f'{BASE_URL}{USERS_ROUTE}', json=create_user_payload)
create_user_response.raise_for_status()
create_user_response_data = create_user_response.json()
print(f"Status code: {create_user_response.status_code}")

login_user_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_user_response = httpx.post(f'{BASE_URL}{AUTH_ROUTE}/login', json=login_user_payload)
login_user_response.raise_for_status()
login_user_response_data = login_user_response.json()
print(f"Status code: {login_user_response.status_code}")

user_id = create_user_response_data["user"]["id"]

get_user_headers = {
    "Authorization": f"Bearer {login_user_response_data['token']['accessToken']}"
}

get_user_response = httpx.get(f"{BASE_URL}{USERS_ROUTE}/{user_id}", headers=get_user_headers)
get_user_response.raise_for_status()
print(f"Status code: {get_user_response.status_code}")
print(f"User data: {get_user_response.json()}")