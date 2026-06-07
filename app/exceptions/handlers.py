from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.categoria_exceptions import (
    CategoriaNaoEncontradaException,
    CategoriaDuplicadaException
)

from app.exceptions.peca_exceptions import (
    PecaNaoEncontradaException,
    PecaPrecoInvalidoException,
    EstoqueInvalidoException
)


async def categoria_nao_encontrada_handler(
    request: Request,
    exc: CategoriaNaoEncontradaException
):
    return JSONResponse(
        status_code=404,
        content={
            "erro": str(exc)
        }
    )


async def categoria_duplicada_handler(
    request: Request,
    exc: CategoriaDuplicadaException
):
    return JSONResponse(
        status_code=400,
        content={
            "erro": str(exc)
        }
    )

async def peca_nao_encontrada_handler(
    request: Request,
    exc: PecaNaoEncontradaException
):
    return JSONResponse(
        status_code=404,
        content={"erro": str(exc)}
    )


async def preco_invalido_handler(
    request: Request,
    exc: PecaPrecoInvalidoException
):
    return JSONResponse(
        status_code=400,
        content={"erro": str(exc)}
    )


async def estoque_invalido_handler(
    request: Request,
    exc: EstoqueInvalidoException
):
    return JSONResponse(
        status_code=400,
        content={"erro": str(exc)}
    )
