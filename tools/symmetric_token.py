from datetime import datetime, timedelta, timezone
import jwt

from tools.token_tool_base import TokenToolBase


class SymmetricToken(TokenToolBase):
    def __init__(self, secret_key):
        self.secret_key = secret_key
        
    def create_token(self, data: dict):
        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(seconds=data['exp'])
        to_encode.update({"iss": "webkehitys", "aud": "webkehitys", "exp": expire})
        token = jwt.encode(to_encode, self.secret_key, algorithm='HS512')

        return token
    
    def verify(self, access_token):
        payload = jwt.decode(
            access_token, self.secret_key, algorithms=['HS512'], audience="webkehitys", issuer="webkehitys"
        )
        return payload
    
    

