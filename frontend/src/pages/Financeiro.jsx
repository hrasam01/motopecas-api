import { useState, useEffect } from 'react'
import { getFinanceiro } from '../api.js'

export default function Financeiro() {
  const [data, setData] = useState(null)
  const [erro, setErro] = useState('')

  useEffect(() => {
    getFinanceiro()
      .then(setData)
      .catch(e => setErro(e.message))
  }, [])

  if (erro) return <div className="error">{erro}</div>
  if (!data) return <div className="loading">Carregando...</div>

  return (
    <div className="cards">
      <div className="card">
        <h3>Total de Compras</h3>
        <div className="value negative">R$ {Number(data.total_compras).toFixed(2)}</div>
      </div>
      <div className="card">
        <h3>Total de Vendas</h3>
        <div className="value positive">R$ {Number(data.total_vendas).toFixed(2)}</div>
      </div>
      <div className="card">
        <h3>Saldo</h3>
        <div className={`value ${data.saldo >= 0 ? 'positive' : 'negative'}`}>
          R$ {Number(data.saldo).toFixed(2)}
        </div>
      </div>
    </div>
  )
}
