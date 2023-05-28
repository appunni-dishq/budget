from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TransactionBase(BaseModel):
    unique_transaction_id: str
    transaction_date: datetime
    short_description: Optional[str] = None
    description: str
    amount: float
    currency: str
    created_by: int
    updated_by: Optional[int] = None


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

