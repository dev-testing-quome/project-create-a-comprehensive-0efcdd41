from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
from models import Case, Base
from schemas import CaseCreate, Case, CaseUpdate
from services import cases_service

Base.metadata.create_all(bind=engine)

r = APIRouter(prefix="/api/cases", tags=["Cases"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@r.post("/", response_model=Case, status_code=status.HTTP_201_CREATED)
def create_case(case: CaseCreate, db: Session = Depends(get_db)):
    return cases_service.create_case(db, case)

@r.get("/", response_model=List[Case])
def get_cases(db: Session = Depends(get_db)):
    return cases_service.get_cases(db)

@r.get("/{{case_id}}", response_model=Case)
def get_case(case_id: int, db: Session = Depends(get_db)):
    db_case = cases_service.get_case(db, case_id)
    if db_case is None:
        raise HTTPException(status_code=404, detail="Case not found")
    return db_case

@r.put("/{{case_id}}", response_model=Case)
def update_case(case_id: int, case_update: CaseUpdate, db: Session = Depends(get_db)):
    db_case = cases_service.update_case(db, case_id, case_update)
    if db_case is None:
        raise HTTPException(status_code=404, detail="Case not found")
    return db_case

@r.delete("/{{case_id}}", status_code=status.HTTP_204_NO_CONTENT)
def delete_case(case_id: int, db: Session = Depends(get_db)):
    cases_service.delete_case(db, case_id)
