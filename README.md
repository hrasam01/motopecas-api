# MotoPeças API

API REST para gerenciamento de uma loja de peças de motocicletas. Projeto acadêmico da disciplina de Backend.

## Dados Acadêmicos

| | |
|---|---|
| **Aluno(a)** | Hrasam Hussem Gomes Monteiro |
| **Professor(a)** | Rodrigo da Cruz Fujioka |
| **Disciplina** | Tecnologia para Back-end |
| **Instituição** | Uniesp |

## Funcionalidades

- **Categorias** — CRUD de categorias de peças
- **Peças** — CRUD com validação de preço e estoque
- **Usuários** — Cadastro com senha criptografada (bcrypt)
- **Autenticação** — Login com JWT (Bearer token)
- **Clientes** — Cadastro com consulta automática de CEP via BrasilAPI
- **Fornecedores** — Cadastro com consulta automática de CEP via BrasilAPI
- **Compras** — Registro de compras com atualização automática do estoque
- **Vendas** — Registro de vendas com baixa no estoque (valida disponibilidade)
- **Financeiro** — Resumo de compras, vendas e saldo
- **Dashboard** — Indicadores gerais (total de clientes, peças, compras, vendas, etc.)

## Tecnologias

| Camada | Tecnologia |
|--------|-----------|
| Linguagem | Python 3.12+ |
| Framework | FastAPI |
| ORM | SQLAlchemy 2 |
| Banco | PostgreSQL 15+ |
| Validação | Pydantic v2 |
| Autenticação | JWT (python-jose) |
| Senhas | bcrypt |
| Integração | BrasilAPI (consulta de CEP) |
| Documentação | Swagger (OpenAPI) |
| Testes | pytest |
| Frontend | React 19 + Vite 6 |

## Arquitetura

O projeto segue o padrão **controller → service → repository → model**, separando cada responsabilidade em camadas:

```
app/
├── controller/   # Rotas e endpoints (FastAPI routers)
├── service/      # Regras de negócio e validações
├── repository/   # Acesso a dados (SQLAlchemy queries)
├── model/        # Entidades ORM (SQLAlchemy models)
├── dto/          # Schemas de entrada/saída (Pydantic)
├── mapper/       # Conversão model → DTO
├── exceptions/   # Exceções customizadas + handlers (RFC 7807)
├── security/     # JWT, bcrypt, dependência de autenticação
├── integrations/ # Integração com APIs externas (BrasilAPI)
├── database/     # Conexão, sessão, criação de tabelas
└── config/       # Configurações via variáveis de ambiente
```

### Fluxo de requisição

```
Request → controller → service → repository → database
                          ↓
                    integrações externas (BrasilAPI)
```

### Modelo de dados (7 tabelas)

```
categorias ──┐
             ├── pecas ──┬── compras ── fornecedores
             │           └── vendas  ── clientes
             └── (referência via categoria_id)
usuarios (autenticação independente)
```

## Pré-requisitos

- Python 3.12+
- PostgreSQL 15+
- pip
- Node.js 18+ (para o frontend)

## Setup — Backend

```bash
# 1. Clonar o repositório
git clone <repo-url>
cd motopecas-api-copy

# 2. Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Configurar variáveis de ambiente
# Edite o arquivo .env com as credenciais do seu PostgreSQL
vim .env

# 5. Criar o banco de dados
psql -U postgres -c "CREATE DATABASE motopecas;"

# 6. Executar a aplicação
uvicorn main:app --reload
```

A API estará disponível em: **http://localhost:8000**

Documentação Swagger: **http://localhost:8000/docs**

## Setup — Frontend

```bash
cd frontend
npm install
npm run dev
```

O frontend estará disponível em: **http://localhost:5173**

O Vite já está configurado com proxy para redirecionar as chamadas à API (`/auth`, `/categorias`, `/pecas`, etc.) para `http://localhost:8000`.

## Variáveis de Ambiente

Arquivo `.env` na raiz do projeto:

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `DATABASE_URL` | URL de conexão do PostgreSQL | `postgresql://postgres:postgres@localhost:5432/motopecas` |
| `SECRET_KEY` | Chave secreta para assinar os tokens JWT | `senha_ultrasecreta_do_banco` |
| `ALGORITHM` | Algoritmo de criptografia do JWT | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Tempo de expiração do token em minutos | `30` |

## Dados de Demonstração

```bash
python seed.py
```

Para resetar o banco antes de popular:

```bash
python seed.py --reset
```

### O que é criado:

