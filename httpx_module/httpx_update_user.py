import httpx
from httpx_module.tools.fakers import random_user_email
from httpx_module.tools.urls import (
    BASE_URL,
    AUTH_ROUTE,
    USERS_ROUTE
)

create_user_payload = {
  "email": random_user_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(f"{BASE_URL}{USERS_ROUTE}", json=create_user_payload)
create_user_response.raise_for_status()
print(f"Status code: {create_user_response.status_code}")
print(f"Response payload: {create_user_response.json()}")

login_user_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_user_response = httpx.post(f"{BASE_URL}{AUTH_ROUTE}/login", json=login_user_payload)
login_user_response.raise_for_status()
print(f"Status code: {login_user_response.status_code}")
print(f"Response payload: {login_user_response.json()}")

user_id = create_user_response.json()["user"]["id"]

update_user_headers = {
    "Authorization": f"Bearer {login_user_response.json()['token']['accessToken']}"
}

update_user_payload = {
  "email": random_user_email(),
  "lastName": "newString",
  "firstName": "newString",
  "middleName": "newString"
}

update_user_response = httpx.patch(f"{BASE_URL}{USERS_ROUTE}/{user_id}", headers=update_user_headers, json=update_user_payload)
update_user_response.raise_for_status()
print(f"Status code: {update_user_response.status_code}")
print(f"Response payload: {update_user_response.json()}")