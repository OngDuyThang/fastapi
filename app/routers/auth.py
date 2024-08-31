from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from schemas.user import User
from services.auth import authenticate_user, create_access_token, create_hashed_password
from database import get_db_context

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)
 
@router.post("/token", status_code=status.HTTP_201_CREATED)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_context)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    
    token = create_access_token(user)
    
    return {
        "access_token": token,
        "token_type": "bearer",
    }