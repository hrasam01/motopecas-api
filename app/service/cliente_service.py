from app.model.cliente import Cliente

from app.repository.cliente_repository import (
    ClienteRepository
)

from app.integrations.brasil_api import (
    BrasilApi
)

from app.exceptions.cliente_exceptions import (
    ClienteNaoEncontradoException,
    ClienteJaExisteException,
    CepInvalidoException
)


class ClienteService:

    def __init__(
        self,
        repository: ClienteRepository
    ):
        self.repository = repository

    def listar(self):
        return self.repository.listar()

    def buscar_por_id(
        self,
        cliente_id: int
    ):

        cliente = self.repository.buscar_por_id(
            cliente_id
        )

        if not cliente:
            raise ClienteNaoEncontradoException(
                "Cliente não encontrado"
            )

        return cliente

    def criar(
        self,
        nome: str,
        cpf: str,
        email: str,
        telefone: str,
        cep: str
    ):

        if self.repository.buscar_por_cpf(cpf):
            raise ClienteJaExisteException(
                "CPF já cadastrado"
            )

        if self.repository.buscar_por_email(email):
            raise ClienteJaExisteException(
                "Email já cadastrado"
            )

        endereco = BrasilApi.buscar_cep(
            cep
        )

        if not endereco:
            raise CepInvalidoException(
                "CEP inválido"
            )

        cliente = Cliente(
            nome=nome,
            cpf=cpf,
            email=email,
            telefone=telefone,
            cep=cep,
            logradouro=endereco["street"],
            bairro=endereco["neighborhood"],
            cidade=endereco["city"],
            estado=endereco["state"]
        )

        return self.repository.criar(
            cliente
        )

    def deletar(
        self,
        cliente_id: int
    ):

        cliente = self.buscar_por_id(
            cliente_id
        )

        self.repository.deletar(
            cliente
        )
