from typing import Generator

import pytest
from fastapi.testclient import TestClient
from pydantic.types import Decimal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from testcontainers.mysql import MySqlContainer

from app.database import get_db
from app.main import app as fastapi_app
from app.transaction.models import Base
from app.transaction.services import TransactionService

engine = create_engine("mysql://test:test@localhost/test")
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="session")
def db() -> Generator:
    # Spin up a test MySQL instance
    with MySqlContainer("mysql:5.7") as mysql:
        engine = create_engine(mysql.get_connection_url())
        TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base.metadata.create_all(bind=engine)
        yield TestingSessionLocal()


@pytest.fixture
def client(db: Session) -> Generator:
    def override_get_db():
        yield db

    fastapi_app.dependency_overrides[get_db] = override_get_db
    with TestClient(fastapi_app) as c:
        yield c


@pytest.fixture
def test_data_1():
    return {
        "unique_transaction_id": "123abc",
        "transaction_date": "2023-05-29T00:00:00Z",
        "short_desc": "Short description",
        "description": "Detailed description",
        "amount": 123.45,
        "currency": "USD",
        "created_by": 1
    }


def test_create_transaction(client: TestClient, db: Session, test_data_1):
    response = client.post("/transaction/", json=test_data_1)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["amount"] == 123.45
    transaction_in_db = TransactionService.get_transaction(db, 1)
    assert transaction_in_db
    assert transaction_in_db.id == 1
    assert transaction_in_db.amount == Decimal('123.45')
