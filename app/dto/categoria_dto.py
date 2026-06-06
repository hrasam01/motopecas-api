from pydantic import BaseModel
from typing import Optional


class CategoriaCreateDTO(BaseModel):
    nome: str
    descricao: Optional[str] = None


class CategoriaResponseDTO(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None

    model_config = {
        "from_attributes": True
    }
