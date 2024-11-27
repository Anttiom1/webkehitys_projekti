from typing import Annotated

from fastapi import HTTPException, Depends
from starlette import status
from starlette.requests import Request

import models
from services.users_service_factory import UserService
from tools.dependencies import TokenTool


def get_logged_in_user(user_service: UserService, token: TokenTool, req: Request):
    token_from_header = req.headers.get('Authorization')
    if token_from_header is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    header_parts = token_from_header.split(' ')
    if len(header_parts) != 2:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    if header_parts[0] != 'Bearer':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    claims = token.verify(header_parts[1])
    logged_in_user = user_service.get_user_by_id(claims['sub'])
    if logged_in_user is None:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
    return logged_in_user


LoggedInUser = Annotated[models.Users, Depends(get_logged_in_user)]
