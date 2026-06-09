from app.model.compra import Compra

from app.repository.compra_repository import (
    CompraRepository
)

from app.repository.peca_repository import (
    PecaRepository
)

from app.repository.fornecedor_repository import (
    FornecedorRepository
)

from app.exceptions.compra_exceptions import (
    CompraInvalidaException
)

from app.exceptions.fornecedor_exceptions import (
    FornecedorNaoEncontradoException
)

from app.exceptions.peca_exceptions import (
    PecaNaoEncontradaException
)


class CompraService:

    def __init__(
        self,
        compra_repository: CompraRepository,
        peca_repository: PecaRepository,
        fornecedor_repository: FornecedorRepository
    ):
        self.compra_repository = compra_repository
        self.peca_repository = peca_repository
        self.fornecedor_repository = fornecedor_repository

    def listar(self, fornecedor_id: int | None = None, peca_id: int | None = None, data_inicio: str | None = None, data_fim: str | None = None):
        return self.compra_repository.listar(
            fornecedor_id=fornecedor_id,
            peca_id=peca_id,
            data_inicio=data_inicio,
            data_fim=data_fim
        )

    def criar(
        self,
        fornecedor_id: int,
        peca_id: int,
        quantidade: int,
        valor_unitario: float
    ):

        if quantidade <= 0:
            raise CompraInvalidaException(
                "Quantidade inválida"
            )

        fornecedor = (
            self.fornecedor_repository
            .buscar_por_id(fornecedor_id)
        )

        if not fornecedor:
            raise FornecedorNaoEncontradoException(
                "Fornecedor não encontrado"
            )

        peca = (
            self.peca_repository
            .buscar_por_id(peca_id)
        )

        if not peca:
            raise PecaNaoEncontradaException(
                "Peça não encontrada"
            )

        valor_total = (
            quantidade *
            valor_unitario
        )

        compra = Compra(
            fornecedor_id=fornecedor_id,
            peca_id=peca_id,
            quantidade=quantidade,
            valor_unitario=valor_unitario,
            valor_total=valor_total
        )

        # REGRA DE NEGÓCIO
        peca.quantidade_estoque += quantidade

        self.compra_repository.db.commit()

        return self.compra_repository.criar(
            compra
        )
