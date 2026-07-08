from httpx_module.clients.users.public_users_client import get_public_users_client
from httpx_module.clients.users.private_users_client import get_private_users_client

from httpx_module.clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from httpx_module.clients.auth.auth_schema import LoginRequestSchema

from httpx_module.tools.fakers import random_user_email
from httpx_module.tools.assertions.schema import validate_json_schema


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=random_user_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string",
)

create_user_response = public_users_client.create_user(create_user_request)

login_user_request = LoginRequestSchema(
    email=create_user_request.email,
    password=create_user_request.password,
)

private_users_client = get_private_users_client(login_user_request)

get_user_response = private_users_client.get_user_api(create_user_response.user.id)

get_user_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)
