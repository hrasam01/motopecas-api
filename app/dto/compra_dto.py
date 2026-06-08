from pydantic import BaseModel
from datetime import datetime


class CompraCreateDTO(BaseModel):
    fornecedor_id: int
    peca_id: int
    quantidade: int
    valor_unitario: float


class CompraResponseDTO(BaseModel):
    id: int

    fornecedor_id: int
    peca_id: int

    quantidade: int

    valor_unitario: float
    valor_total: float

    data_compra: datetime

    model_config = {
        "from_attributes": True
    }
