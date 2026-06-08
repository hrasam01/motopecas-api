from pydantic import BaseModel


class FinanceiroDTO(BaseModel):
    total_compras: float
    total_vendas: float
    saldo: float
