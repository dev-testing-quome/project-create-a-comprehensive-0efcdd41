from sqlalchemy.orm import Session
from models import Case
from schemas import CaseCreate, CaseUpdate

def create_case(db: Session, case: CaseCreate) -> Case:
    db_case = Case(**case.dict())
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case

def get_cases(db: Session) -> list:
    return db.query(Case).all()

def get_case(db: Session, case_id: int) -> Case:
    return db.query(Case).filter(Case.id == case_id).first()

def update_case(db: Session, case_id: int, case_update: CaseUpdate) -> Case:
    db_case = db.query(Case).filter(Case.id == case_id).first()
    if db_case:
        for key, value in case_update.dict(exclude_unset=True).items():
            setattr(db_case, key, value)
        db.commit()
        db.refresh(db_case)
        return db_case
    return None

def delete_case(db: Session, case_id: int):
    db_case = db.query(Case).filter(Case.id == case_id).first()
    if db_case:
        db.delete(db_case)
        db.commit()
