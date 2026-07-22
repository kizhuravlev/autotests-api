import pytest

@pytest.mark.parametrize("number", [1, 2, 3, 4])
def test_numbers(number: int):
    assert number >= 1

@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["macos", "win", "linux"])
@pytest.mark.parametrize("host",[
    "https://dev.company.com",
    "https://staging.company.com",
    "https://prod.company.com"
])
def test_multinumbers(os: str, host: str):
    assert len(os + host) > 0