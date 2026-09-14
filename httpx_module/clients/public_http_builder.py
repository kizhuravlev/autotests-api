from httpx import Client

from httpx_module.clients.event_hooks import curl_event_hook


def get_public_http_client() -> Client:
    """
    Создает и возвращает настроенный httpx.Client

    :return: Настроенный экземпляр httpx.Client
    """
    return Client(timeout=100, base_url="http://localhost:8000", event_hooks={"request": [curl_event_hook]})