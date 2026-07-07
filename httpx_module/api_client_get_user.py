from httpx_module.clients.users.public_users_client import get_public_users_client
from httpx_module.clients.auth.auth_schema import LoginRequestSchema
from httpx_module.clients.users.private_users_client import get_private_users_client
from httpx_module.clients.users.users_schema import CreateUserRequestSchema

from httpx_module.tools.fakers import random_user_email

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email = random_user_email(),
    password = "Password123!",
    last_name = "string",
    first_name = "string",
    middle_name = "string",
) 

create_user_data = public_user_client.create_user(create_user_request)
print(f"Create user data: {create_user_data}")

login_user_request = LoginRequestSchema(
    email = create_user_request.email,
    password = create_user_request.password
)
private_user_client = get_private_users_client(user=login_user_request)
get_user_data = private_user_client.get_user(create_user_data.user.id)
print(f"Get user data: {get_user_data}")

