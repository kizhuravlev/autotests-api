import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные в сервис аналитики")

@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Инициализируем настройки автотестов")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаем пользователя один раз для тестов внутри класса")

@pytest.fixture(scope="function")
def user_client():
    print("[FUNCTION] Создаем клиента каждый раз для использоваия внутри теста")

class TestUserFlow:
    def test_user_can_login(self, settings, user, user_client):
        pass

    def test_user_can_create_course(self, settings, user, user_client):
        pass

class TestAccountFlow:
    def test_user_can_account(self, settings, user, user_client):
        pass

