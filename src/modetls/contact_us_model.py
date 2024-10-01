from pydantic import BaseModel


class ContactUsModel(BaseModel):
    first_name: str
    last_name: str
    email: str
    company_name: str