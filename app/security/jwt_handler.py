from datetime import datetime, timedelta

from jose import jwt
from app.config.settings import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


def criar_token(
    dados: dict
):

    payload = dados.copy()

    expire = (
        datetime.utcnow()
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload.update(
        {
            "exp": expire
        }
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
