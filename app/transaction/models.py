from enum import Enum

from sqlalchemy import Column, Integer, String, DateTime, Float, func, Enum as SQLEnum, ForeignKey, Text, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)
    account_id = Column(Integer, ForeignKey('account.id'))
    account = relationship("Account")
    unique_transaction_id = Column(String(255), unique=True, index=True)
    transaction_date = Column(DateTime(timezone=True))
    short_description = Column(String(255))
    description = Column(Text)
    amount = Column(DECIMAL(15,2))
    currency = Column(String(3))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True))
    created_by = Column(Integer)
    updated_by = Column(Integer)
