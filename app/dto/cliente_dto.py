from pydantic import BaseModel
from typing import Optional


class ClienteCreateDTO(BaseModel):
    nome: str
    cpf: str
    email: str
    telefone: str
    cep: str


class ClienteResponseDTO(BaseModel):
    id: int
    nome: str
    cpf: str
    email: str
    telefone: str

    cep: str
    logradouro: str
    bairro: str
    cidade: str
    estado: str

    model_config = {
        "from_attributes": True
    }
