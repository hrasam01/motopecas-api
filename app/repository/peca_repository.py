from sqlalchemy.orm import Session

from app.model.peca import Peca


class PecaRepository:

    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        return self.db.query(Peca).all()

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
