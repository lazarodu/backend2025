from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from blog.api.deps import user_repo
from blog.usecases.user.register_user import RegisterUserUseCase
from blog.usecases.user.login_user import LoginUserUseCase
from blog.usecases.user.logout_user import LogoutUserUseCase
from blog.usecases.user.get_current_user import GetCurrentUserUseCase
from blog.usecases.user.set_current_user import SetCurrentUserUseCase
from blog.domain.entities.user import User
from blog.domain.value_objects.email_vo import Email
from blog.domain.value_objects.password import Password
import uuid

router = APIRouter()

# ----------------------
# Shared Schemas
# ----------------------

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str
    role: str

class LoginRequest(BaseModel):
    email: str
    password: str

class SetCurrentRequest(BaseModel):
    user_id: str

# ----------------------
# Register
# ----------------------

@router.post("/register")
def register_user(data: RegisterRequest):
    try:
        user = User(
            id=str(uuid.uuid4()),
            name=data.name,
            email=Email(data.email),
            password=Password(data.password),
            role=data.role
        )
        usecase = RegisterUserUseCase(user_repo)
        result = usecase.execute(user)
        return {"message": "User registered successfully", "user_id": result.id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# ----------------------
# Login
# ----------------------

@router.post("/login")
def login_user(data: LoginRequest):
    try:
        usecase = LoginUserUseCase(user_repo)
        result = usecase.execute(Email(data.email), Password(data.password))
        return {"message": "Login successful", "user": result.name}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

# ----------------------
# Logout
# ----------------------

@router.post("/logout")
def logout_user():
    usecase = LogoutUserUseCase(user_repo)
    usecase.execute()
    return {"message": "Logout successful"}

# ----------------------
# Set Current User
# ----------------------

@router.post("/set-current")
def set_current_user(data: SetCurrentRequest):
    try:
        usecase = SetCurrentUserUseCase(user_repo)
        usecase.execute(data.user_id)
        return {"message": "Current user set"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# ----------------------
# Get Current User
# ----------------------

@router.get("/me")
def get_current_user():
    try:
        usecase = GetCurrentUserUseCase(user_repo)
        result = usecase.execute()
        return {
            "id": result.id,
            "name": result.name,
            "email": str(result.email),
            "role": result.role
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
