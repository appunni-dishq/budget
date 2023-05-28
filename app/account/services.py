from sqlalchemy.orm import Session

from . import models, schemas


class CRUDAccount:
    @classmethod
    def create_account(cls, db: Session, account: schemas.AccountCreate):
        db_account = models.Account(**account.dict())
        db.add(db_account)
        db.commit()
        db.refresh(db_account)
        return db_account

    @classmethod
    def get_account(cls, db: Session, account_id: int):
        return db.query(models.Account).filter(models.Account.id == account_id).first()

    @classmethod
    def get_accounts(cls, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Account).offset(skip).limit(limit).all()

    @classmethod
    def update_account(cls, db: Session, account_id: int, account: schemas.AccountUpdate):
        db_account = db.query(models.Account).filter(models.Account.id == account_id).first()
        if db_account is None:
            return None
        for var, value in vars(account).items():
            setattr(db_account, var, value) if value else None
        db.add(db_account)
        db.commit()
        db.refresh(db_account)
        return db_account

    @classmethod
    def delete_account(cls, db: Session, account_id: int):
        db_account = db.query(models.Account).filter(models.Account.id == account_id).first()
        db.delete(db_account)
        db.commit()
        return db_account


class CRUDConnection:
    @classmethod
    def create_connection(cls, db: Session, connection: schemas.ConnectionCreate):
        db_connection = models.Connection(**connection.dict())
        db.add(db_connection)
        db.commit()
        db.refresh(db_connection)
        return db_connection

    @classmethod
    def get_connection(cls, db: Session, conn_id: str):
        return db.query(models.Connection).filter(models.Connection.conn_id == conn_id).first()

    @classmethod
    def get_connections(cls, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Connection).offset(skip).limit(limit).all()

    @classmethod
    def update_connection(cls, db: Session, conn_id: str, connection: schemas.ConnectionUpdate):
        db_connection = db.query(models.Connection).filter(models.Connection.conn_id == conn_id).first()
        if db_connection is None:
            return None
        for var, value in vars(connection).items():
            setattr(db_connection, var, value) if value else None
        db.add(db_connection)
        db.commit()
        db.refresh(db_connection)
        return db_connection

    @classmethod
    def delete_connection(cls, db: Session, conn_id: str):
        db_connection = db.query(models.Connection).filter(models.Connection.conn_id == conn_id).first()
        db.delete(db_connection)
        db.commit()
        return db_connection
