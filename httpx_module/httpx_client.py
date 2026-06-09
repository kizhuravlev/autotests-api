import httpx

login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post('http://127.0.0.1:8000/api/v1/authentication/login', json=login_payload)
login_response.raise_for_status()

client = httpx.Client(
    base_url='http://127.0.0.1:8000',
    timeout=100,
    headers={"Authorization": f"Bearer {login_response.json()['token']['accessToken']}"}
    )

me_response = client.get("/api/v1/users/me")
me_response.raise_for_status()
print(f"Me data: {me_response.json()}")