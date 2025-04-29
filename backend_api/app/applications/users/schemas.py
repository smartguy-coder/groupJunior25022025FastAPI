from pydantic import BaseModel, EmailStr, Field


class BaseFields(BaseModel):
    email: EmailStr = Field(description='User email', examples=['test_hillel_api_mailing@ukr.net'])
    name: str = Field(description='User nickname', examples=['Casper'])

class PasswordField(BaseModel):
    password: str = Field(min_length=8)


class RegisterUserFields(BaseFields, PasswordField):
    pass
