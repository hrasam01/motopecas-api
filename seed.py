import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.database.database import SessionLocal
from app.database.base import Base
from app.database.database import engine

from app.model.categoria import Categoria
from app.model.peca import Peca
from app.model.usuario import Usuario
from app.model.cliente import Cliente
from app.model.fornecedor import Fornecedor
from app.model.compra import Compra
from app.model.venda import Venda

from app.security.password_handler import gerar_hash
from datetime import datetime


def limpar():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        db.query(Venda).delete()
        db.query(Compra).delete()
        db.query(Peca).delete()
        db.query(Cliente).delete()
        db.query(Fornecedor).delete()
        db.query(Categoria).delete()
        db.query(Usuario).delete()
        db.commit()
        print("Banco limpo com sucesso.")
    finally:
        db.close()


def seed():
    db = SessionLocal()
    try:
        usuario = Usuario(
            nome="Administrador",
            email="admin@motopecas.com",
            senha_hash=gerar_hash("admin123")
        )
        db.add(usuario)
        db.flush()

        categorias_data = [
            {"nome": "Motor e Componentes", "descricao": "Peças para motor e sistemas internos"},
            {"nome": "Freios", "descricao": "Sistemas de frenagem e componentes"},
            {"nome": "Transmissão", "descricao": "Correntes, relações e embreagens"},
            {"nome": "Suspensão e Direção", "descricao": "Amortecedores, garfos e guidões"},
            {"nome": "Elétrica e Iluminação", "descricao": "Baterias, faróis e componentes elétricos"},
            {"nome": "Carroceria e Acessórios", "descricao": "Tanques, bancos e retrovisores"},
        ]
        categorias = []
        for c in categorias_data:
            cat = Categoria(**c)
            db.add(cat)
            db.flush()
            categorias.append(cat)

        pecas_data = [
            {"nome": "Kit Junta do Motor CG 150", "descricao": "Kit completo de juntas para motor CG 150", "preco": 89.90, "quantidade_estoque": 15, "categoria_id": categorias[0].id},
            {"nome": "Pistão CG 150 63.5mm", "descricao": "Pistão para motor CG 150 com anéis", "preco": 129.90, "quantidade_estoque": 10, "categoria_id": categorias[0].id},
            {"nome": "Vela de Ignição NGK", "descricao": "Vela de ignição padrão NGK BPR6ES", "preco": 19.90, "quantidade_estoque": 50, "categoria_id": categorias[0].id},
            {"nome": "Corrente de Comando", "descricao": "Corrente de comando para CG 150", "preco": 45.00, "quantidade_estoque": 20, "categoria_id": categorias[0].id},
            {"nome": "Biela CG 150", "descricao": "Biela original para CG 150", "preco": 89.00, "quantidade_estoque": 8, "categoria_id": categorias[0].id},

            {"nome": "Pastilha de Freio Dianteira", "descricao": "Pastilha de freio para CG 150 dianteira", "preco": 35.90, "quantidade_estoque": 30, "categoria_id": categorias[1].id},
            {"nome": "Disco de Freio 240mm", "descricao": "Disco de freio dianteiro 240mm", "preco": 79.90, "quantidade_estoque": 12, "categoria_id": categorias[1].id},
            {"nome": "Cilindro Mestre de Freio", "descricao": "Cilindro mestre completo", "preco": 59.90, "quantidade_estoque": 10, "categoria_id": categorias[1].id},
            {"nome": "Lona de Freio Traseira", "descricao": "Jogo de lonas de freio traseiro", "preco": 25.00, "quantidade_estoque": 25, "categoria_id": categorias[1].id},

            {"nome": "Corrente de Transmissão 428", "descricao": "Corrente de transmissão 428 120 elos", "preco": 69.90, "quantidade_estoque": 18, "categoria_id": categorias[2].id},
            {"nome": "Relação Completa CG 150", "descricao": "Kit relação completa coroa+pinhão+corrente", "preco": 149.90, "quantidade_estoque": 7, "categoria_id": categorias[2].id},
            {"nome": "Kit Embreagem CG 150", "descricao": "Kit embreagem completo com discos e molas", "preco": 119.90, "quantidade_estoque": 6, "categoria_id": categorias[2].id},

            {"nome": "Amortecedor Traseiro CG 150", "descricao": "Amortecedor traseiro original CG 150", "preco": 159.90, "quantidade_estoque": 5, "categoria_id": categorias[3].id},
            {"nome": "Balança Traseira", "descricao": "Balança traseira completa CG 150", "preco": 199.90, "quantidade_estoque": 4, "categoria_id": categorias[3].id},
            {"nome": "Garfo Dianteiro Completo", "descricao": "Garfo dianteiro completo com bengalas", "preco": 299.90, "quantidade_estoque": 3, "categoria_id": categorias[3].id},

            {"nome": "Bateria Moura 12Ah", "descricao": "Bateria selada Moura 12V 12Ah", "preco": 189.90, "quantidade_estoque": 10, "categoria_id": categorias[4].id},
            {"nome": "Farol CG 150", "descricao": "Farol dianteiro completo CG 150", "preco": 89.90, "quantidade_estoque": 8, "categoria_id": categorias[4].id},
            {"nome": "CDI CG 150", "descricao": "Módulo CDI para CG 150", "preco": 69.90, "quantidade_estoque": 12, "categoria_id": categorias[4].id},
            {"nome": "Bobina de Ignição", "descricao": "Bobina de ignição CG 150", "preco": 45.00, "quantidade_estoque": 15, "categoria_id": categorias[4].id},

            {"nome": "Tanque de Combustível CG 150", "descricao": "Tanque de combustível CG 150 12L", "preco": 249.90, "quantidade_estoque": 4, "categoria_id": categorias[5].id},
            {"nome": "Guidão CG 150", "descricao": "Guidão original CG 150", "preco": 59.90, "quantidade_estoque": 10, "categoria_id": categorias[5].id},
            {"nome": "Retrovisor Par CG 150", "descricao": "Par de retrovisores CG 150", "preco": 39.90, "quantidade_estoque": 20, "categoria_id": categorias[5].id},
            {"nome": "Banco CG 150", "descricao": "Banco completo CG 150", "preco": 129.90, "quantidade_estoque": 6, "categoria_id": categorias[5].id},
        ]
        pecas = []
        for p in pecas_data:
            peca = Peca(**p)
            db.add(peca)
            db.flush()
            pecas.append(peca)

        clientes_data = [
            {"nome": "João Silva", "cpf": "529.982.247-25", "email": "joao.silva@email.com", "telefone": "(11) 99999-0001", "cep": "01001-000", "logradouro": "Praça da Sé", "bairro": "Sé", "cidade": "São Paulo", "estado": "SP"},
            {"nome": "Maria Santos", "cpf": "123.456.789-09", "email": "maria.santos@email.com", "telefone": "(21) 98888-0002", "cep": "20040-020", "logradouro": "Rua Primeiro de Março", "bairro": "Centro", "cidade": "Rio de Janeiro", "estado": "RJ"},
            {"nome": "Pedro Oliveira", "cpf": "987.654.321-00", "email": "pedro.oliveira@email.com", "telefone": "(31) 97777-0003", "cep": "30140-070", "logradouro": "Rua da Bahia", "bairro": "Funcionários", "cidade": "Belo Horizonte", "estado": "MG"},
            {"nome": "Ana Souza", "cpf": "111.222.333-44", "email": "ana.souza@email.com", "telefone": "(41) 96666-0004", "cep": "80010-010", "logradouro": "Praça Tiradentes", "bairro": "Centro", "cidade": "Curitiba", "estado": "PR"},
            {"nome": "Carlos Pereira", "cpf": "555.666.777-88", "email": "carlos.pereira@email.com", "telefone": "(51) 95555-0005", "cep": "90010-050", "logradouro": "Rua dos Andradas", "bairro": "Centro", "cidade": "Porto Alegre", "estado": "RS"},
        ]
        clientes = []
        for c in clientes_data:
            cliente = Cliente(**c)
            db.add(cliente)
            db.flush()
            clientes.append(cliente)

        fornecedores_data = [
            {"razao_social": "Peças Motor Brasil Ltda", "cnpj": "11.222.333/0001-44", "email": "vendas@pecasmotor.com", "telefone": "(11) 3333-0001", "cep": "01001-000", "logradouro": "Praça da Sé", "bairro": "Sé", "cidade": "São Paulo", "estado": "SP"},
            {"razao_social": "Distribuidora 2 Rodas S.A.", "cnpj": "44.555.666/0001-77", "email": "contato@2rodas.com", "telefone": "(21) 3333-0002", "cep": "20040-020", "logradouro": "Rua Primeiro de Março", "bairro": "Centro", "cidade": "Rio de Janeiro", "estado": "RJ"},
            {"razao_social": "MotoPeças Center", "cnpj": "77.888.999/0001-00", "email": "admin@motopecascenter.com", "telefone": "(31) 3333-0003", "cep": "30140-070", "logradouro": "Rua da Bahia", "bairro": "Funcionários", "cidade": "Belo Horizonte", "estado": "MG"},
        ]
        fornecedores = []
        for f in fornecedores_data:
            forn = Fornecedor(**f)
            db.add(forn)
            db.flush()
            fornecedores.append(forn)

        compras_data = [
            {"fornecedor_id": fornecedores[0].id, "peca_id": pecas[0].id, "quantidade": 10, "valor_unitario": 60.00},
            {"fornecedor_id": fornecedores[0].id, "peca_id": pecas[5].id, "quantidade": 20, "valor_unitario": 22.00},
            {"fornecedor_id": fornecedores[1].id, "peca_id": pecas[9].id, "quantidade": 15, "valor_unitario": 45.00},
            {"fornecedor_id": fornecedores[1].id, "peca_id": pecas[15].id, "quantidade": 10, "valor_unitario": 130.00},
            {"fornecedor_id": fornecedores[2].id, "peca_id": pecas[2].id, "quantidade": 50, "valor_unitario": 12.00},
            {"fornecedor_id": fornecedores[2].id, "peca_id": pecas[18].id, "quantidade": 8, "valor_unitario": 35.00},
        ]
        compras = []
        for c in compras_data:
            compra = Compra(
                fornecedor_id=c["fornecedor_id"],
                peca_id=c["peca_id"],
                quantidade=c["quantidade"],
                valor_unitario=c["valor_unitario"],
                valor_total=round(c["quantidade"] * c["valor_unitario"], 2),
                data_compra=datetime.utcnow()
            )
            db.add(compra)
            db.flush()

            peca = db.query(Peca).filter(Peca.id == c["peca_id"]).first()
            if peca:
                peca.quantidade_estoque += c["quantidade"]

            compras.append(compra)

        vendas_data = [
            {"cliente_id": clientes[0].id, "peca_id": pecas[0].id, "quantidade": 2, "valor_unitario": 89.90},
            {"cliente_id": clientes[0].id, "peca_id": pecas[5].id, "quantidade": 3, "valor_unitario": 35.90},
            {"cliente_id": clientes[1].id, "peca_id": pecas[9].id, "quantidade": 1, "valor_unitario": 69.90},
            {"cliente_id": clientes[2].id, "peca_id": pecas[15].id, "quantidade": 1, "valor_unitario": 189.90},
            {"cliente_id": clientes[2].id, "peca_id": pecas[2].id, "quantidade": 10, "valor_unitario": 19.90},
            {"cliente_id": clientes[3].id, "peca_id": pecas[18].id, "quantidade": 2, "valor_unitario": 45.00},
            {"cliente_id": clientes[4].id, "peca_id": pecas[1].id, "quantidade": 1, "valor_unitario": 129.90},
            {"cliente_id": clientes[4].id, "peca_id": pecas[6].id, "quantidade": 1, "valor_unitario": 79.90},
        ]
        for v in vendas_data:
            peca = db.query(Peca).filter(Peca.id == v["peca_id"]).first()
            if peca and peca.quantidade_estoque >= v["quantidade"]:
                venda = Venda(
                    cliente_id=v["cliente_id"],
                    peca_id=v["peca_id"],
                    quantidade=v["quantidade"],
                    valor_unitario=v["valor_unitario"],
                    valor_total=round(v["quantidade"] * v["valor_unitario"], 2),
                    data_venda=datetime.utcnow()
                )
                db.add(venda)
                peca.quantidade_estoque -= v["quantidade"]

        db.commit()
        print("=" * 50)
        print("  SEED REALIZADO COM SUCESSO!")
        print("=" * 50)
        print(f"  Usuário: admin@motopecas.com / admin123")
        print(f"  Categorias: {len(categorias)}")
        print(f"  Peças: {len(pecas)}")
        print(f"  Clientes: {len(clientes)}")
        print(f"  Fornecedores: {len(fornecedores)}")
        print(f"  Compras: {len(compras)}")
        print(f"  Vendas: {len(vendas_data)}")
        print("=" * 50)

    except Exception as e:
        db.rollback()
        print(f"ERRO: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    import sys
    if "--reset" in sys.argv:
        limpar()
    seed()
