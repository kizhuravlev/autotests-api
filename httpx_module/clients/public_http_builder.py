from httpx import Client


def get_public_http_client() -> Client:
    """
    Создает и возвращает настроенный httpx.Client

    :return: Настроенный экземпляр httpx.Client
    """
    return Client(timeout=100, base_url="http://localhost:8000")