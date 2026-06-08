from pydantic import BaseModel


class FornecedorCreateDTO(BaseModel):
    razao_social: str
    cnpj: str
    email: str
    telefone: str
    cep: str


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
