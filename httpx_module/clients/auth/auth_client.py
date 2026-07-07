from httpx import Response

from httpx_module.clients.api_client import APIClient
from httpx_module.clients.auth.auth_schema import LoginRequestSchema, LoginResponseSchema, RefreshRequestSchema
from httpx_module.clients.public_http_builder import get_public_http_client

class AuthClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """
    
    def login_api(self, request: LoginRequestSchema) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request.model_dump(by_alias=True))
    
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request.model_dump(by_alias=True))
    
    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request=request)
        return LoginResponseSchema.model_validate_json(response.text)
    


def get_auth_client() -> AuthClient:
    """
    Функция настраивает готовый AuthClient

    :return: Возвращается готовый AuthClient
    """
    return AuthClient(client=get_public_http_client())  


