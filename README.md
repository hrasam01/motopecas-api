# MotoPeças API

API REST para gerenciamento de uma loja de peças de motocicletas. Desenvolvida como projeto acadêmico da disciplina de Backend.

## Funcionalidades

- **Categorias** — CRUD de categorias de peças
- **Peças** — CRUD com validação de preço e estoque
- **Usuários** — Cadastro com senha criptografada (bcrypt)
- **Autenticação** — Login com JWT
- **Clientes** — Cadastro com consulta automática de CEP (BrasilAPI)
- **Fornecedores** — Cadastro com consulta automática de CEP
- **Compras** — Registro de compras com atualização automática do estoque
- **Vendas** — Registro de vendas com baixa no estoque
- **Financeiro** — Resumo de compras, vendas e saldo
- **Dashboard** — Indicadores gerais do sistema

## Tecnologias

| Camada | Tecnologia |
|--------|-----------|
| Linguagem | Python 3.12 |
| Framework | FastAPI |
| ORM | SQLAlchemy 2 |
| Banco | PostgreSQL |
| Validação | Pydantic v2 |
| Autenticação | JWT (python-jose) |
| Senhas | bcrypt |
| Integração | BrasilAPI (CEP) |
| Documentação | Swagger (OpenAPI) |
| Testes | pytest |

## Arquitetura

```
app/
├── controller/   # Rotas e endpoints
├── service/      # Regras de negócio
├── repository/   # Acesso a dados
├── model/        # Entidades ORM
├── dto/          # Schemas de entrada/saída
├── mapper/       # Conversão model → DTO
├── exceptions/   # Exceções customizadas + handlers
├── security/     # JWT, bcrypt, dependência de autenticação
├── integrations/ # Integração com APIs externas
├── database/     # Conexão, sessão, criação de tabelas
└── config/       # Configurações do ambiente
```

## Pré-requisitos

- Python 3.12+
- PostgreSQL 15+
- Pip

## Setup

```bash
# Clonar o repositório
git clone <repo-url>
cd motopecas-api-copy

# Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
cp .env.example .env
# Editar .env com suas credenciais do PostgreSQL

# Criar o banco de dados
psql -U postgres -c "CREATE DATABASE motopecas;"

# Executar a aplicação
uvicorn main:app --reload
```

Acessar: http://localhost:8000

Swagger: http://localhost:8000/docs

## Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `DATABASE_URL` | URL de conexão do PostgreSQL | `postgresql://postgres:postgres@localhost:5432/motopecas` |
| `SECRET_KEY` | Chave secreta para JWT | `motopecas_super_secret_key` |
| `ALGORITHM` | Algoritmo JWT | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Expiração do token | `30` |

## Dados de Demonstração

```bash
python seed.py
```

Cria:
- **Usuário:** admin@motopecas.com / admin123
- **Categorias:** 6 (Motor, Freios, Transmissão, Suspensão, Elétrica, Carroceria)
- **Peças:** 23 itens com preços e estoques
- **Clientes:** 5 clientes com endereços reais (SP, RJ, MG, PR, RS)
- **Fornecedores:** 3 fornecedores
- **Compras:** 6 registros com atualização de estoque
- **Vendas:** 8 registros com baixa de estoque

Para resetar: `python seed.py --reset`

## Endpoints

### Autenticação

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/auth/login` | Login (email + senha) → JWT |

### Categorias

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/categorias/` | Listar todas |
| GET | `/categorias/{id}` | Buscar por ID |
| POST | `/categorias/` | Criar |
| PUT | `/categorias/{id}` | Atualizar |
| DELETE | `/categorias/{id}` | Remover |

### Peças

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/pecas/` | Listar (com filtros) |
| GET | `/pecas/{id}` | Buscar por ID |
| POST | `/pecas/` | Criar |
| PUT | `/pecas/{id}` | Atualizar |
| DELETE | `/pecas/{id}` | Remover |

Filtros disponíveis: `?categoria_id=&preco_min=&preco_max=&nome=`

### Clientes

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/clientes/` | Listar |
| POST | `/clientes/` | Criar (CEP preenchido automaticamente) |

### Fornecedores

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/fornecedores/` | Listar |
| POST | `/fornecedores/` | Criar (CEP preenchido automaticamente) |

### Compras

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/compras/` | Listar (com filtros) |
| POST | `/compras/` | Registrar (aumenta estoque) |

Filtros: `?fornecedor_id=&peca_id=&data_inicio=&data_fim=`

### Vendas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/vendas/` | Listar (com filtros) |
| POST | `/vendas/` | Registrar (diminui estoque) |

Filtros: `?cliente_id=&peca_id=&data_inicio=&data_fim=`

### Consultas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/financeiro/` | Total compras, vendas e saldo |
| GET | `/dashboard/` | Indicadores do sistema |

## Regras de Negócio

- Preço de peça não pode ser negativo
- Estoque não pode ser negativo
- Categoria deve existir ao criar/atualizar peça
- **Compra** → quantidade_estoque += quantidade
- **Venda** → quantidade_estoque -= quantidade (valida estoque disponível)
- CPF e CNPJ validados pelos dígitos verificadores
- CEP consultado via BrasilAPI no cadastro de clientes e fornecedores

## Tratamento de Erros

Todos os erros seguem o padrão RFC 7807 (`application/problem+json`):

```json
{
  "type": "about:blank",
  "title": "Não Encontrado",
  "status": 404,
  "detail": "Categoria não encontrada",
  "instance": "/categorias/999"
}
```

## Testes

```bash
pytest tests/ -v
```

## Commits

```
feat: estrutura inicial e configuração FastAPI
feat: módulo categoria, peça, usuário
feat: autenticação JWT
feat: cliente e fornecedor com BrasilAPI
feat: compras e vendas com controle de estoque
feat: financeiro e dashboard
feat: filtros nas consultas
feat: custom validators (CPF, CNPJ, senha)
feat: erros no padrão RFC 7807
feat: testes unitários e de integração
feat: seed de dados
```

## Licença

Projeto acadêmico — Uniesp
