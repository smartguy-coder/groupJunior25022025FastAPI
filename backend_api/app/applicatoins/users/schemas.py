from pydantic import BaseModel , EmailStr , Field

class UserFields(BaseModel):
    email: EmailStr = Field(description='User email' , examples=['arturkovalchuk497@gmail.com , arturrkovalchuk09gmail.com'])
