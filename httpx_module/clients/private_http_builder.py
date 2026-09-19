from httpx import Client

from httpx_module.clients.auth.auth_client import get_auth_client, LoginRequestSchema
from httpx_module.clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook

from config import settings


def get_private_http_client(user: LoginRequestSchema) -> Client:
    
    auth_client = get_auth_client()
    login_response = auth_client.login(user)
    token = login_response.token.access_token

    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        headers= {
            "Authorization": f"Bearer {token}"
        },
        event_hooks={"request": [curl_event_hook, log_request_event_hook],
                     "response": [log_response_event_hook]}
    )
    