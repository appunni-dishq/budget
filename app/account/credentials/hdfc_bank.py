from pydantic import BaseModel


class HDFCBankCredential(BaseModel):
    customer_id: str
    password: str
