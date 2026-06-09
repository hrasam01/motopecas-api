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

export function getDashboard() {
  return authFetch('/dashboard/')
}

export function getFinanceiro() {
  return authFetch('/financeiro/')
}

export function getCategorias() {
  return authFetch('/categorias/')
}

export function getPecas(params = '') {
  return authFetch(`/pecas/${params}`)
}

export function getClientes() {
  return authFetch('/clientes/')
}

export function getCompras(params = '') {
  return authFetch(`/compras/${params}`)
}

export function getVendas(params = '') {
  return authFetch(`/vendas/${params}`)
}
