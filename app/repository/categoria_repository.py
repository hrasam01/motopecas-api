from sqlalchemy.orm import Session

from app.model.categoria import Categoria


class CategoriaRepository:

    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        return self.db.query(Categoria).all()

    def buscar_por_id(self, categoria_id: int):
        return (
            self.db.query(Categoria)
            .filter(Categoria.id == categoria_id)
            .first()
        )

    def criar(self, categoria: Categoria):
        self.db.add(categoria)
        self.db.commit()
        self.db.refresh(categoria)
        return categoria

    def deletar(self, categoria: Categoria):
        self.db.delete(categoria)
        self.db.commit()
