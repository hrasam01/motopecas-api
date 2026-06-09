from sqlalchemy.orm import Session

from app.model.venda import Venda


class VendaRepository:

    def __init__(self, db: Session):
        self.db = db

    def listar(self, cliente_id: int | None = None, peca_id: int | None = None, data_inicio: str | None = None, data_fim: str | None = None):
        query = self.db.query(Venda)

        if cliente_id:
            query = query.filter(Venda.cliente_id == cliente_id)
        if peca_id:
            query = query.filter(Venda.peca_id == peca_id)
        if data_inicio:
            query = query.filter(Venda.data_venda >= data_inicio)
        if data_fim:
            query = query.filter(Venda.data_venda <= data_fim)

        return query.all()

    def criar(
        self,
        venda: Venda
    ):
        self.db.add(venda)
        self.db.commit()
        self.db.refresh(venda)

        return venda
