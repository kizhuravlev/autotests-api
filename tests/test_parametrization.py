from _pytest.fixtures import SubRequest
import pytest

@pytest.fixture(params=[
    "https://dev.company.com",
    "https://stage.company.com",
    "https://prod.company.com"
])
def host(request: SubRequest):
    return request.param

def test_host(host: str):
    print(f"Running test on host: {host}")

@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    def test_users_with_operations(self, user: str):
        return print(f"Print users with operations: {user}")

    def test_users_without_operations(self, user: str):
        return print(f"Print users without operations: {user}")


@pytest.mark.parametrize("phone", [
    "+79999999999",
    "+78888888888",
    "+77777777777"
], ids=[
    "1",
    "2",
    "3"
])
def test_ids(phone: str):
    pass