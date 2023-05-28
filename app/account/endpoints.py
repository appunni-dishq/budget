from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .schemas import AccountCreate, Account, ConnectionUpdate, AccountUpdate
from .schemas import ConnectionCreate, Connection
from .services import CRUDAccount
from .services import CRUDConnection
from ..database import get_db

connection_router = APIRouter()

router = APIRouter()


@connection_router.post("/", response_model=Connection, status_code=201)
def create_connection(connection: ConnectionCreate, db: Session = Depends(get_db)):
    return CRUDConnection.create_connection(db, connection)


@connection_router.get("/{conn_id}", response_model=Connection)
def read_connection(conn_id: str, db: Session = Depends(get_db)):
    return CRUDConnection.get_connection(db, conn_id)


@connection_router.get("/", response_model=List[Connection])
def read_connections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return CRUDConnection.get_connections(db, skip=skip, limit=limit)


@connection_router.put("/{conn_id}", response_model=Connection)
def update_connection(conn_id: str, connection: ConnectionUpdate, db: Session = Depends(get_db)):
    return CRUDConnection.update_connection(db, conn_id, connection)


@connection_router.delete("/{conn_id}", response_model=Connection)
def delete_connection(conn_id: str, db: Session = Depends(get_db)):
    return CRUDConnection.delete_connection(db, conn_id)


@router.post("/", response_model=Account, status_code=201)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    return CRUDAccount.create_account(db, account)


@router.get("/{account_id}", response_model=Account)
def read_account(account_id: int, db: Session = Depends(get_db)):
    return CRUDAccount.get_account(db, account_id)


@router.get("/", response_model=List[Account])
def read_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return CRUDAccount.get_accounts(db, skip=skip, limit=limit)


@router.put("/{account_id}", response_model=Account)
def update_account(account_id: int, account: AccountUpdate, db: Session = Depends(get_db)):
    return CRUDAccount.update_account(db, account_id, account)


@router.delete("/{account_id}", response_model=Account)
def delete_account(account_id: int, db: Session = Depends(get_db)):
    return CRUDAccount.delete_account(db, account_id)
