from httpx_module.clients.api_client import APIClient
from httpx_module.clients.private_http_builder import get_private_http_client
from httpx_module.clients.auth.auth_client import LoginRequestSchema

from httpx import Response

from typing import TypedDict

class Exercise(TypedDict):
    """
    Описание структуры упражнения
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий
    """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания
    """
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str
    estimatedTime: str | None

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str| None
    estimatedTime: str | None

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на получение заданий
    """
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение задания
    """
    exercise: Exercise

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на обновление задания
    """
    exercise: Exercise

class UpdateExerciseResponseDict(TypedDict):
    exercise: Exercise

class ExercisesClient(APIClient):

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод получения списка заданий.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)
    
    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)
    
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")
    
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)
    
    def delete_exercise(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")
    
    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод получения данных о заданиях

        :return: Возвращает json-объект переданных заданий
        """
        response = self.get_exercises_api(query)
        return response.json()
    
    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод получения данных о задании

        :return: Возвращает json-объект переданного задания
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()
    
    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод получения данных о созданном задании

        :return: Возвращает json-объект созданного задания
        """
        response = self.create_exercise_api(request)
        return response.json()
    
    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Метод получения данных об обновленном задании

        :return: Возвращает json-объект обновленного задания
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request=request)
        return response.json()
    
def get_exercises_client(user: LoginRequestSchema) -> ExercisesClient:
    """
    Функция создания готового к использованию ExercisesClient

    :return: Возвращает готовый ExercisesClient
    """
    return ExercisesClient(client=get_private_http_client(user=user))