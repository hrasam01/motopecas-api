import { useState, useEffect } from 'react'
import { getClientes } from '../api.js'

export default function Clientes() {
  const [clientes, setClientes] = useState([])
  const [erro, setErro] = useState('')

  useEffect(() => {
    getClientes()
      .then(setClientes)
      .catch(e => setErro(e.message))
  }, [])

  return (
    <div className="table-wrapper">
      {erro && <div className="error" style={{ margin: 16 }}>{erro}</div>}
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>CPF</th>
            <th>Email</th>
            <th>Telefone</th>
            <th>Cidade</th>
            <th>Estado</th>
          </tr>
        </thead>
        <tbody>
          {clientes.map(c => (
            <tr key={c.id}>
              <td>{c.id}</td>
              <td>{c.nome}</td>
              <td>{c.cpf}</td>
              <td>{c.email}</td>
              <td>{c.telefone}</td>
              <td>{c.cidade}</td>
              <td>{c.estado}</td>
            </tr>
          ))}
          {clientes.length === 0 && !erro && (
            <tr><td colSpan={7} style={{ textAlign: 'center', padding: 40, color: '#888' }}>Nenhum cliente encontrado</td></tr>
          )}
        </tbody>
      </table>
    </div>
  )
}
