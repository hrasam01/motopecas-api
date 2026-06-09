import { useState, useEffect } from 'react'
import { getPecas, getCategorias, criarPeca, atualizarPeca } from '../api.js'

const INITIAL_FORM = { nome: '', descricao: '', preco: '', quantidade_estoque: '', categoria_id: '' }

export default function Pecas() {
  const [pecas, setPecas] = useState([])
  const [categorias, setCategorias] = useState([])
  const [filtro, setFiltro] = useState({ nome: '', categoria_id: '' })
  const [erro, setErro] = useState('')
  const [showModal, setShowModal] = useState(false)
  const [editingId, setEditingId] = useState(null)
  const [form, setForm] = useState(INITIAL_FORM)

  useEffect(() => { getCategorias().then(setCategorias).catch(() => {}) }, [])

  function load() {
    const params = new URLSearchParams()
    if (filtro.nome) params.set('nome', filtro.nome)
    if (filtro.categoria_id) params.set('categoria_id', filtro.categoria_id)
    const query = params.toString() ? `?${params}` : ''
    getPecas(query).then(setPecas).catch(e => setErro(e.message))
  }
  useEffect(load, [filtro])

  function openCreate() {
    setEditingId(null)
    setForm(INITIAL_FORM)
    setShowModal(true)
  }

  function openEdit(peca) {
    setEditingId(peca.id)
    setForm({
      nome: peca.nome,
      descricao: peca.descricao || '',
      preco: String(peca.preco),
      quantidade_estoque: String(peca.quantidade_estoque),
      categoria_id: String(peca.categoria_id)
    })
    setShowModal(true)
  }

  async function handleSubmit(e) {
    e.preventDefault()
    try {
      const data = {
        nome: form.nome,
        descricao: form.descricao || null,
        preco: parseFloat(form.preco),
        quantidade_estoque: parseInt(form.quantidade_estoque),
        categoria_id: parseInt(form.categoria_id)
      }
      if (editingId) await atualizarPeca(editingId, data)
      else await criarPeca(data)
      setShowModal(false)
      load()
    } catch (err) { setErro(err.message) }
  }

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: 12 }}>
        <button className="btn-primary" onClick={openCreate}>+ Nova Peça</button>
      </div>
      <div className="table-wrapper">
        <div className="filter-bar">
          <input placeholder="Buscar por nome..." value={filtro.nome} onChange={e => setFiltro(f => ({ ...f, nome: e.target.value }))} />
          <select value={filtro.categoria_id} onChange={e => setFiltro(f => ({ ...f, categoria_id: e.target.value }))} style={{ padding: '10px 14px', border: '2px solid #e0e0e0', borderRadius: 8, fontSize: 14 }}>
            <option value="">Todas categorias</option>
            {categorias.map(c => <option key={c.id} value={c.id}>{c.nome}</option>)}
          </select>
        </div>
        {erro && <div className="error" style={{ margin: 16 }}>{erro}</div>}
        <table>
          <thead>
            <tr>
              <th>ID</th><th>Nome</th><th>Preço</th><th>Estoque</th><th>Categoria</th><th>Ações</th>
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
                <td><button className="btn-small" onClick={() => openEdit(p)}>Editar</button></td>
              </tr>
            ))}
            {pecas.length === 0 && !erro && (
              <tr><td colSpan={6} style={{ textAlign: 'center', padding: 40, color: '#888' }}>Nenhuma peça encontrada</td></tr>
            )}
          </tbody>
        </table>
      </div>
      {showModal && (
        <div className="modal-overlay" onClick={() => setShowModal(false)}>
          <div className="modal" onClick={e => e.stopPropagation()}>
            <h3>{editingId ? 'Editar Peça' : 'Nova Peça'}</h3>
            <form onSubmit={handleSubmit}>
              <div className="modal-grid">
                <div className="field"><label>Nome</label><input value={form.nome} onChange={e => setForm(f => ({ ...f, nome: e.target.value }))} required /></div>
                <div className="field"><label>Descrição</label><input value={form.descricao} onChange={e => setForm(f => ({ ...f, descricao: e.target.value }))} /></div>
                <div className="field"><label>Preço</label><input type="number" step="0.01" min="0" value={form.preco} onChange={e => setForm(f => ({ ...f, preco: e.target.value }))} required /></div>
                <div className="field"><label>Estoque</label><input type="number" min="0" value={form.quantidade_estoque} onChange={e => setForm(f => ({ ...f, quantidade_estoque: e.target.value }))} required /></div>
                <div className="field"><label>Categoria</label>
                  <select value={form.categoria_id} onChange={e => setForm(f => ({ ...f, categoria_id: e.target.value }))} required>
                    <option value="">Selecione...</option>
                    {categorias.map(c => <option key={c.id} value={c.id}>{c.nome}</option>)}
                  </select>
                </div>
              </div>
              <div className="modal-actions">
                <button type="button" className="btn-secondary" onClick={() => setShowModal(false)}>Cancelar</button>
                <button type="submit" className="btn-primary">Salvar</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  )
}
