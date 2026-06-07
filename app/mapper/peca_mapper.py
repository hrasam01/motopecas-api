from app.model.peca import Peca
from app.dto.peca_dto import PecaResponseDTO


class PecaMapper:

    @staticmethod
    def to_dto(
        peca: Peca
    ) -> PecaResponseDTO:

        return PecaResponseDTO(
            id=peca.id,
            nome=peca.nome,
            descricao=peca.descricao,
            preco=float(peca.preco),
            quantidade_estoque=peca.quantidade_estoque,
            categoria_id=peca.categoria_id
        )
