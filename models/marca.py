from pydantic import BaseModel, EmailStr, Field, field_validator

class Marca(BaseModel):
    nome : str
    pais : str