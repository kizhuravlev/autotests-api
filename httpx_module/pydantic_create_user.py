from pydantic import BaseModel, Field, EmailStr, UUID4

STR_LENGTH_VALIDATOR = {"min_length": 1, "max_length": 50}
PASSWORD_LENGTH_VALIDATOR = {"min_length": 1, "max_length": 250}

class UserSchema(BaseModel):
    id: UUID4
    email: EmailStr
    last_name: str = Field(**STR_LENGTH_VALIDATOR, alias="lastName")
    first_name: str = Field(**STR_LENGTH_VALIDATOR, alias="firstName")
    middle_name: str = Field(**STR_LENGTH_VALIDATOR, alias="middleName")

class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str = Field(**PASSWORD_LENGTH_VALIDATOR)
    last_name: str = Field(**STR_LENGTH_VALIDATOR, alias="lastName")
    first_name: str = Field(**STR_LENGTH_VALIDATOR, alias="firstName")
    middle_name: str = Field(**STR_LENGTH_VALIDATOR, alias="middleName")

class CreateUserResponseSchema(BaseModel):
    user: UserSchema