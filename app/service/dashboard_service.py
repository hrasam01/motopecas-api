from sqlalchemy import func

from app.model.cliente import Cliente
from app.model.fornecedor import Fornecedor
from app.model.peca import Peca
from app.model.compra import Compra
from app.model.venda import Venda


class DashboardService:

    def __init__(self, db):
        self.db = db

    def resumo(self):

        total_clientes = (
            self.db.query(
                func.count(Cliente.id)
            ).scalar()
        )

        total_fornecedores = (
            self.db.query(
                func.count(Fornecedor.id)
            ).scalar()
        )

        total_pecas = (
            self.db.query(
                func.count(Peca.id)
            ).scalar()
        )

        total_compras = (
            self.db.query(
                func.count(Compra.id)
            ).scalar()
        )

        total_vendas = (
            self.db.query(
                func.count(Venda.id)
            ).scalar()
        )

        estoque_total = (
            self.db.query(
                func.coalesce(
                    func.sum(
                        Peca.quantidade_estoque
                    ),
                    0
                )
            ).scalar()
        )

        return {
            "total_clientes": total_clientes,
            "total_fornecedores": total_fornecedores,
            "total_pecas": total_pecas,
            "total_compras": total_compras,
            "total_vendas": total_vendas,
            "estoque_total": estoque_total
        }
