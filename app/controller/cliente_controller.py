from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import (
    get_db
)

from app.dto.cliente_dto import (
    ClienteCreateDTO,
    ClienteResponseDTO
)

from app.mapper.cliente_mapper import (
    ClienteMapper
)

from app.repository.cliente_repository import (
    ClienteRepository
)

from app.service.cliente_service import (
    ClienteService
)

from app.security.auth_dependency import (
    get_current_user
)

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


def get_service(
    db: Session = Depends(get_db)
):
    repository = ClienteRepository(db)

    return ClienteService(
        repository
    )


@router.get(
    "/",
    response_model=list[ClienteResponseDTO]
)
def listar_clientes(
    service: ClienteService = Depends(
        get_service
    ),
    user: str = Depends(
        get_current_user
    )
):

    clientes = service.listar()

    return [
        ClienteMapper.to_dto(cliente)
        for cliente in clientes
    ]


@router.post(
    "/",
    response_model=ClienteResponseDTO,
    status_code=201
)
def criar_cliente(
    dto: ClienteCreateDTO,
    service: ClienteService = Depends(
        get_service
    ),
    user: str = Depends(
        get_current_user
    )
):

    cliente = service.criar(
        nome=dto.nome,
        cpf=dto.cpf,
        email=dto.email,
        telefone=dto.telefone,
        cep=dto.cep
    )

    return ClienteMapper.to_dto(
        cliente
    )
