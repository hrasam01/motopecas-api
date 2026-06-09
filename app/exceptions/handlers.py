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

TITULOS = {
    400: "Requisição Inválida",
    401: "Não Autorizado",
    404: "Não Encontrado",
}


def problema(request: Request, status: int, detail: str):
    return JSONResponse(
        status_code=status,
        media_type="application/problem+json",
        content={
            "type": "about:blank",
            "title": TITULOS.get(status, "Erro"),
            "status": status,
            "detail": detail,
            "instance": str(request.url.path)
        }
    )


async def categoria_nao_encontrada_handler(
    request: Request,
    exc: CategoriaNaoEncontradaException
):
    return problema(request, 404, str(exc))


async def categoria_duplicada_handler(
    request: Request,
    exc: CategoriaDuplicadaException
):
    return problema(request, 400, str(exc))


async def peca_nao_encontrada_handler(
    request: Request,
    exc: PecaNaoEncontradaException
):
    return problema(request, 404, str(exc))


async def preco_invalido_handler(
    request: Request,
    exc: PecaPrecoInvalidoException
):
    return problema(request, 400, str(exc))


async def estoque_invalido_handler(
    request: Request,
    exc: EstoqueInvalidoException
):
    return problema(request, 400, str(exc))


async def credenciais_invalidas_handler(
    request: Request,
    exc: CredenciaisInvalidasException
):
    return problema(request, 401, str(exc))


async def usuario_ja_existe_handler(
    request: Request,
    exc: UsuarioJaExisteException
):
    return problema(request, 400, str(exc))


async def cliente_nao_encontrado_handler(
    request: Request,
    exc: ClienteNaoEncontradoException
):
    return problema(request, 404, str(exc))


async def cliente_ja_existe_handler(
    request: Request,
    exc: ClienteJaExisteException
):
    return problema(request, 400, str(exc))


async def cep_invalido_handler(
    request: Request,
    exc: CepInvalidoException
):
    return problema(request, 400, str(exc))


async def fornecedor_nao_encontrado_handler(
    request: Request,
    exc: FornecedorNaoEncontradoException
):
    return problema(request, 404, str(exc))


async def fornecedor_ja_existe_handler(
    request: Request,
    exc: FornecedorJaExisteException
):
    return problema(request, 400, str(exc))


async def compra_invalida_handler(
    request: Request,
    exc: CompraInvalidaException
):
    return problema(request, 400, str(exc))


async def venda_invalida_handler(
    request: Request,
    exc: VendaInvalidaException
):
    return problema(request, 400, str(exc))


async def estoque_insuficiente_handler(
    request: Request,
    exc: EstoqueInsuficienteException
):
    return problema(request, 400, str(exc))
