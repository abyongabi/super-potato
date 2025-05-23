from fastapi import APIRouter

from models.auth_model import LoginRequest, LoginResponse

router: APIRouter = APIRouter()


@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest) -> LoginResponse:
    return LoginResponse(result=True)
