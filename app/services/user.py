from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.user import UserModel
from services.auth import create_hashed_password
from schemas.user import User
from datetime import datetime

def create_user(db: Session, request: UserModel) -> User:
    if (not request.username) or (not request.email) or (not request.first_name) or (not request.last_name) or (not request.password):
        raise HTTPException(status_code=400, detail="All fields are required")
    
    try:
        user = db.query(User).filter((User.username == request.username) | (User.email == request.email)).first()    
        if user:
            raise HTTPException(status_code=400, detail="User already exists")
        
        hashed_password = create_hashed_password(request.password)
        newUser = User(
            username=request.username,
            email=request.email,
            password=hashed_password,
            first_name=request.first_name,
            last_name=request.last_name,
            created_at=datetime.now(),
        )
        
        if (request.company_id):
            newUser.company_id = request.company_id
        
        db.add(newUser)
        db.commit()
        db.refresh(newUser)
        
        return newUser
    except Exception as e:
        raise HTTPException(e)

def get_all_users(db: Session) -> list[User]:
    try:
        return db.query(User).all()
    except Exception as e:
        raise HTTPException(e)

def get_user_by_id(db: Session, user_id: str) -> User:
    try:
        return db.query(User).filter(User.id == user_id).first()
    except Exception as e:
        raise HTTPException(e)

def update_user(db: Session, user_id: str, request: User) -> User:
    if (not request.username) or (not request.email) or (not request.first_name) or (not request.last_name) or (not request.password):
        raise HTTPException(status_code=400, detail="All fields are required")
    
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user.username = request.username
        user.email = request.email
        user.first_name = request.first_name
        user.last_name = request.last_name
        user.password = create_hashed_password(request.password)
        user.updated_at = datetime.now()
        
        if (request.company_id):
            user.company_id = request.company_id

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    except Exception as e:
        raise HTTPException(e)
    
def delete_user(db: Session, user_id: str):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        db.delete(user)
        db.commit()
        
        return True
    except Exception as e:
        raise HTTPException(e)