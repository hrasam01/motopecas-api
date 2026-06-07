from app.database.base import Base
from app.database.database import engine

from app.model.categoria import Categoria
from app.model.peca import Peca

Base.metadata.create_all(bind=engine)
