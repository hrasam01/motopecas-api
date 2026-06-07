from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.categoria_exceptions import (
    CategoriaNaoEncontradaException,
    CategoriaDuplicadaException
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
