from httpx import Client

from httpx_module.clients.auth.auth_client import get_auth_client, LoginRequestSchema

def get_private_http_client(user: LoginRequestSchema) -> Client:
    
    auth_client = get_auth_client()
    login_response = auth_client.login(user)
    token = login_response.token.access_token

    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers= {
            "Authorization": f"Bearer {token}"
        }
    )
    