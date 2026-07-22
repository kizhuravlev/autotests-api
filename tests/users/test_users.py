import email
from http import HTTPStatus

import pytest

from httpx_module.clients.users.private_users_client import PrivateUsersClient
from httpx_module.clients.users.public_users_client import PublicUsersClient
from httpx_module.clients.users.users_schema import GetUserResponseSchema
from httpx_module.pydantic_create_user import CreateUserRequestSchema, CreateUserResponseSchema

from httpx_module.tools.assertions.schema import validate_json_schema
from httpx_module.tools.assertions.base import assert_status_code
from httpx_module.tools.assertions.users import assert_create_user_response, assert_get_user_response
from httpx_module.tools.fakers import fake

from fixtures.users import UserFixture


@pytest.mark.users
@pytest.mark.regression
class TestUsers:
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    def test_create_user(self, domain: str, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema(email=fake.email(domain=domain))
        print(request.email)
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_user_me(self, function_user: UserFixture, private_users_client: PrivateUsersClient):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)
        
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)

        validate_json_schema(response.json(), function_user.response.model_json_schema())