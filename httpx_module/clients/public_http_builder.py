from httpx import Client

import config
from httpx_module.clients.event_hooks import curl_event_hook

from config import settings


def get_public_http_client() -> Client:
    """
    Создает и возвращает настроенный httpx.Client

    :return: Настроенный экземпляр httpx.Client
    """
    return Client(timeout=settings.http_client.timeout, base_url=settings.http_client.client_url, event_hooks={"request": [curl_event_hook]})