from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
from models import Client, Base
from schemas import ClientCreate, Client, ClientUpdate
from services import clients_service

Base.metadata.create_all(bind=engine)

r = APIRouter(prefix="/api/clients", tags=["Clients"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@r.post("/", response_model=Client, status_code=status.HTTP_201_CREATED)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    return clients_service.create_client(db, client)

@r.get("/", response_model=List[Client])
def get_clients(db: Session = Depends(get_db)):
    return clients_service.get_clients(db)

@r.get("/{{client_id}}", response_model=Client)
def get_client(client_id: int, db: Session = Depends(get_db)):
    db_client = clients_service.get_client(db, client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@r.put("/{{client_id}}", response_model=Client)
def update_client(client_id: int, client_update: ClientUpdate, db: Session = Depends(get_db)):
    db_client = clients_service.update_client(db, client_id, client_update)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@r.delete("/{{client_id}}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    clients_service.delete_client(db, client_id)
