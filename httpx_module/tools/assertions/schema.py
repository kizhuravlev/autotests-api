from typing import Any

from jsonschema import validate
from jsonschema.validators import Draft202012Validator

from httpx_module.tools.logger import get_logger

import allure

logger = get_logger("SCHEMA_ASSERTIONS")

@allure.step("Check validation JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    logger.info("Check validation JSON schema")

    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )