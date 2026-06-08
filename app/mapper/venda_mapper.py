from app.model.venda import Venda

from app.dto.venda_dto import (
    VendaResponseDTO
)


class VendaMapper:

    @staticmethod
    def to_dto(
        venda: Venda
    ):

        return VendaResponseDTO(
            id=venda.id,
            cliente_id=venda.cliente_id,
            peca_id=venda.peca_id,
            quantidade=venda.quantidade,
            valor_unitario=float(
                venda.valor_unitario
            ),
            valor_total=float(
                venda.valor_total
            ),
            data_venda=venda.data_venda
        )
