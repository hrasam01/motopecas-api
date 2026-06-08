from fastapi import FastAPI

from app.controller.categoria_controller import (
    router as categoria_router
)

from app.controller.peca_controller import (
    router as peca_router
)

from app.controller.usuario_controller import (
    router as usuario_router
)

from app.controller.auth_controller import (
    router as auth_router
)

from app.controller.cliente_controller import (
    router as cliente_router
)

from app.exceptions.handlers import (
    categoria_nao_encontrada_handler,
    categoria_duplicada_handler,
    peca_nao_encontrada_handler,
    preco_invalido_handler,
    estoque_invalido_handler,
    usuario_ja_existe_handler,
    credenciais_invalidas_handler,
    cliente_nao_encontrado_handler,
    cliente_ja_existe_handler,
    cep_invalido_handler
)

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

app = FastAPI(
    title="MotoPeças API",
    description="API para gerenciamento de peças de motocicletas",
    version="1.0.0"
)

app.include_router(categoria_router)
app.include_router(peca_router)
app.include_router(usuario_router)
app.include_router(auth_router)
app.include_router(cliente_router)

app.add_exception_handler(
    CategoriaNaoEncontradaException,
    categoria_nao_encontrada_handler
)

app.add_exception_handler(
    CategoriaDuplicadaException,
    categoria_duplicada_handler
)

app.add_exception_handler(
    PecaNaoEncontradaException,
    peca_nao_encontrada_handler
)

app.add_exception_handler(
    PecaPrecoInvalidoException,
    preco_invalido_handler
)

app.add_exception_handler(
    EstoqueInvalidoException,
    estoque_invalido_handler
)

app.add_exception_handler(
    UsuarioJaExisteException,
    usuario_ja_existe_handler
)

app.add_exception_handler(
    CredenciaisInvalidasException,
    credenciais_invalidas_handler
)

app.add_exception_handler(
    ClienteNaoEncontradoException,
    cliente_nao_encontrado_handler
)

app.add_exception_handler(
    ClienteJaExisteException,
    cliente_ja_existe_handler
)

app.add_exception_handler(
    CepInvalidoException,
    cep_invalido_handler
)

@app.get("/")
def home():
    return {
        "mensagem": "MotoPeças API funcionando!"
    }
