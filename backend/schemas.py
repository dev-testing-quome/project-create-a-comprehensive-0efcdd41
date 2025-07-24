from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ClientCreate(BaseModel):
    name: str
    email: str

class ClientUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

class Client(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CaseCreate(BaseModel):
    client_id: int
    case_name: str
    description: Optional[str] = None
    status: Optional[str] = "Open"
    court_date: Optional[datetime] = None

class CaseUpdate(BaseModel):
    case_name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    court_date: Optional[datetime] = None

class Case(BaseModel):
    id: int
    client_id: int
    case_name: str
    description: Optional[str]
    status: str
    court_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    client: Client

    class Config:
        orm_mode = True
