from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from .models import SpendCategory


class ExpenseCategoryBase(BaseModel):
    name: str


class ExpenseCategoryCreate(ExpenseCategoryBase):
    pass


class ExpenseCategory(ExpenseCategoryBase):
    id: int

    class Config:
        orm_mode = True


class TransactionClassificationBase(BaseModel):
    transaction_id: int
    spend_category: SpendCategory
    expense_category: ExpenseCategoryCreate
    created_by: int
    updated_by: Optional[int] = None


class TransactionClassificationCreate(TransactionClassificationBase):
    pass


class TransactionClassification(TransactionClassificationBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    expense_category: ExpenseCategory

    class Config:
        orm_mode = True
