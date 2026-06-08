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

from app.exceptions.auth_exceptions import (
    UsuarioJaExisteException,
    CredenciaisInvalidasException
)

from app.exceptions.cliente_exceptions import (
    ClienteNaoEncontradoException,
    ClienteJaExisteException,
    CepInvalidoException
)

from app.exceptions.fornecedor_exceptions import (
    FornecedorNaoEncontradoException,
    FornecedorJaExisteException
)

from app.exceptions.compra_exceptions import (
    CompraInvalidaException
)

from app.exceptions.venda_exceptions import (
    VendaInvalidaException,
    EstoqueInsuficienteException
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

async def credenciais_invalidas_handler(
    request: Request,
    exc: CredenciaisInvalidasException
):
    return JSONResponse(
        status_code=401,
        content={
            "erro": str(exc)
        }
    )

async def usuario_ja_existe_handler(
    request: Request,
    exc: UsuarioJaExisteException
):
    return JSONResponse(
        status_code=400,
        content={
            "erro": str(exc)
        }
    )

async def cliente_nao_encontrado_handler(
    request,
    exc: ClienteNaoEncontradoException
):
    return JSONResponse(
        status_code=404,
        content={"erro": str(exc)}
    )


async def cliente_ja_existe_handler(
    request,
    exc: ClienteJaExisteException
):
    return JSONResponse(
        status_code=400,
        content={"erro": str(exc)}
    )


async def cep_invalido_handler(
    request,
    exc: CepInvalidoException
):
    return JSONResponse(
        status_code=400,
        content={"erro": str(exc)}
    )

async def fornecedor_nao_encontrado_handler(
    request: Request,
    exc: FornecedorNaoEncontradoException
):
    return JSONResponse(
        status_code=404,
        content={
            "erro": str(exc)
        }
    )


async def fornecedor_ja_existe_handler(
    request: Request,
    exc: FornecedorJaExisteException
):
    return JSONResponse(
        status_code=400,
        content={
            "erro": str(exc)
        }
    )

async def compra_invalida_handler(
    request: Request,
    exc: CompraInvalidaException
):
    return JSONResponse(
        status_code=400,
        content={
            "erro": str(exc)
        }
    )

async def venda_invalida_handler(
    request: Request,
    exc: VendaInvalidaException
):
    return JSONResponse(
        status_code=400,
        content={"erro": str(exc)}
    )


async def estoque_insuficiente_handler(
    request: Request,
    exc: EstoqueInsuficienteException
):
    return JSONResponse(
        status_code=400,
        content={"erro": str(exc)}
    )
