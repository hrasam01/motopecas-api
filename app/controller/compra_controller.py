from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.dto.compra_dto import (
    CompraCreateDTO,
    CompraResponseDTO
)

from app.mapper.compra_mapper import (
    CompraMapper
)

from app.repository.compra_repository import (
    CompraRepository
)

from app.repository.peca_repository import (
    PecaRepository
)

from app.repository.fornecedor_repository import (
    FornecedorRepository
)

from app.service.compra_service import (
    CompraService
)

from app.security.auth_dependency import (
    get_current_user
)

router = APIRouter(
    prefix="/compras",
    tags=["Compras"]
)


def get_service(
    db: Session = Depends(get_db)
):

    compra_repository = CompraRepository(db)

    peca_repository = PecaRepository(db)

    fornecedor_repository = (
        FornecedorRepository(db)
    )

    return CompraService(
        compra_repository,
        peca_repository,
        fornecedor_repository
    )


@router.get(
    "/",
    response_model=list[CompraResponseDTO]
)
def listar_compras(
    service: CompraService = Depends(
        get_service
    ),
    user: str = Depends(
        get_current_user
    )
):

    compras = service.listar()

    return [
        CompraMapper.to_dto(compra)
        for compra in compras
    ]


@router.post(
    "/",
    response_model=CompraResponseDTO,
    status_code=201
)
def criar_compra(
    dto: CompraCreateDTO,
    service: CompraService = Depends(
        get_service
    ),
    user: str = Depends(
        get_current_user
    )
):

    compra = service.criar(
        fornecedor_id=dto.fornecedor_id,
        peca_id=dto.peca_id,
        quantidade=dto.quantidade,
        valor_unitario=dto.valor_unitario
    )

    return CompraMapper.to_dto(
        compra
    )
