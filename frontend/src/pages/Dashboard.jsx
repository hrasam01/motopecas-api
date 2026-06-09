import { useState, useEffect } from 'react'
import { getDashboard } from '../api.js'

export default function Dashboard() {
  const [data, setData] = useState(null)
  const [erro, setErro] = useState('')

  useEffect(() => {
    getDashboard()
      .then(setData)
      .catch(e => setErro(e.message))
  }, [])

  if (erro) return <div className="error">{erro}</div>
  if (!data) return <div className="loading">Carregando...</div>

  const cards = [
    { label: 'Clientes', value: data.total_clientes },
    { label: 'Fornecedores', value: data.total_fornecedores },
    { label: 'Peças Cadastradas', value: data.total_pecas },
    { label: 'Compras', value: data.total_compras },
    { label: 'Vendas', value: data.total_vendas },
    { label: 'Estoque Total', value: data.estoque_total },
  ]

  return (
    <div className="cards">
      {cards.map(c => (
        <div key={c.label} className="card">
          <h3>{c.label}</h3>
          <div className="value">{c.value}</div>
        </div>
      ))}
    </div>
  )
}
