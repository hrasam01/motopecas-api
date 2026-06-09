from pydantic import BaseModel


class DashboardDTO(BaseModel):
    total_clientes: int
    total_fornecedores: int
    total_pecas: int
    total_compras: int
    total_vendas: int
    estoque_total: int
