from typing import Any, Sized
import allure


@allure.step("Check that response status code equals to {expected}")
def assert_status_code(actual: int, expected: int):
    """
    Проверяет что фактический статус-код соответствует ожидаемому.

    :actual: Фактический статус-код
    :expected: Ожидаемый статус-код
    :raises AssertionError: Если статус-коды не совпадают
    """
    assert actual == expected, (
        f"Incorrect response status code",
        f"Expected status code: {expected}",
        f"Actual status code: {actual}"
    )

@allure.step("Check that {name} equals to {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    assert actual == expected, (
        f"Incorrect value: {name}",
        f"Expected value: {expected}",
        f"Actual value: {actual}"
    )

@allure.step("Check that {name} is true")
def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (
        f"Incorrect value: {name}",
        f"Expected true but value got: {actual}"
    )

def assert_length(actual: Sized, expected: Sized, name: str):
    with allure.step(f"Check that {name} length equals to {len(expected)}"):
        assert len(actual) == len(expected), (
            f"Incorrect object length: {name}",
            f"Expected length: {len(expected)}",
            f"Actual length: {len(actual)}"
        )