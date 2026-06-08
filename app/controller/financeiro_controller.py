from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import (
    get_db
)

from app.dto.financeiro_dto import (
    FinanceiroDTO
)

from app.service.financeiro_service import (
    FinanceiroService
)

from app.security.auth_dependency import (
    get_current_user
)

router = APIRouter(
    prefix="/financeiro",
    tags=["Financeiro"]
)


@router.get(
    "/",
    response_model=FinanceiroDTO
)
def resumo_financeiro(
    db: Session = Depends(get_db),
    user: str = Depends(
        get_current_user
    )
):

    service = FinanceiroService(
        db
    )

    return service.resumo()
