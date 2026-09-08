from enum import Enum

class AllureFeature(str, Enum):
    USERS = "Users"
    FILES = "Files"
    AUTHENTICATION = "Authentication"
    COURSES = "Courses"
    EXERCISES = "Exercises"