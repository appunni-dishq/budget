from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from .schemas import TransactionCreate, Transaction
from .services import TransactionService

router = APIRouter()


@router.post("/", response_model=Transaction, status_code=201)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return TransactionService.create_transaction(db, transaction)


@router.get("/{transaction_id}", response_model=Transaction)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return TransactionService.get_transaction(db, transaction_id)


@router.get("/", response_model=List[Transaction])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return TransactionService.get_transactions(db, skip=skip, limit=limit)


@router.put("/{transaction_id}", response_model=Transaction)
def update_transaction(transaction_id: int, transaction: TransactionCreate, db: Session = Depends(get_db)):
    return TransactionService.update_transaction(db, transaction_id, transaction)


@router.delete("/{transaction_id}", response_model=Transaction)
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    return TransactionService.delete_transaction(db, transaction_id)


@router.post("/batch/", response_model=List[Transaction], status_code=201)
def create_transactions_batch(transactions: List[TransactionCreate], db: Session = Depends(get_db)):
    return TransactionService.create_transactions_batch(db, transactions)
