import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from datetime import datetime

from app.model.categoria import Categoria
from app.model.peca import Peca
from app.model.cliente import Cliente
from app.model.fornecedor import Fornecedor
from app.model.compra import Compra
from app.model.venda import Venda

from app.mapper.categoria_mapper import CategoriaMapper
from app.mapper.peca_mapper import PecaMapper
from app.mapper.cliente_mapper import ClienteMapper
from app.mapper.fornecedor_mapper import FornecedorMapper
from app.mapper.compra_mapper import CompraMapper
from app.mapper.venda_mapper import VendaMapper


class TestCategoriaMapper:

    def test_to_dto(self):
        model = Categoria(id=1, nome="Motor", descricao="Peças de motor")
        dto = CategoriaMapper.to_dto(model)
        assert dto.id == 1
        assert dto.nome == "Motor"
        assert dto.descricao == "Peças de motor"

    def test_to_dto_sem_descricao(self):
        model = Categoria(id=2, nome="Freios")
        dto = CategoriaMapper.to_dto(model)
        assert dto.id == 2
        assert dto.nome == "Freios"
        assert dto.descricao is None


class TestPecaMapper:

    def test_to_dto(self):
        model = Peca(
            id=1, nome="Pastilha de Freio",
            descricao="Pastilha original",
            preco=35.90, quantidade_estoque=10,
            categoria_id=1
        )
        dto = PecaMapper.to_dto(model)
        assert dto.id == 1
        assert dto.nome == "Pastilha de Freio"
        assert dto.preco == 35.90
        assert dto.quantidade_estoque == 10
        assert dto.categoria_id == 1


class TestClienteMapper:

    def test_to_dto(self):
        model = Cliente(
            id=1, nome="João", cpf="529.982.247-25",
            email="joao@email.com", telefone="(11) 99999-0000",
            cep="01001-000", logradouro="Rua A",
            bairro="Centro", cidade="São Paulo", estado="SP"
        )
        dto = ClienteMapper.to_dto(model)
        assert dto.id == 1
        assert dto.nome == "João"
        assert dto.cpf == "529.982.247-25"
        assert dto.estado == "SP"


class TestFornecedorMapper:

    def test_to_dto(self):
        model = Fornecedor(
            id=1, razao_social="Fornecedor Ltda",
            cnpj="06.215.096/0001-91",
            email="contato@fornecedor.com",
            telefone="(11) 3333-0000",
            cep="01001-000", logradouro="Rua B",
            bairro="Centro", cidade="São Paulo", estado="SP"
        )
        dto = FornecedorMapper.to_dto(model)
        assert dto.id == 1
        assert dto.razao_social == "Fornecedor Ltda"
        assert dto.cnpj == "06.215.096/0001-91"


class TestCompraMapper:

    def test_to_dto(self):
        model = Compra(
            id=1, fornecedor_id=1, peca_id=1,
            quantidade=10, valor_unitario=50.0,
            valor_total=500.0, data_compra=datetime(2026, 6, 9)
        )
        dto = CompraMapper.to_dto(model)
        assert dto.id == 1
        assert dto.quantidade == 10
        assert dto.valor_total == 500.0


class TestVendaMapper:

    def test_to_dto(self):
        model = Venda(
            id=1, cliente_id=1, peca_id=1,
            quantidade=2, valor_unitario=89.90,
            valor_total=179.80, data_venda=datetime(2026, 6, 9)
        )
        dto = VendaMapper.to_dto(model)
        assert dto.id == 1
        assert dto.quantidade == 2
        assert dto.valor_total == 179.80
