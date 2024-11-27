import datetime
from typing import List
import bcrypt
from custom_exceptions.not_unique import UserNameTakenException
from dtos import Users
from dtos.Users import AddUserReq, LoginReq
import models
from services.user_service_base import UserServiceBase
from custom_exceptions.not_found import NotFoundexception
from tools.token_tool_base import TokenToolBase

class UserServiceSQLAlchemy(UserServiceBase):
    def __init__(self, db: models.Db):
        self.context = db

    def get_all(self):
        return self.context.query(models.Users).all()
    
    def create(self, req: AddUserReq) -> models.Users:
        user_exists = self.context.query(models.Users).filter(models.Users.UserName == req.UserName).first()
        if user_exists is not None:
            raise UserNameTakenException('username already taken')
        user = models.Users(
            UserName=req.UserName,
            HashedPassword=bcrypt.hashpw(req.Password.encode('utf-8'), bcrypt.gensalt()),
            Role=req.Role
        )

        user.PasswordSalt = ''.encode('utf-8')
        self.context.add(user)
        self.context.commit()
        return user
    
    
    def login(self, req: LoginReq, token: TokenToolBase) -> str:
        user = self.context.query(models.Users).filter(models.Users.UserName == req.username).first()
        if user is None:
            raise NotFoundexception('user not found')

        if bcrypt.checkpw(req.password.encode('utf-8'), user.HashedPassword):
            return token.create_token({'sub': str(user.Id), 'username': user.UserName, 'iat': datetime.datetime.now().timestamp(),
                                    'exp': datetime.datetime.now().timestamp() + (3600 * 24 * 7)})
        raise NotFoundexception('user not found')

    def get_all(self) -> List[models.Users]:
        return self.context.query(models.Users).all()
    
    def get_user_by_id(self, user_id: int) -> Users:
        return self.context.query(models.Users).filter(models.Users.Id == user_id).first()
