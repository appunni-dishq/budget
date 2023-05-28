from enum import Enum

from sqlalchemy import Column, Integer, String, Enum as SQLEnum, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class SpendCategory(str, Enum):
    EXPENSE = 'expense'
    INVESTMENT = 'investment'
    TRANSFER = 'transfer'
    IGNORE = 'ignore'


class ExpenseCategory(Base):
    __tablename__ = "expense_category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)


class TransactionClassification(Base):
    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, ForeignKey('transaction.id'))
    transaction = relationship("Transaction")
    spend_category = Column(SQLEnum(SpendCategory))
    expense_category_id = Column(Integer, ForeignKey('expense_category.id'))
    expense_category = relationship("ExpenseCategory")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Integer)
    updated_by = Column(Integer)
