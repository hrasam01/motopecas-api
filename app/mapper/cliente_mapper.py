from app.model.cliente import Cliente

from app.dto.cliente_dto import (
    ClienteResponseDTO
)


class ClienteMapper:

    @staticmethod
    def to_dto(
        cliente: Cliente
    ):

        return ClienteResponseDTO(
            id=cliente.id,
            nome=cliente.nome,
            cpf=cliente.cpf,
            email=cliente.email,
            telefone=cliente.telefone,
            cep=cliente.cep,
            logradouro=cliente.logradouro,
            bairro=cliente.bairro,
            cidade=cliente.cidade,
            estado=cliente.estado
        )
