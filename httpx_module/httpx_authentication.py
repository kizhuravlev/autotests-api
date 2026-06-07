import httpx

BASE_URL = 'http://127.0.0.1:8000/api/v1/authentication'

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

login_response = httpx.post(f"{BASE_URL}/login", json=login_payload)
login_response_data = login_response.json()
print(f"Login response: {login_response_data}")
print(f"Status code: {login_response.status_code}")

refresh_payload = {
    "refreshToken" : login_response_data['token']['refreshToken']
}

refresh_response = httpx.post(f"{BASE_URL}/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()
print(f"Refresh response: {refresh_response_data}")
print(f"Status code: {refresh_response.status_code}")