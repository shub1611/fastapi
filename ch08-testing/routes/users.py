from fastapi import APIRouter, HTTPException, status, Depends
from model.users import User, UserSignIn, TokenResponse
from auth.hash_password import HashPassword
from database.connection import Database
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token


user_router = APIRouter(tags=["User"])
users = {}
user_database = Database(User)
hash_passowrd = HashPassword()

@user_router.post('/signup')
async def sign_new_user(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists")
    hashed_password = hash_passowrd.create_hash(user.password)
    user.password = hashed_password
    await user_database.save(user)
    return {'message': 'user successfully registered'}

@user_router.post('/signin', response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()):
    user_exist = await User.find_one(User.email == user.username)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist."
        )
    if hash_passowrd.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed."
    )