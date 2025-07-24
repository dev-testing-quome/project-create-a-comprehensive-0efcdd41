from sqlalchemy.orm import Session
from models import Client
from schemas import ClientCreate, ClientUpdate

def create_client(db: Session, client: ClientCreate) -> Client:
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(db: Session) -> list:
    return db.query(Client).all()

def get_client(db: Session, client_id: int) -> Client:
    return db.query(Client).filter(Client.id == client_id).first()

def update_client(db: Session, client_id: int, client_update: ClientUpdate) -> Client:
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client:
        for key, value in client_update.dict(exclude_unset=True).items():
            setattr(db_client, key, value)
        db.commit()
        db.refresh(db_client)
        return db_client
    return None

def delete_client(db: Session, client_id: int):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client:
        db.delete(db_client)
        db.commit()
