from models.company import CompanyModel
from services.auth import token_interceptor
from database import get_db_context
from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
import services.company as company_service

router = APIRouter(
    prefix="/company",
    tags=["company"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_company(request: CompanyModel, db: Session = Depends(get_db_context), user = Depends(token_interceptor)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")        
    
    return company_service.create_company(db, request)

@router.get("/", status_code=status.HTTP_200_OK)
def get_companies(db: Session = Depends(get_db_context)):
    return company_service.get_all_companies(db)

@router.get("/{company_id}", status_code=status.HTTP_200_OK)
def get_company_by_id(company_id: str, db: Session = Depends(get_db_context)):
    return company_service.get_company_by_id(db, company_id)

@router.put("/{company_id}", status_code=status.HTTP_200_OK)
def update_company(company_id: str, request: CompanyModel, db: Session = Depends(get_db_context), user = Depends(token_interceptor)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return company_service.update_company(db, company_id, request)

@router.delete("/{company_id}", status_code=status.HTTP_200_OK)
def delete_company(company_id: str, db: Session = Depends(get_db_context), user = Depends(token_interceptor)):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return company_service.delete_company(db, company_id)