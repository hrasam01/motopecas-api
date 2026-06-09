from sqlalchemy.orm import Session

from app.model.compra import Compra


class CompraRepository:

    def __init__(self, db: Session):
        self.db = db

    def listar(self, fornecedor_id: int | None = None, peca_id: int | None = None, data_inicio: str | None = None, data_fim: str | None = None):
        query = self.db.query(Compra)

        if fornecedor_id:
            query = query.filter(Compra.fornecedor_id == fornecedor_id)
        if peca_id:
            query = query.filter(Compra.peca_id == peca_id)
        if data_inicio:
            query = query.filter(Compra.data_compra >= data_inicio)
        if data_fim:
            query = query.filter(Compra.data_compra <= data_fim)

        return query.all()

    def criar(
        self,
        compra: Compra
    ):
        self.db.add(compra)
        self.db.commit()
        self.db.refresh(compra)

        return compra
