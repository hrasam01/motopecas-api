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


class Venda(Base):

    __tablename__ = "vendas"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    cliente_id: Mapped[int] = mapped_column(
        ForeignKey("clientes.id"),
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

    data_venda: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    cliente = relationship(
        "Cliente"
    )

    peca = relationship(
        "Peca"
    )
