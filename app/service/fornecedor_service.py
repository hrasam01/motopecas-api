from app.model.fornecedor import Fornecedor

from app.repository.fornecedor_repository import (
    FornecedorRepository
)

from app.integrations.brasil_api import (
    BrasilApi
)

from app.exceptions.fornecedor_exceptions import (
    FornecedorNaoEncontradoException,
    FornecedorJaExisteException
)

from app.exceptions.cliente_exceptions import (
    CepInvalidoException
)


class FornecedorService:

    def __init__(
        self,
        repository: FornecedorRepository
    ):
        self.repository = repository

    def listar(self):
        return self.repository.listar()

    def criar(
        self,
        razao_social: str,
        cnpj: str,
        email: str,
        telefone: str,
        cep: str
    ):

        if self.repository.buscar_por_cnpj(cnpj):
            raise FornecedorJaExisteException(
                "CNPJ já cadastrado"
            )

        if self.repository.buscar_por_email(email):
            raise FornecedorJaExisteException(
                "Email já cadastrado"
            )

        endereco = BrasilApi.buscar_cep(
            cep
        )

        if not endereco:
            raise CepInvalidoException(
                "CEP inválido"
            )

        fornecedor = Fornecedor(
            razao_social=razao_social,
            cnpj=cnpj,
            email=email,
            telefone=telefone,
            cep=cep,
            logradouro=endereco["street"],
            bairro=endereco["neighborhood"],
            cidade=endereco["city"],
            estado=endereco["state"]
        )

        return self.repository.criar(
            fornecedor
        )
