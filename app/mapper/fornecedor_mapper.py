from app.model.fornecedor import Fornecedor

from app.dto.fornecedor_dto import (
    FornecedorResponseDTO
)


class FornecedorMapper:

    @staticmethod
    def to_dto(
        fornecedor: Fornecedor
    ):

        return FornecedorResponseDTO(
            id=fornecedor.id,
            razao_social=fornecedor.razao_social,
            cnpj=fornecedor.cnpj,
            email=fornecedor.email,
            telefone=fornecedor.telefone,
            cep=fornecedor.cep,
            logradouro=fornecedor.logradouro,
            bairro=fornecedor.bairro,
            cidade=fornecedor.cidade,
            estado=fornecedor.estado
        )
