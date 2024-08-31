from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from services.auth import token_interceptor
import services.user as user_service
from models.user import UserModel
from database import get_db_context
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(request: UserModel, db: Session = Depends(get_db_context), user = Depends(token_interceptor)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return user_service.create_user(db, request)

@router.get("/")
async def get_users(db: Session = Depends(get_db_context)):
    return user_service.get_all_users(db)

@router.get("/{user_id}")
async def get_user_by_id(user_id: str, db: Session = Depends(get_db_context)):
    return user_service.get_user_by_id(db, user_id)

@router.put("/{user_id}")
async def update_user(user_id: str, request: UserModel, db: Session = Depends(get_db_context), user = Depends(token_interceptor)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return user_service.update_user(db, user_id, request)

@router.delete("/{user_id}")
async def delete_user(user_id: str, db: Session = Depends(get_db_context), user = Depends(token_interceptor)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return user_service.delete_user(db, user_id)