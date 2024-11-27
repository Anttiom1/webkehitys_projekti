from dotenv import load_dotenv

from controllers import account_controller, auth_controller, carts_controller, categories_controller, order_controller, products_controller, users_controller
from custom_exceptions.not_found import NotFoundexception
from custom_exceptions.not_unique import UserNameTakenException
from custom_exceptions.unauthorize import UnauthorizedException


load_dotenv()
from fastapi import FastAPI, HTTPException, Request

app = FastAPI()
app.include_router(users_controller.router)
app.include_router(products_controller.router)
app.include_router(categories_controller.router)
app.include_router(auth_controller.router)
app.include_router(carts_controller.router)
app.include_router(order_controller.router)
app.include_router(account_controller.router)

@app.exception_handler(NotFoundexception)
async def not_found(request: Request, exc: NotFoundexception):
    raise HTTPException(status_code=404, detail=str(exc))

@app.exception_handler(UserNameTakenException)
async def usernametaken(request: Request, exc: NotFoundexception):
    raise HTTPException(status_code=400, detail=str(exc))

@app.exception_handler(UnauthorizedException)
async def usernametaken(request: Request, exc: UnauthorizedException):
    raise HTTPException(status_code=401, detail=str(exc))

@app.middleware('http')
async def log_urls(request: Request, call_next):

    print("logging", request.url)
    return await call_next(request)