from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import (
    get_db
)

from app.dto.auth_dto import (
    LoginDTO,
    TokenDTO
)

from app.repository.usuario_repository import (
    UsuarioRepository
)

from app.service.auth_service import (
    AuthService
)

router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)


def get_service(
    db: Session = Depends(get_db)
):

    repository = UsuarioRepository(db)

    return AuthService(
        repository
    )


from fastapi.security import OAuth2PasswordRequestForm

@router.post(
    "/login",
    response_model=TokenDTO
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: AuthService = Depends(get_service)
):

    return service.login(
        email=form_data.username,
        senha=form_data.password
    )
