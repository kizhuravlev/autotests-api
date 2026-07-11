import httpx
from httpx_module.tools.fakers import fake
from httpx_module.tools.urls import (
    BASE_URL,
    AUTH_ROUTE,
    USERS_ROUTE
)

create_user_payload = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(f"{BASE_URL}{USERS_ROUTE}", json=create_user_payload)
create_user_response.raise_for_status()
print(f"Status code: {create_user_response.status_code}")

login_user_payload = {
  "email": create_user_payload["email"],
  "password": create_user_payload["password"]
}

login_user_response = httpx.post(f"{BASE_URL}{AUTH_ROUTE}/login", json=login_user_payload)
login_user_response.raise_for_status()
print(f"Status code: {login_user_response.status_code}")


user_id = create_user_response.json()["user"]["id"]
token = login_user_response.json()["token"]["accessToken"]

delete_user_headers = {
    "Authorization": f"Bearer {token}"
}

delete_user_response = httpx.delete(f"{BASE_URL}{USERS_ROUTE}/{user_id}", headers=delete_user_headers)
delete_user_response.raise_for_status()
print(f"Status code: {delete_user_response.status_code}")