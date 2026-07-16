import pytest

from pydantic import BaseModel, EmailStr

from httpx_module.clients.users.public_users_client import PublicUsersClient, get_public_users_client
from httpx_module.clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from httpx_module.clients.auth.auth_client import AuthClient, get_auth_client

class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email
    
    @property
    def password(self) -> str:
        return self.request.password
    
@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()

@pytest.fixture
def authentication_client() -> AuthClient:
    return get_auth_client()

@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)