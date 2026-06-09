from sqlalchemy.orm import Session

from app.model.peca import Peca


class PecaRepository:

    def __init__(self, db: Session):
        self.db = db

    def listar(self, categoria_id: int | None = None, preco_min: float | None = None, preco_max: float | None = None, nome: str | None = None):
        query = self.db.query(Peca)

        if categoria_id:
            query = query.filter(Peca.categoria_id == categoria_id)
        if preco_min is not None:
            query = query.filter(Peca.preco >= preco_min)
        if preco_max is not None:
            query = query.filter(Peca.preco <= preco_max)
        if nome:
            query = query.filter(Peca.nome.ilike(f"%{nome}%"))

        return query.all()

    def buscar_por_id(self, peca_id: int):
        return (
            self.db.query(Peca)
            .filter(Peca.id == peca_id)
            .first()
        )

    def criar(self, peca: Peca):
        self.db.add(peca)
        self.db.commit()
        self.db.refresh(peca)

        return peca

    def deletar(self, peca: Peca):
        self.db.delete(peca)
        self.db.commit()
