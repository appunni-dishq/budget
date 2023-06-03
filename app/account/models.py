import enum

from sqlalchemy import Column, Integer, String, DateTime, func, Enum as SQLEnum, Boolean, JSON, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AccountType(str, enum.Enum):
    CREDIT_CARD = 'credit_card'
    BNPL = 'bnpl'
    SAVINGS = 'savings'
    CURRENT = 'current'
    PF = 'pf'
    NPS = 'nps'


class AccountProvider(str, enum.Enum):
    HDFC_BANK = 'hdfc_bank'
    CRED = 'cred'
    ICICI_BANK = 'icici_bank'
    CANARA_BANK = 'canara_bank'


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, index=True)
    unique_account_id = Column(String(255), index=True)
    account_type = Column(SQLEnum(AccountType))
    account_provider = Column(SQLEnum(AccountProvider))
    name = Column(String(255))
    description = Column(Text())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Connection(Base):
    __tablename__ = "connection"

    id = Column(Integer, primary_key=True, index=True)
    conn_id = Column(String(250), unique=True, nullable=False)
    provider = Column(SQLEnum(AccountProvider))
    login_url = Column(String(500))
    credentials = Column(JSON)
    extra = Column(String(5000), nullable=True)