- **Usuário:** `admin@motopecas.com` / `admin123`
- **Categorias:** 6 (Motor e Componentes, Freios, Transmissão, Suspensão e Direção, Elétrica e Iluminação, Carroceria e Acessórios)
- **Peças:** 23 itens distribuídos entre as categorias
- **Clientes:** 5 clientes com endereços reais (SP, RJ, MG, PR, RS) e CPFs válidos
- **Fornecedores:** 3 fornecedores com CNPJs válidos
- **Compras:** 6 registros com atualização de estoque
- **Vendas:** 8 registros com baixa de estoque

## Endpoints

> **Nota:** Todos os endpoints exigem autenticação via JWT (Bearer token), exceto `POST /usuarios/` (criação) e `POST /auth/login`.

### Autenticação

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/auth/login` | Login (username=email, password=senha) → retorna JWT |

### Usuários

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/usuarios/` | Cadastrar novo usuário (sem autenticação) |
| GET | `/usuarios/` | Listar todos os usuários |

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

**Filtros disponíveis:** `?categoria_id=&preco_min=&preco_max=&nome=` (busca por nome via `ILIKE`)

### Clientes

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/clientes/` | Listar |
| POST | `/clientes/` | Criar (CEP preenchido automaticamente via BrasilAPI) |

### Fornecedores

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/fornecedores/` | Listar |
| POST | `/fornecedores/` | Criar (CEP preenchido automaticamente via BrasilAPI) |

### Compras

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/compras/` | Listar (com filtros) |
| POST | `/compras/` | Registrar — aumenta o estoque da peça |

**Filtros:** `?fornecedor_id=&peca_id=&data_inicio=&data_fim=`

### Vendas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/vendas/` | Listar (com filtros) |
| POST | `/vendas/` | Registrar — diminui o estoque da peça |

**Filtros:** `?cliente_id=&peca_id=&data_inicio=&data_fim=`

### Consultas

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/financeiro/` | Total de compras, vendas e saldo |
| GET | `/dashboard/` | Indicadores do sistema (clientes, fornecedores, peças, etc.) |

## Regras de Negócio

- Preço da peça não pode ser negativo
- Estoque não pode ser negativo
- Categoria deve existir ao criar ou atualizar uma peça
- **Compra** → `quantidade_estoque += quantidade` (aumenta o estoque)
- **Venda** → `quantidade_estoque -= quantidade` (valida se há estoque suficiente)
- CPF e CNPJ validados pelos dígitos verificadores
- CEP consultado automaticamente via BrasilAPI no cadastro de clientes e fornecedores
- Senha deve ter no mínimo 6 caracteres
- E-mail deve ser único por usuário/cliente/fornecedor

## Tratamento de Erros

Todos os erros seguem o padrão **RFC 7807** (`application/problem+json`):

```json
{
  "type": "about:blank",
  "title": "Não Encontrado",
  "status": 404,
  "detail": "Categoria não encontrada",
  "instance": "/categorias/999"
}
```

### Exceções customizadas

| Exceção | Status | Descrição |
|---------|--------|-----------|
| `CategoriaNaoEncontradaException` | 404 | Categoria inexistente |
| `CategoriaDuplicadaException` | 400 | Nome de categoria já existe |
| `PecaNaoEncontradaException` | 404 | Peça inexistente |
| `PecaPrecoInvalidoException` | 400 | Preço negativo |
| `EstoqueInvalidoException` | 400 | Estoque negativo |
| `UsuarioJaExisteException` | 400 | E-mail já cadastrado |
| `CredenciaisInvalidasException` | 401 | Login ou senha incorretos |
| `ClienteNaoEncontradoException` | 404 | Cliente inexistente |
| `ClienteJaExisteException` | 400 | CPF ou e-mail já cadastrado |
| `CepInvalidoException` | 400 | CEP não encontrado na BrasilAPI |
| `FornecedorNaoEncontradoException` | 404 | Fornecedor inexistente |
| `FornecedorJaExisteException` | 400 | CNPJ ou e-mail já cadastrado |
| `CompraInvalidaException` | 400 | Dados inválidos na compra |
| `VendaInvalidaException` | 400 | Dados inválidos na venda |
| `EstoqueInsuficienteException` | 400 | Quantidade maior que o estoque disponível |

## Testes

```bash
# Todos os testes
pytest tests/ -v

# Apenas testes de unidade (services, mappers, validators)
pytest tests/ -v --ignore=tests/controller

# Apenas testes de integração (API)
pytest tests/controller/ -v
```

Os testes de controller utilizam `TestClient` do FastAPI com `dependency_overrides` para mockar o banco e a autenticação.

## Licença

Projeto acadêmico — Uniesp
