from fastapi import FastAPI

from app.controller.categoria_controller import router as categoria_router

from app.exceptions.handlers import (
    categoria_nao_encontrada_handler,
    categoria_duplicada_handler
)

from app.exceptions.categoria_exceptions import (
    CategoriaNaoEncontradaException,
    CategoriaDuplicadaException
)

app = FastAPI(
    title="MotoPeças API",
    description="API para gerenciamento de peças de motocicletas",
    version="1.0.0"
)

app.include_router(categoria_router)

app.add_exception_handler(
    CategoriaNaoEncontradaException,
    categoria_nao_encontrada_handler
)

app.add_exception_handler(
    CategoriaDuplicadaException,
    categoria_duplicada_handler
)

@app.get("/")
def home():
    return {
        "mensagem": "MotoPeças API funcionando!"
    }
