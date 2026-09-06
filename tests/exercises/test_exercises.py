from http import HTTPStatus

import pytest

from fixtures.courses import CourseFixture
from httpx_module.clients.exercises.exercises_client import ExercisesClient
from httpx_module.clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from httpx_module.tools.assertions.base import assert_status_code
from httpx_module.tools.assertions.exercises import assert_create_exercise_response
from httpx_module.tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.exercises
class TestExercises:
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())