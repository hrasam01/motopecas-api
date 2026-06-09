import { useState, useEffect } from 'react'
import { getPecas, getCategorias } from '../api.js'

export default function Pecas() {
  const [pecas, setPecas] = useState([])
  const [categorias, setCategorias] = useState([])
  const [filtro, setFiltro] = useState({ nome: '', categoria_id: '' })
  const [erro, setErro] = useState('')

  useEffect(() => {
    getCategorias().then(setCategorias).catch(() => {})
  }, [])

  useEffect(() => {
    const params = new URLSearchParams()
    if (filtro.nome) params.set('nome', filtro.nome)
    if (filtro.categoria_id) params.set('categoria_id', filtro.categoria_id)
    const query = params.toString() ? `?${params}` : ''
    getPecas(query)
      .then(setPecas)
      .catch(e => setErro(e.message))
  }, [filtro])

  return (
    <div>
      <div className="table-wrapper">
        <div className="filter-bar">
          <input
            placeholder="Buscar por nome..."
            value={filtro.nome}
            onChange={e => setFiltro(f => ({ ...f, nome: e.target.value }))}
          />
          <select
            value={filtro.categoria_id}
            onChange={e => setFiltro(f => ({ ...f, categoria_id: e.target.value }))}
            style={{ padding: '10px 14px', border: '2px solid #e0e0e0', borderRadius: 8, fontSize: 14 }}
          >
            <option value="">Todas categorias</option>
            {categorias.map(c => (
              <option key={c.id} value={c.id}>{c.nome}</option>
            ))}
          </select>
        </div>
        {erro && <div className="error" style={{ margin: 16 }}>{erro}</div>}
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Nome</th>
              <th>Preço</th>
              <th>Estoque</th>
              <th>Categoria</th>
            </tr>
          </thead>
          <tbody>
            {pecas.map(p => (
              <tr key={p.id}>
                <td>{p.id}</td>
                <td>{p.nome}</td>
                <td>R$ {Number(p.preco).toFixed(2)}</td>
                <td>{p.quantidade_estoque}</td>
                <td>{categorias.find(c => c.id === p.categoria_id)?.nome || '-'}</td>
              </tr>
            ))}
            {pecas.length === 0 && !erro && (
              <tr><td colSpan={5} style={{ textAlign: 'center', padding: 40, color: '#888' }}>Nenhuma peça encontrada</td></tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  )
}
