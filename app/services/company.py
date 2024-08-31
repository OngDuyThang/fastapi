from datetime import datetime
from models.company import CompanyModel
from fastapi import HTTPException
from sqlalchemy.orm import Session

def create_company(request: CompanyModel, db: Session):
    if (not request.name) or (not request.mode):
        raise HTTPException(status_code=400, detail="All fields are required")
    
    try:
        company = CompanyModel(
            name=request.name,
            description=request.description,
            mode=request.mode,
            rating=request.rating
        )
        
        db.add(company)
        db.commit()
        db.refresh(company)
        
        return company
    except Exception as e:
        raise HTTPException(e)
    
def get_all_companies(db: Session):
    try:
        return db.query(CompanyModel).all()
    except Exception as e:
        raise HTTPException(e)
    
def get_company_by_id(db: Session, company_id: str):
    try:
        return db.query(CompanyModel).filter(CompanyModel.id == company_id).first()
    except Exception as e:
        raise HTTPException(e)
    
def update_company(db: Session, company_id: str, request: CompanyModel):
    if (not request.name) or (not request.mode):
        raise HTTPException(status_code=400, detail="All fields are required")
    
    try:
        company = db.query(CompanyModel).filter(CompanyModel.id == company_id).first()
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")
        
        company.name = request.name
        company.description = request.description
        company.mode = request.mode
        company.rating = request.rating
        company.updated_at = datetime.now()
        
        db.add(company)
        db.commit()
        db.refresh(company)
        
        return company
    except Exception as e:
        raise HTTPException(e)
    
def delete_company(db: Session, company_id: str):
    try:
        company = db.query(CompanyModel).filter(CompanyModel.id == company_id).first()
        if not company:
            raise HTTPException(status_code=404, detail="Company not found")
        
        db.delete(company)
        db.commit()
        
        return True
    except Exception as e:
        raise HTTPException(e)