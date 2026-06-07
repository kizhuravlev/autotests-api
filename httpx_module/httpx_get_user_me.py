import httpx

BASE_URL = 'http://127.0.0.1:8000/api/v1'

AUTH_ROUTE = '/authentication'
USERS_ROUTE = '/users'


login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post(f'{BASE_URL}{AUTH_ROUTE}/login', json=login_payload)
access_token = login_response.json()['token']['accessToken']

me_headers = {
    "Authorization": f"Bearer {access_token}"
}

me_response = httpx.get(f'{BASE_URL}{USERS_ROUTE}/me', headers=me_headers)
print(f"Me response: {me_response.json()}")
print(f"Status code: {me_response.status_code}")
