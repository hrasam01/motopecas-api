from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.security.auth_dependency import (
    get_current_user
)

from app.dto.peca_dto import (
    PecaCreateDTO,
    PecaResponseDTO
)

from app.mapper.peca_mapper import PecaMapper

from app.repository.peca_repository import (
    PecaRepository
)

from app.repository.categoria_repository import (
    CategoriaRepository
)

from app.service.peca_service import (
    PecaService
)

router = APIRouter(
    prefix="/pecas",
    tags=["Peças"]
)


def get_service(
    db: Session = Depends(get_db)
):

    peca_repository = PecaRepository(db)

    categoria_repository = (
        CategoriaRepository(db)
    )

    return PecaService(
        peca_repository,
        categoria_repository
    )


@router.get(
    "/",
    response_model=list[PecaResponseDTO]
)
def listar_pecas(
    categoria_id: int | None = None,
    preco_min: float | None = None,
    preco_max: float | None = None,
    nome: str | None = None,
    service: PecaService = Depends(get_service),
    usuario=Depends(get_current_user)
):

    pecas = service.listar(
        categoria_id=categoria_id,
        preco_min=preco_min,
        preco_max=preco_max,
        nome=nome
    )

    return [
        PecaMapper.to_dto(peca)
        for peca in pecas
    ]


@router.get(
    "/{peca_id}",
    response_model=PecaResponseDTO
)
def buscar_peca(
    peca_id: int,
    service: PecaService = Depends(get_service),
    usuario=Depends(get_current_user)
):

    peca = service.buscar_por_id(
        peca_id
    )

    return PecaMapper.to_dto(peca)


@router.post(
    "/",
    response_model=PecaResponseDTO,
    status_code=201
)
def criar_peca(
    dto: PecaCreateDTO,
    service: PecaService = Depends(get_service),
    usuario=Depends(get_current_user)
):

    peca = service.criar(
        nome=dto.nome,
        descricao=dto.descricao,
        preco=dto.preco,
        quantidade_estoque=dto.quantidade_estoque,
        categoria_id=dto.categoria_id
    )

    return PecaMapper.to_dto(peca)


@router.put(
    "/{peca_id}",
    response_model=PecaResponseDTO
)
def atualizar_peca(
    peca_id: int,
    dto: PecaCreateDTO,
    service: PecaService = Depends(get_service),
    usuario=Depends(get_current_user)
):

    peca = service.atualizar(
        peca_id=peca_id,
        nome=dto.nome,
        descricao=dto.descricao,
        preco=dto.preco,
        quantidade_estoque=dto.quantidade_estoque,
        categoria_id=dto.categoria_id
    )

    return PecaMapper.to_dto(peca)


@router.delete(
    "/{peca_id}",
    status_code=204
)
def deletar_peca(
    peca_id: int,
    service: PecaService = Depends(get_service),
    usuario=Depends(get_current_user)
):

    service.deletar(peca_id)
