from pydantic import BaseModel, Field, field_validator

class Produto(BaseModel):
    nome : str
    preco : float = Field(gt=0)
    estoque: int = Field(gt=0)
    marca_id: int
