from app.model.categoria import Categoria
from app.repository.categoria_repository import CategoriaRepository


class CategoriaService:

    def __init__(self, repository: CategoriaRepository):
        self.repository = repository

    def listar(self):
        return self.repository.listar()

    def buscar_por_id(self, categoria_id: int):
        categoria = self.repository.buscar_por_id(categoria_id)

        if not categoria:
            raise ValueError("Categoria não encontrada")

        return categoria

    def criar(self, nome: str, descricao: str | None = None):

        categorias = self.repository.listar()

        for categoria in categorias:
            if categoria.nome.lower() == nome.lower():
                raise ValueError(
                    "Já existe uma categoria com esse nome"
                )

        nova_categoria = Categoria(
            nome=nome,
            descricao=descricao
        )

        return self.repository.criar(
            nova_categoria
        )

    def atualizar(
        self,
        categoria_id: int,
        nome: str,
        descricao: str | None = None
    ):

        categoria = self.buscar_por_id(
            categoria_id
        )

        categoria.nome = nome
        categoria.descricao = descricao

        self.repository.db.commit()
        self.repository.db.refresh(categoria)

        return categoria

    def deletar(self, categoria_id: int):

        categoria = self.buscar_por_id(
            categoria_id
        )

        self.repository.deletar(categoria)
