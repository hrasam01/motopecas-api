from app.model.compra import Compra

from app.dto.compra_dto import (
    CompraResponseDTO
)


class CompraMapper:

    @staticmethod
    def to_dto(
        compra: Compra
    ):

        return CompraResponseDTO(
            id=compra.id,
            fornecedor_id=compra.fornecedor_id,
            peca_id=compra.peca_id,
            quantidade=compra.quantidade,
            valor_unitario=float(
                compra.valor_unitario
            ),
            valor_total=float(
                compra.valor_total
            ),
            data_compra=compra.data_compra
        )
