from app.repository.usuario_repository import (
    UsuarioRepository
)

from app.security.password_handler import (
    verificar_senha
)

from app.security.jwt_handler import (
    criar_token
)

from app.exceptions.auth_exceptions import (
    CredenciaisInvalidasException
)


class AuthService:

    def __init__(
        self,
        repository: UsuarioRepository
    ):
        self.repository = repository

    def login(
        self,
        email: str,
        senha: str
    ):

        usuario = (
            self.repository
            .buscar_por_email(email)
        )

        if not usuario:

            raise CredenciaisInvalidasException(
                "Email ou senha inválidos"
            )

        senha_valida = verificar_senha(
            senha,
            usuario.senha_hash
        )

        if not senha_valida:

            raise CredenciaisInvalidasException(
                "Email ou senha inválidos"
            )

        token = criar_token(
            {
                "sub": usuario.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }
