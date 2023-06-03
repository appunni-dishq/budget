from datetime import datetime
from typing import Optional, Dict

from pydantic import BaseModel

from .models import AccountProvider, AccountType


class AccountBase(BaseModel):
    name: str
    account_no: str
    description: str
    balance_string: str
    connection_id: int
    account_type: AccountType
    account_provider: AccountProvider


class AccountCreate(AccountBase):
    pass


class AccountUpdate(AccountBase):
    updated_by: Optional[int] = None


class Account(AccountBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class ConnectionBase(BaseModel):
    conn_name: str
    provider: AccountProvider
    login_url: str
    credentials: Dict[str, str]
    extra: Optional[str] = None


class ConnectionCreate(ConnectionBase):
    pass


class ConnectionUpdate(ConnectionBase):
    pass


class Connection(ConnectionBase):
    id: int

    class Config:
        orm_mode = True
