from pydantic import BaseModel, EmailStr, field_validator


class UsuarioCreateDTO(BaseModel):
    nome: str
    email: EmailStr
    senha: str

    @field_validator("senha")
    @classmethod
    def validar_senha(cls, v: str) -> str:
        if len(v) < 6:
            raise ValueError("Senha deve ter no mínimo 6 caracteres")
        return v


class UsuarioResponseDTO(BaseModel):
    id: int
    nome: str
    email: str

    model_config = {
        "from_attributes": True
    }
