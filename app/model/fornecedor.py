from sqlalchemy import String

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.base import Base


class Fornecedor(Base):

    __tablename__ = "fornecedores"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    razao_social: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    cnpj: Mapped[str] = mapped_column(
        String(18),
        unique=True,
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    telefone: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    cep: Mapped[str] = mapped_column(
        String(9),
        nullable=False
    )

    logradouro: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    bairro: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    cidade: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    estado: Mapped[str] = mapped_column(
        String(2),
        nullable=False
    )

    compras = relationship(
        "Compra"
    )
