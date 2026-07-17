import pytest

from httpx_module.clients.auth.auth_client import AuthClient, get_auth_client

@pytest.fixture
def authentication_client() -> AuthClient:
    return get_auth_client()