from app.model.peca import Peca

from app.repository.peca_repository import (
    PecaRepository
)

from app.repository.categoria_repository import (
    CategoriaRepository
)

from app.exceptions.categoria_exceptions import (
    CategoriaNaoEncontradaException
)

from app.exceptions.peca_exceptions import (
    PecaNaoEncontradaException,
    PecaPrecoInvalidoException,
    EstoqueInvalidoException
)


class PecaService:

    def __init__(
        self,
        peca_repository: PecaRepository,
        categoria_repository: CategoriaRepository
    ):
        self.peca_repository = peca_repository
        self.categoria_repository = categoria_repository

    def listar(self):
        return self.peca_repository.listar()

    def buscar_por_id(self, peca_id: int):

        peca = self.peca_repository.buscar_por_id(
            peca_id
        )

        if not peca:
            raise PecaNaoEncontradaException(
                "Peça não encontrada"
            )

        return peca

    def criar(
        self,
        nome: str,
        descricao: str | None,
        preco: float,
        quantidade_estoque: int,
        categoria_id: int
    ):

        if preco < 0:
            raise PecaPrecoInvalidoException(
                "Preço não pode ser negativo"
            )

        if quantidade_estoque < 0:
            raise EstoqueInvalidoException(
                "Estoque não pode ser negativo"
            )

        categoria = (
            self.categoria_repository
            .buscar_por_id(categoria_id)
        )

        if not categoria:
            raise CategoriaNaoEncontradaException(
                "Categoria não encontrada"
            )

        nova_peca = Peca(
            nome=nome,
            descricao=descricao,
            preco=preco,
            quantidade_estoque=quantidade_estoque,
            categoria_id=categoria_id
        )

        return self.peca_repository.criar(
            nova_peca
        )

    def atualizar(
        self,
        peca_id: int,
        nome: str,
        descricao: str | None,
        preco: float,
        quantidade_estoque: int,
        categoria_id: int
    ):

        peca = self.buscar_por_id(peca_id)

        if preco < 0:
            raise PecaPrecoInvalidoException(
                "Preço não pode ser negativo"
            )

        if quantidade_estoque < 0:
            raise EstoqueInvalidoException(
                "Estoque não pode ser negativo"
            )

        categoria = (
            self.categoria_repository
            .buscar_por_id(categoria_id)
        )

        if not categoria:
            raise CategoriaNaoEncontradaException(
                "Categoria não encontrada"
            )

        peca.nome = nome
        peca.descricao = descricao
        peca.preco = preco
        peca.quantidade_estoque = quantidade_estoque
        peca.categoria_id = categoria_id

        self.peca_repository.db.commit()
        self.peca_repository.db.refresh(peca)

        return peca

    def deletar(self, peca_id: int):

        peca = self.buscar_por_id(peca_id)

        self.peca_repository.deletar(peca)
