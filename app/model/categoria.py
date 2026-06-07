from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.base import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    descricao: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )
    pecas: Mapped[list["Peca"]] = relationship(
        back_populates="categoria"
    )
