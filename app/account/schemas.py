from datetime import datetime
from typing import Optional, Dict

from pydantic import BaseModel

from .models import AccountProvider


class AccountBase(BaseModel):
    account_name: str


class AccountCreate(AccountBase):
    created_by: int


class AccountUpdate(AccountBase):
    updated_by: Optional[int] = None


class Account(AccountBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class ConnectionBase(BaseModel):
    conn_id: str
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
