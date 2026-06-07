from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.dto.categoria_dto import (
    CategoriaCreateDTO,
    CategoriaResponseDTO
)
from app.mapper.categoria_mapper import CategoriaMapper
from app.repository.categoria_repository import CategoriaRepository
from app.service.categoria_service import CategoriaService
from app.exceptions.categoria_exceptions import (
    CategoriaNaoEncontradaException,
    CategoriaDuplicadaException
)


router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)


def get_service(db: Session = Depends(get_db)):
    repository = CategoriaRepository(db)
    return CategoriaService(repository)


@router.get("/", response_model=list[CategoriaResponseDTO])
def listar_categorias(
    service: CategoriaService = Depends(get_service)
):
    categorias = service.listar()

    return [
        CategoriaMapper.to_dto(categoria)
        for categoria in categorias
    ]


@router.get("/{categoria_id}",
            response_model=CategoriaResponseDTO)
def buscar_categoria(
    categoria_id: int,
    service: CategoriaService = Depends(get_service)
):
    categoria = service.buscar_por_id(categoria_id)

    return CategoriaMapper.to_dto(categoria)

@router.post("/",
             response_model=CategoriaResponseDTO,
             status_code=201)
def criar_categoria(
    dto: CategoriaCreateDTO,
    service: CategoriaService = Depends(get_service)
):
    categoria = service.criar(
        nome=dto.nome,
        descricao=dto.descricao
    )

    return CategoriaMapper.to_dto(categoria)

@router.put("/{categoria_id}",
            response_model=CategoriaResponseDTO)
def atualizar_categoria(
    categoria_id: int,
    dto: CategoriaCreateDTO,
    service: CategoriaService = Depends(get_service)
):
    categoria = service.atualizar(
        categoria_id=categoria_id,
        nome=dto.nome,
        descricao=dto.descricao
    )

    return CategoriaMapper.to_dto(categoria)

@router.delete("/{categoria_id}",
               status_code=204)
def deletar_categoria(
    categoria_id: int,
    service: CategoriaService = Depends(get_service)
):
    service.deletar(categoria_id)
