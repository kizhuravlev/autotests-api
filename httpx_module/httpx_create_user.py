import httpx
from httpx_module.tools.fakers import random_user_email

payload = {
  "email": random_user_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

user_create_response = httpx.post('http://127.0.0.1:8000/api/v1/users', json=payload)

print(user_create_response.status_code)
print(user_create_response.json())