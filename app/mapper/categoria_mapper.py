from app.model.categoria import Categoria
from app.dto.categoria_dto import (
    CategoriaResponseDTO
)


class CategoriaMapper:

    @staticmethod
    def to_dto(
        categoria: Categoria
    ) -> CategoriaResponseDTO:

        return CategoriaResponseDTO(
            id=categoria.id,
            nome=categoria.nome,
            descricao=categoria.descricao
        )
