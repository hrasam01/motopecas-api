from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.dto.usuario_dto import (
    UsuarioCreateDTO,
    UsuarioResponseDTO
)

from app.repository.usuario_repository import (
    UsuarioRepository
)

from app.service.usuario_service import (
    UsuarioService
)

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)


def get_service(
    db: Session = Depends(get_db)
):
    repository = UsuarioRepository(db)

    return UsuarioService(
        repository
    )


@router.post(
    "/",
    response_model=UsuarioResponseDTO,
    status_code=201
)
def criar_usuario(
    dto: UsuarioCreateDTO,
    service: UsuarioService = Depends(get_service)
):

    usuario = service.criar(
        nome=dto.nome,
        email=dto.email,
        senha=dto.senha
    )

    return usuario


@router.get(
    "/",
    response_model=list[UsuarioResponseDTO]
)
def listar_usuarios(
    service: UsuarioService = Depends(get_service)
):

    return service.listar()
