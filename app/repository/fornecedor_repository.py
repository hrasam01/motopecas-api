from sqlalchemy.orm import Session

from app.model.fornecedor import Fornecedor


class FornecedorRepository:

    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        return self.db.query(
            Fornecedor
        ).all()

    def buscar_por_id(
        self,
        fornecedor_id: int
    ):
        return (
            self.db.query(Fornecedor)
            .filter(
                Fornecedor.id == fornecedor_id
            )
            .first()
        )

    def buscar_por_cnpj(
        self,
        cnpj: str
    ):
        return (
            self.db.query(Fornecedor)
            .filter(
                Fornecedor.cnpj == cnpj
            )
            .first()
        )

    def buscar_por_email(
        self,
        email: str
    ):
        return (
            self.db.query(Fornecedor)
            .filter(
                Fornecedor.email == email
            )
            .first()
        )

    def criar(
        self,
        fornecedor: Fornecedor
    ):
        self.db.add(fornecedor)
        self.db.commit()
        self.db.refresh(fornecedor)

        return fornecedor

    def deletar(
        self,
        fornecedor: Fornecedor
    ):
        self.db.delete(fornecedor)
        self.db.commit()
