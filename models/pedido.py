from pydantic import BaseModel, Field, field_validator

class Pedido(BaseModel):
    cliente_id: id
    