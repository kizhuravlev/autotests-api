from http import HTTPStatus

import pytest

from fixtures.users import UserFixture

from httpx_module.clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema
from httpx_module.clients.auth.auth_client import AuthClient
from httpx_module.tools.assertions.authentication import assert_login_response
from httpx_module.tools.assertions.base import assert_status_code
from httpx_module.tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
class TestAuthentication:
    def test_login(self, function_user: UserFixture, authentication_client: AuthClient):
        login_request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        login_response = authentication_client.login_api(login_request)
        login_response_data = LoginResponseSchema.model_validate_json(login_response.text)

        assert_status_code(login_response.status_code, HTTPStatus.OK)
        assert_login_response(login_response_data)

        validate_json_schema(login_response.json(), login_response_data.model_json_schema())
