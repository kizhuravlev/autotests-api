from httpx_module.clients.api_client import APIClient
from httpx_module.clients.auth.auth_client import LoginRequestSchema
from httpx_module.clients.private_http_builder import get_private_http_client
from httpx_module.clients.files.files_client import File
from httpx_module.clients.users.private_users_client import User

from httpx import Response

from typing import TypedDict

class Course:
    """
    Описание структуры курса
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User

class GetCoursesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка курсов
    """
    userId: str

class CreateCoursesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание курса
    """
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

class UpdateCoursesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление курса
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    description: str | None
    estimatedTime: str | None

class CreateCourseResponseDict(TypedDict):
    """
    Описание структуры ответа на создание курса
    """
    course: Course

class CoursesClient(APIClient):
    """
    Клиент для работы с /api/v1/courses
    """
    
    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Метод получения списка курсов

        :param query: Словарь с userId
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/courses", params=query)
    
    def create_courses_api(self, request: CreateCoursesRequestDict) -> Response:
        """
        Метод создания курса

        :param request: Словарь с title, maxScore, minScore, description, estimatedTime, 
        previewFileId, createdByUserId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/courses", json=request)
    
    def get_course_api(self, course_id: str) -> Response:
        """
        Метод получения курса

        :param course_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/courses/{course_id}")
    
    def update_course_api(self, course_id: str, request: UpdateCoursesRequestDict) -> Response:
        """
        Метод обновления курса

        :param course_id: Идентификатор курса
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/courses/{course_id}", json=request)
    
    def delete_course_api(self, course_id: str) -> Response:
        """
        Метод удаления курса

        :param course_id: Идентификатор курса
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")
    
    def create_course(self, request: CreateCoursesRequestDict) -> CreateCourseResponseDict:
        """
        Метод создания курса с возвращаемым json() data

        :return: Возвращает данные созданного курса в json()
        """
        response = self.create_courses_api(request)
        return response.json()
    
def get_courses_client(user: LoginRequestSchema) -> CoursesClient:
    """
    Функция создает и настраивает готовый CoursesClient

    :return: Возвращает готовый и настроенный CoursesClient
    """
    return CoursesClient(client=get_private_http_client(user=user))