from sqlalchemy import func

from app.model.compra import Compra
from app.model.venda import Venda


class FinanceiroService:

    def __init__(self, db):
        self.db = db

    def resumo(self):

        total_compras = (
            self.db.query(
                func.coalesce(
                    func.sum(
                        Compra.valor_total
                    ),
                    0
                )
            ).scalar()
        )

        total_vendas = (
            self.db.query(
                func.coalesce(
                    func.sum(
                        Venda.valor_total
                    ),
                    0
                )
            ).scalar()
        )

        saldo = (
            float(total_vendas)
            - float(total_compras)
        )

        return {
            "total_compras": float(
                total_compras
            ),
            "total_vendas": float(
                total_vendas
            ),
            "saldo": saldo
        }
