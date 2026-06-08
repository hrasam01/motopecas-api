from sqlalchemy.orm import Session

from app.model.compra import Compra


class CompraRepository:

    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        return self.db.query(
            Compra
        ).all()

    def criar(
        self,
        compra: Compra
    ):
        self.db.add(compra)
        self.db.commit()
        self.db.refresh(compra)

        return compra
