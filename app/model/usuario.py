from sqlalchemy import String

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.database.base import Base


class Usuario(Base):

    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        unique=True
    )

    senha_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
