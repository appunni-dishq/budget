from typing import List

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from . import schemas, models

router = APIRouter()


class TransactionService:
    @classmethod
    def create_transaction(cls, db: Session, transaction: schemas.TransactionCreate):
        obj = models.Transaction(**transaction.dict())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @classmethod
    def get_transaction(cls, db: Session, transaction_id: int):
        obj = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
        if obj is None:
            raise HTTPException(status_code=404, detail="Transaction not found")
        return obj

    @classmethod
    def get_transactions(cls, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Transaction).offset(skip).limit(limit).all()

    @classmethod
    def update_transaction(cls, db: Session, transaction_id: int, transaction: schemas.TransactionCreate):
        obj = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
        if obj is None:
            raise HTTPException(status_code=404, detail="Transaction not found")

        for key, value in transaction.dict().items():
            setattr(obj, key, value)
        db.commit()
        db.refresh(obj)
        return obj

    @classmethod
    def delete_transaction(cls, db: Session, transaction_id: int):
        obj = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
        if obj is None:
            raise HTTPException(status_code=404, detail="Transaction not found")

        db.delete(obj)
        db.commit()
        return obj

    @classmethod
    def create_transactions_batch(cls, db: Session, transactions: List[schemas.TransactionCreate]):
        objs = [models.Transaction(**transaction.dict()) for transaction in transactions]
        db.bulk_save_objects(objs)
        db.commit()
        return objs
