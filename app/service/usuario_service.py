from app.model.usuario import Usuario

from app.repository.usuario_repository import (
    UsuarioRepository
)

from app.security.password_handler import (
    gerar_hash
)

from app.exceptions.auth_exceptions import (
    UsuarioJaExisteException
)


class UsuarioService:

    def __init__(
        self,
        repository: UsuarioRepository
    ):
        self.repository = repository

    def listar(self):

        return self.repository.listar()

    def criar(
        self,
        nome: str,
        email: str,
        senha: str
    ):

        usuario_existente = (
            self.repository
            .buscar_por_email(email)
        )

        if usuario_existente:

            raise UsuarioJaExisteException(
                "Já existe usuário com esse email"
            )

        usuario = Usuario(
            nome=nome,
            email=email,
            senha_hash=gerar_hash(
                senha
            )
        )

        return self.repository.criar(
            usuario
        )
