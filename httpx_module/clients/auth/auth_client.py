from typing import TypedDict

from httpx import Response

from httpx_module.clients.api_client import APIClient
from httpx_module.clients.public_http_builder import get_public_http_client

class LoginRequestDict(TypedDict):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class RefreshTokenDict(TypedDict):
    """
    Описание структуры запроса для обновления токена.
    """
    refreshToken: str

class TokenDict(TypeError):
    """
    Описание структуры ответа токена
    """
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginResponseDict(TypedDict):
    """
    Описание структуры ответа на аутентификацию
    """
    token: TokenDict

class AuthClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)
    
    def refresh_api(self, request: RefreshTokenDict) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)
    
    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request=request)
        return response.json()
    


def get_auth_client() -> AuthClient:
    """
    Функция настраивает готовый AuthClient

    :return: Возвращается готовый AuthClient
    """
    return AuthClient(client=get_public_http_client())  


