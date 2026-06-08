from app.database.base import Base
from app.database.database import engine

from app.model.categoria import Categoria
from app.model.peca import Peca
from app.model.usuario import Usuario
from app.model.cliente import Cliente
from app.model.fornecedor import Fornecedor
from app.model.compra import Compra
from app.model.venda import Venda

Base.metadata.create_all(bind=engine)
