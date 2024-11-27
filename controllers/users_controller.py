from fastapi import APIRouter, HTTPException
from dtos.Users import AddUserReq, UserRes
from mapper.mapper import ResponseMapper
from services.users_service_factory import UserService
from policies.authorize import LoggedInUser
from response_handlers.user_res_handler import UserResResponseHandler

router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("/")
async def get_all_users(service: UserService, mapper: ResponseMapper) -> list[UserRes]:
    users = service.get_all()
    return mapper.map('user_dto', users)

@router.post('/')
async def create_user(user_service: UserService, req: AddUserReq, res_handler: UserResResponseHandler) -> UserRes:
    try:
        user = user_service.create(req)
        return res_handler.send(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get('/account')
async def get_account(logged_in_user: LoggedInUser, res_handler: UserResResponseHandler) -> UserRes:
    return res_handler.send(logged_in_user)

@router.get("/{user_id}")
async def get_account_by_id(service: UserService, id: int, mapper: ResponseMapper):
    user = service.get_user_by_id(id)
    return mapper.map("user_dto", user)
