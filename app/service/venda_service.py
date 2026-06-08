from app.model.venda import Venda

from app.repository.venda_repository import (
    VendaRepository
)

from app.repository.cliente_repository import (
    ClienteRepository
)

from app.repository.peca_repository import (
    PecaRepository
)

from app.exceptions.cliente_exceptions import (
    ClienteNaoEncontradoException
)

from app.exceptions.peca_exceptions import (
    PecaNaoEncontradaException
)

from app.exceptions.venda_exceptions import (
    VendaInvalidaException,
    EstoqueInsuficienteException
)


class VendaService:

    def __init__(
        self,
        venda_repository: VendaRepository,
        cliente_repository: ClienteRepository,
        peca_repository: PecaRepository
    ):
        self.venda_repository = venda_repository
        self.cliente_repository = cliente_repository
        self.peca_repository = peca_repository

    def listar(self):
        return self.venda_repository.listar()

    def criar(
        self,
        cliente_id: int,
        peca_id: int,
        quantidade: int,
        valor_unitario: float
    ):

        if quantidade <= 0:
            raise VendaInvalidaException(
                "Quantidade inválida"
            )

        cliente = (
            self.cliente_repository
            .buscar_por_id(cliente_id)
        )

        if not cliente:
            raise ClienteNaoEncontradoException(
                "Cliente não encontrado"
            )

        peca = (
            self.peca_repository
            .buscar_por_id(peca_id)
        )

        if not peca:
            raise PecaNaoEncontradaException(
                "Peça não encontrada"
            )

        if quantidade > peca.quantidade_estoque:
            raise EstoqueInsuficienteException(
                "Estoque insuficiente"
            )

        valor_total = (
            quantidade *
            valor_unitario
        )

        venda = Venda(
            cliente_id=cliente_id,
            peca_id=peca_id,
            quantidade=quantidade,
            valor_unitario=valor_unitario,
            valor_total=valor_total
        )

        # REGRA DE NEGÓCIO
        peca.quantidade_estoque -= quantidade

        self.venda_repository.db.commit()

        return self.venda_repository.criar(
            venda
        )
