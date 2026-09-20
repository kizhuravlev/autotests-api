from enum import Enum


class APIRoutes(str, Enum):
    USERS = "/api/v1/users"
    FILES = "/api/v1/files"
    AUTHENTICATION = "/api/v1/authentication"
    EXERCISES = "/api/v1/exercises"
    COURSES = "/api/v1/courses"

    def __str__(self) -> str:
        return self.value