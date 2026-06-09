from pydantic import BaseModel, field_validator

from app.dto.validators import validar_cnpj


class FornecedorCreateDTO(BaseModel):
    razao_social: str
    cnpj: str
    email: str
    telefone: str
    cep: str

    @field_validator("cnpj")
    @classmethod
    def validar_cnpj(cls, v: str) -> str:
        return validar_cnpj(v)


class FornecedorResponseDTO(BaseModel):
    id: int
    razao_social: str
    cnpj: str
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
