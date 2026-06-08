from datetime import datetime

from sqlalchemy import (
    ForeignKey,
    Numeric,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.base import Base


class Compra(Base):

    __tablename__ = "compras"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    fornecedor_id: Mapped[int] = mapped_column(
        ForeignKey("fornecedores.id"),
        nullable=False
    )

    peca_id: Mapped[int] = mapped_column(
        ForeignKey("pecas.id"),
        nullable=False
    )

    quantidade: Mapped[int] = mapped_column(
        nullable=False
    )

    valor_unitario: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    valor_total: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    data_compra: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    fornecedor = relationship(
        "Fornecedor"
    )

    peca = relationship(
        "Peca"
    )
