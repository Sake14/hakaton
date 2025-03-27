from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from ..models.user import User, hash_password, verify_password, create_access_token

router = APIRouter()

user_bd = {}

security = HTTPBasic()

@router.post("/register/")
async def register(user: User):
    if user.username in user_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    hashed_password = hash_password(user.password)
    user_bd[user.username] = {"username": user.username, "password": hashed_password}
    return {"massage": "User registered successfully"}

@router.post("/login/")
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    user = user_bd.get(credentials.username)
    if user is None or not verify_password(credentials.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    access_token = create_access_token(data={"sub": credentials.username})
    return {"access_token": access_token, "token_type": "bearer"}