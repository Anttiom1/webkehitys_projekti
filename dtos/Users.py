from pydantic import BaseModel


class UserRes(BaseModel):
    id: int
    username: str
    role: str
    
class AddUserReq(BaseModel):
    UserName: str
    Password: str
    Role: str
    
class LoginReq(BaseModel):
    username: str
    password: str
    
class LoginRes(BaseModel):
    token: str