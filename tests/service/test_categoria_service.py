import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from unittest.mock import Mock, patch
import pytest

from app.model.categoria import Categoria
from app.service.categoria_service import CategoriaService
from app.exceptions.categoria_exceptions import (
    CategoriaNaoEncontradaException,
    CategoriaDuplicadaException
)


class TestCategoriaService:

    @pytest.fixture
    def repository(self):
        return Mock()

    @pytest.fixture
    def service(self, repository):
        return CategoriaService(repository)

    def test_listar(self, service, repository):
        repository.listar.return_value = [
            Categoria(id=1, nome="Motor"),
            Categoria(id=2, nome="Freios")
        ]
        resultado = service.listar()
        assert len(resultado) == 2
        repository.listar.assert_called_once()

    def test_buscar_por_id_encontrado(self, service, repository):
        repository.buscar_por_id.return_value = Categoria(
            id=1, nome="Motor"
        )
        resultado = service.buscar_por_id(1)
        assert resultado.id == 1
        assert resultado.nome == "Motor"

    def test_buscar_por_id_nao_encontrado(self, service, repository):
        repository.buscar_por_id.return_value = None
        with pytest.raises(CategoriaNaoEncontradaException):
            service.buscar_por_id(999)

    def test_criar_sucesso(self, service, repository):
        repository.listar.return_value = []
        repository.criar.return_value = Categoria(
            id=1, nome="Motor", descricao="Peças de motor"
        )
        resultado = service.criar("Motor", "Peças de motor")
        assert resultado.nome == "Motor"
        repository.criar.assert_called_once()

    def test_criar_nome_duplicado(self, service, repository):
        repository.listar.return_value = [
            Categoria(id=1, nome="Motor")
        ]
        with pytest.raises(CategoriaDuplicadaException):
            service.criar("Motor", "Descrição")

    def test_deletar_sucesso(self, service, repository):
        repository.buscar_por_id.return_value = Categoria(
            id=1, nome="Motor"
        )
        service.deletar(1)
        repository.deletar.assert_called_once()

    def test_deletar_nao_encontrado(self, service, repository):
        repository.buscar_por_id.return_value = None
        with pytest.raises(CategoriaNaoEncontradaException):
            service.deletar(999)
