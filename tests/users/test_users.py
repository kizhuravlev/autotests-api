from http import HTTPStatus

import pytest
import allure

from httpx_module.tools.allure.tags import AllureTag
from httpx_module.tools.allure.epics import AllureEpic
from httpx_module.tools.allure.features import AllureFeature
from httpx_module.tools.allure.stories import AllureStory
from allure_commons.types import Severity

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
@allure.tag(AllureTag.REGRESSION, AllureTag.USERS)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.USERS)
class TestUsers:
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    @allure.title("Create user")
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_user(self, domain: str, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema(email=fake.email(domain=domain))
        print(request.email)
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title("Get user me")
    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    def test_get_user_me(self, function_user: UserFixture, private_users_client: PrivateUsersClient):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)
        
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_user.response)

        validate_json_schema(response.json(), function_user.response.model_json_schema())