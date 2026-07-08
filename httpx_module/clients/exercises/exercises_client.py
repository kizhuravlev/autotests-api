from httpx_module.clients.api_client import APIClient
from httpx_module.clients.private_http_builder import get_private_http_client
from httpx_module.clients.auth.auth_client import LoginRequestSchema

from httpx_module.clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, UpdateExerciseRequestSchema, GetExercisesResponseSchema, GetExerciseResponseSchema, CreateExerciseResponseSchema, UpdateExerciseResponseSchema

from httpx import Response

class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка заданий.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))
    
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))
    
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")
    
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))
    
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
    
    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Метод получения данных о заданиях

        :return: Возвращает json-объект переданных заданий
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)
    
    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод получения данных о задании

        :return: Возвращает json-объект переданного задания
        """
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)
    
    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод получения данных о созданном задании

        :return: Возвращает json-объект созданного задания
        """
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)
    
    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Метод получения данных об обновленном задании

        :return: Возвращает json-объект обновленного задания
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)
    
def get_exercises_client(user: LoginRequestSchema) -> ExercisesClient:
    """
    Функция создания готового к использованию ExercisesClient

    :return: Возвращает готовый ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user=user))