from datetime import datetime, timedelta

from jose import jwt

SECRET_KEY = "motopecas_super_secret_key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60


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
