from pydantic import BaseModel, field_validator
from typing import Optional

from app.dto.validators import validar_cpf


class ClienteCreateDTO(BaseModel):
    nome: str
    cpf: str
    email: str
    telefone: str
    cep: str

    @field_validator("cpf")
    @classmethod
    def validar_cpf(cls, v: str) -> str:
        return validar_cpf(v)


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
