import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from unittest.mock import Mock
import pytest

from app.model.peca import Peca
from app.model.categoria import Categoria
from app.service.peca_service import PecaService
from app.exceptions.peca_exceptions import (
    PecaNaoEncontradaException,
    PecaPrecoInvalidoException,
    EstoqueInvalidoException
)
from app.exceptions.categoria_exceptions import (
    CategoriaNaoEncontradaException
)


class TestPecaService:

    @pytest.fixture
    def peca_repository(self):
        return Mock()

    @pytest.fixture
    def categoria_repository(self):
        return Mock()

    @pytest.fixture
    def service(self, peca_repository, categoria_repository):
        return PecaService(peca_repository, categoria_repository)

    def test_criar_sucesso(self, service, peca_repository, categoria_repository):
        categoria_repository.buscar_por_id.return_value = Categoria(
            id=1, nome="Motor"
        )
        peca_repository.criar.return_value = Peca(
            id=1, nome="Vela NGK", preco=19.90,
            quantidade_estoque=50, categoria_id=1
        )
        resultado = service.criar(
            nome="Vela NGK",
            descricao="Vela de ignição",
            preco=19.90,
            quantidade_estoque=50,
            categoria_id=1
        )
        assert resultado.nome == "Vela NGK"
        assert resultado.preco == 19.90

    def test_criar_preco_negativo(self, service, peca_repository, categoria_repository):
        categoria_repository.buscar_por_id.return_value = Categoria(
            id=1, nome="Motor"
        )
        with pytest.raises(PecaPrecoInvalidoException):
            service.criar("Teste", "", -10, 10, 1)

    def test_criar_estoque_negativo(self, service, peca_repository, categoria_repository):
        categoria_repository.buscar_por_id.return_value = Categoria(
            id=1, nome="Motor"
        )
        with pytest.raises(EstoqueInvalidoException):
            service.criar("Teste", "", 10, -1, 1)

    def test_criar_categoria_inexistente(self, service, peca_repository, categoria_repository):
        categoria_repository.buscar_por_id.return_value = None
        with pytest.raises(CategoriaNaoEncontradaException):
            service.criar("Teste", "", 10, 10, 999)

    def test_buscar_por_id_nao_encontrado(self, service, peca_repository):
        peca_repository.buscar_por_id.return_value = None
        with pytest.raises(PecaNaoEncontradaException):
            service.buscar_por_id(999)
