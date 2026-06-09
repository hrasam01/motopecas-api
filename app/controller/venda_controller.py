from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.dto.venda_dto import (
    VendaCreateDTO,
    VendaResponseDTO
)

from app.mapper.venda_mapper import (
    VendaMapper
)

from app.repository.venda_repository import (
    VendaRepository
)

from app.repository.cliente_repository import (
    ClienteRepository
)

from app.repository.peca_repository import (
    PecaRepository
)

from app.service.venda_service import (
    VendaService
)

from app.security.auth_dependency import (
    get_current_user
)

router = APIRouter(
    prefix="/vendas",
    tags=["Vendas"]
)


def get_service(
    db: Session = Depends(get_db)
):

    return VendaService(
        VendaRepository(db),
        ClienteRepository(db),
        PecaRepository(db)
    )


@router.get(
    "/",
    response_model=list[VendaResponseDTO]
)
def listar_vendas(
    cliente_id: int | None = None,
    peca_id: int | None = None,
    data_inicio: str | None = None,
    data_fim: str | None = None,
    service: VendaService = Depends(
        get_service
    ),
    user: str = Depends(
        get_current_user
    )
):

    vendas = service.listar(
        cliente_id=cliente_id,
        peca_id=peca_id,
        data_inicio=data_inicio,
        data_fim=data_fim
    )

    return [
        VendaMapper.to_dto(venda)
        for venda in vendas
    ]


@router.post(
    "/",
    response_model=VendaResponseDTO,
    status_code=201
)
def criar_venda(
    dto: VendaCreateDTO,
    service: VendaService = Depends(
        get_service
    ),
    user: str = Depends(
        get_current_user
    )
):

    venda = service.criar(
        cliente_id=dto.cliente_id,
        peca_id=dto.peca_id,
        quantidade=dto.quantidade,
        valor_unitario=dto.valor_unitario
    )

    return VendaMapper.to_dto(
        venda
    )
