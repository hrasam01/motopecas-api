from sqlalchemy.orm import Session

from app.model.cliente import Cliente


class ClienteRepository:

    def __init__(self, db: Session):
        self.db = db

    def listar(self):
        return self.db.query(
            Cliente
        ).all()

    def buscar_por_id(
        self,
        cliente_id: int
    ):
        return (
            self.db.query(Cliente)
            .filter(
                Cliente.id == cliente_id
            )
            .first()
        )

    def criar(
        self,
        cliente: Cliente
    ):
        self.db.add(cliente)
        self.db.commit()
        self.db.refresh(cliente)

        return cliente

    def deletar(
        self,
        cliente: Cliente
    ):
        self.db.delete(cliente)
        self.db.commit()

    def buscar_por_cpf(
        self,
        cpf: str
    ):
        return (
            self.db.query(Cliente)
            .filter(
                Cliente.cpf == cpf
            )
            .first()
        )
    
    
    def buscar_por_email(
        self,
        email: str
    ):
        return (
            self.db.query(Cliente)
            .filter(
                Cliente.email == email
            )
            .first()
        )
