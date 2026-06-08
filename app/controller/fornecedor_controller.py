from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import (
    get_db
)

from app.dto.fornecedor_dto import (
    FornecedorCreateDTO,
    FornecedorResponseDTO
)

from app.mapper.fornecedor_mapper import (
    FornecedorMapper
)

from app.repository.fornecedor_repository import (
    FornecedorRepository
)

from app.service.fornecedor_service import (
    FornecedorService
)

from app.security.auth_dependency import (
    get_current_user
)

router = APIRouter(
    prefix="/fornecedores",
    tags=["Fornecedores"]
)


def get_service(
    db: Session = Depends(get_db)
):
    repository = FornecedorRepository(db)

    return FornecedorService(
        repository
    )


@router.get(
    "/",
    response_model=list[FornecedorResponseDTO]
)
def listar_fornecedores(
    service: FornecedorService = Depends(
        get_service
    ),
    user: str = Depends(
        get_current_user
    )
):

    fornecedores = service.listar()

    return [
        FornecedorMapper.to_dto(
            fornecedor
        )
        for fornecedor in fornecedores
    ]


@router.post(
    "/",
    response_model=FornecedorResponseDTO,
    status_code=201
)
def criar_fornecedor(
    dto: FornecedorCreateDTO,
    service: FornecedorService = Depends(
        get_service
    ),
    user: str = Depends(
        get_current_user
    )
):

    fornecedor = service.criar(
        razao_social=dto.razao_social,
        cnpj=dto.cnpj,
        email=dto.email,
        telefone=dto.telefone,
        cep=dto.cep
    )

    return FornecedorMapper.to_dto(
        fornecedor
    )
