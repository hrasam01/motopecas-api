from pydantic import BaseModel, EmailStr


class UsuarioCreateDTO(BaseModel):
    nome: str
    email: EmailStr
    senha: str


class UsuarioResponseDTO(BaseModel):
    id: int
    nome: str
    email: str

    model_config = {
        "from_attributes": True
    }
