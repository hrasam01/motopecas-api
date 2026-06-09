const API = ''

export async function login(email, senha) {
  const params = new URLSearchParams({ username: email, password: senha })
  const res = await fetch(`${API}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: params
  })
  if (!res.ok) throw new Error('Email ou senha inválidos')
  return res.json()
}

async function authFetch(url, options = {}) {
  const token = localStorage.getItem('token')
  const res = await fetch(`${API}${url}`, {
    ...options,
    headers: {
      ...options.headers,
      'Authorization': `Bearer ${token}`
    }
  })
  if (res.status === 204) return null
  if (res.status === 401) {
    localStorage.removeItem('token')
    window.location.reload()
    throw new Error('Sessão expirada')
  }
  if (!res.ok) {
    const body = await res.json().catch(() => ({}))
    throw new Error(body.detail || body.detail?.[0]?.msg || 'Erro na requisição')
  }
  return res.json()
}

export function getDashboard() { return authFetch('/dashboard/') }
export function getFinanceiro() { return authFetch('/financeiro/') }
export function getCategorias() { return authFetch('/categorias/') }

export function getPecas(params = '') { return authFetch(`/pecas/${params}`) }
export function getPeca(id) { return authFetch(`/pecas/${id}`) }
export function criarPeca(data) { return authFetch('/pecas/', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) }) }
export function atualizarPeca(id, data) { return authFetch(`/pecas/${id}`, { method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) }) }

export function getClientes() { return authFetch('/clientes/') }
export function criarCliente(data) { return authFetch('/clientes/', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) }) }

export function getFornecedores() { return authFetch('/fornecedores/') }
export function criarFornecedor(data) { return authFetch('/fornecedores/', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) }) }

export function getCompras(params = '') { return authFetch(`/compras/${params}`) }
export function criarCompra(data) { return authFetch('/compras/', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) }) }

export function getVendas(params = '') { return authFetch(`/vendas/${params}`) }
export function criarVenda(data) { return authFetch('/vendas/', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) }) }

export function getUsuarios() { return authFetch('/usuarios/') }
export function criarUsuario(data) { return authFetch('/usuarios/', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) }) }
