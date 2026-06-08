from sqlalchemy import (
    String,
    ForeignKey,
    Numeric
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.base import Base


class Peca(Base):

    __tablename__ = "pecas"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    descricao: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    preco: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    quantidade_estoque: Mapped[int] = mapped_column(
        nullable=False
    )

    categoria_id: Mapped[int] = mapped_column(
        ForeignKey("categorias.id"),
        nullable=False
    )

    categoria: Mapped["Categoria"] = relationship(
        back_populates="pecas"
    )

    compras = relationship(
        "Compra"
    )

    vendas = relationship(
        "Venda"
    )
