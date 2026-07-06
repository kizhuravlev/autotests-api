from pydantic import BaseModel, Field, EmailStr, UUID4

class UserSchema(BaseModel):
    id: UUID4
    email: EmailStr
    last_name: str = Field(min_length=1, max_length=50, alias="lastName")
    first_name: str = Field(min_length=1, max_length=50, alias="firstName")
    middle_name: str = Field(min_length=1, max_length=50, alias="middleName")

class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=250)
    last_name: str = Field(min_length=1, max_length=50, alias="lastName")
    first_name: str = Field(min_length=1, max_length=50, alias="firstName")
    middle_name: str = Field(min_length=1, max_length=50, alias="middleName")

class CreateUserResponseSchema(BaseModel):
    user: UserSchema