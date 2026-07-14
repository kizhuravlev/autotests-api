from http import HTTPStatus

from httpx_module.clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema
from httpx_module.clients.users.public_users_client import get_public_users_client
from httpx_module.clients.users.users_schema import CreateUserRequestSchema
from httpx_module.clients.auth.auth_client import get_auth_client
from httpx_module.tools.assertions.authentication import assert_login_response
from httpx_module.tools.assertions.base import assert_status_code
from httpx_module.tools.assertions.schema import validate_json_schema

def test_login():
    public_user_client = get_public_users_client()
    auth_client = get_auth_client()

    create_user_request = CreateUserRequestSchema()
    public_user_client.create_user(create_user_request)

    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password,
    )

    login_response = auth_client.login_api(login_request)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

    assert_status_code(login_response.status_code, HTTPStatus.OK)
    assert_login_response(login_response_data)

    validate_json_schema(login_response.json(), login_response_data.model_json_schema())
    



