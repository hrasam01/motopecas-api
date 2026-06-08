from sqlalchemy.orm import Session

from app.model.usuario import Usuario


class UsuarioRepository:

    def __init__(self, db: Session):
        self.db = db

    def criar(self, usuario: Usuario):

        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)

        return usuario

    def buscar_por_email(
        self,
        email: str
    ):

        return (
            self.db.query(Usuario)
            .filter(
                Usuario.email == email
            )
            .first()
        )

    def listar(self):

        return (
            self.db.query(Usuario)
            .all()
        )
