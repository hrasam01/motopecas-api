from pydantic import BaseModel
from datetime import datetime


class VendaCreateDTO(BaseModel):
    cliente_id: int
    peca_id: int
    quantidade: int
    valor_unitario: float


class VendaResponseDTO(BaseModel):
    id: int

    cliente_id: int
    peca_id: int

    quantidade: int

    valor_unitario: float
    valor_total: float

    data_venda: datetime

    model_config = {
        "from_attributes": True
    }
