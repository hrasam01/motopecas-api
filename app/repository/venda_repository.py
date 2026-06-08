from sqlalchemy.orm import Session

from app.model.venda import Venda


class VendaRepository:

    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        return self.db.query(
            Venda
        ).all()

    def criar(
        self,
        venda: Venda
    ):
        self.db.add(venda)
        self.db.commit()
        self.db.refresh(venda)

        return venda
