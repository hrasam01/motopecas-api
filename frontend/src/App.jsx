import { useState } from 'react'
import Login from './pages/Login.jsx'
import Dashboard from './pages/Dashboard.jsx'
import Pecas from './pages/Pecas.jsx'
import Clientes from './pages/Clientes.jsx'
import Financeiro from './pages/Financeiro.jsx'

const PAGINAS = {
  dashboard: { titulo: 'Dashboard', componente: Dashboard },
  pecas: { titulo: 'Peças', componente: Pecas },
  clientes: { titulo: 'Clientes', componente: Clientes },
  financeiro: { titulo: 'Financeiro', componente: Financeiro },
}

export default function App() {
  const [token, setToken] = useState(localStorage.getItem('token'))
  const [pagina, setPagina] = useState('dashboard')

  if (!token) return <Login onLogin={t => { setToken(t); localStorage.setItem('token', t) }} />

  const PaginaAtual = PAGINAS[pagina].componente

  return (
    <div className="layout">
      <aside className="sidebar">
        <h1>🏍️ MotoPeças</h1>
        <nav>
          {Object.entries(PAGINAS).map(([key, p]) => (
            <button
              key={key}
              className={pagina === key ? 'active' : ''}
              onClick={() => setPagina(key)}
            >
              {p.titulo}
            </button>
          ))}
        </nav>
        <div className="logout">
          <button onClick={() => { localStorage.removeItem('token'); setToken(null) }}>
            Sair
          </button>
        </div>
      </aside>
      <main className="content">
        <h2>{PAGINAS[pagina].titulo}</h2>
        <PaginaAtual />
      </main>
    </div>
  )
}
