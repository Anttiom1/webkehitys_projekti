from fastapi import APIRouter
from dtos.Users import LoginReq, LoginRes
from services.users_service_factory import UserService
from tools.dependencies import TokenTool

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/login")
async def login(service: UserService, req: LoginReq, token: TokenTool) -> LoginRes:
    token = service.login(req, token)
    return LoginRes(token=token)