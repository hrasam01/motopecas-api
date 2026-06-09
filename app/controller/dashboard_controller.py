from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.dto.dashboard_dto import (
    DashboardDTO
)

from app.service.dashboard_service import (
    DashboardService
)

from app.security.auth_dependency import (
    get_current_user
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/",
    response_model=DashboardDTO
)
def dashboard(
    db: Session = Depends(get_db),
    user: str = Depends(
        get_current_user
    )
):

    service = DashboardService(db)

    return service.resumo()
