from httpx import Client

from httpx_module.clients.auth.auth_client import get_auth_client, LoginRequestDict

def get_private_http_client(user: LoginRequestDict) -> Client:
    
    auth_client = get_auth_client()
    login_response = auth_client.login(user)
    token = login_response['token']['accessToken']

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers= {
            "Authorization": f"Bearer {token}"
        }
    )
    