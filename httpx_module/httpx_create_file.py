import httpx

from tools.fakers import random_user_email

create_user_payload = {
    "email": random_user_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)

login_user_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"],
}

login_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_user_payload)
access_token = f"Bearer {login_user_response.json()["token"]["accessToken"]}"

create_file_headers = {
    "Authorization": access_token
}

create_file_data = {
    "filename": "file",
    "directory": "local",
}

create_file_files = {
    "upload_file": open("../testdata/files/image.png", "rb"),
}

create_file_response = httpx.post("http://localhost:8000/api/v1/files", data=create_file_data, files=create_file_files, headers=create_file_headers)
print(create_file_response.json())