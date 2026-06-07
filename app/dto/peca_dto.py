from pydantic import BaseModel
from typing import Optional


class PecaCreateDTO(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float
    quantidade_estoque: int
    categoria_id: int


class PecaResponseDTO(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: float
    quantidade_estoque: int
    categoria_id: int

    model_config = {
        "from_attributes": True
    }
