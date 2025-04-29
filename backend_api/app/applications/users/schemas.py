from pydantic import BaseModel, EmailStr, Field, model_validator, ValidationInfo


class BaseFields(BaseModel):
    email: EmailStr = Field(description='User email', examples=['test_hillel_api_mailing@ukr.net'])
    name: str = Field(description='User nickname', examples=['Casper'])


class PasswordField(BaseModel):
    password: str = Field(min_length=8)

    @model_validator(mode="before")
    def validate_password(cls, values: dict, info: ValidationInfo) -> dict:
        print(values, 5555555555555555555)
        print(info, 5555555555555555555)
        return values


class RegisterUserFields(BaseFields, PasswordField):
    pass
