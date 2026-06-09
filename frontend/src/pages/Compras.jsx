import { useState, useEffect } from 'react'
import { getCompras, criarCompra, getFornecedores, getPecas } from '../api.js'

export default function Compras() {
  const [compras, setCompras] = useState([])
  const [fornecedores, setFornecedores] = useState([])
  const [pecas, setPecas] = useState([])
  const [erro, setErro] = useState('')
  const [showModal, setShowModal] = useState(false)
  const [form, setForm] = useState({ fornecedor_id: '', peca_id: '', quantidade: '', valor_unitario: '' })

  function load() {
    getCompras().then(setCompras).catch(e => setErro(e.message))
    getFornecedores().then(setFornecedores).catch(() => {})
    getPecas().then(setPecas).catch(() => {})
  }
  useEffect(load, [])

  async function handleSubmit(e) {
    e.preventDefault()
    try {
      await criarCompra({
        fornecedor_id: parseInt(form.fornecedor_id),
        peca_id: parseInt(form.peca_id),
        quantidade: parseInt(form.quantidade),
        valor_unitario: parseFloat(form.valor_unitario)
      })
      setShowModal(false)
      setForm({ fornecedor_id: '', peca_id: '', quantidade: '', valor_unitario: '' })
      load()
    } catch (err) { setErro(err.message) }
  }

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: 12 }}>
        <button className="btn-primary" onClick={() => setShowModal(true)}>+ Nova Compra</button>
      </div>
      {erro && <div className="error">{erro}</div>}
      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID</th><th>Fornecedor</th><th>Peça</th><th>Qtd</th><th>Valor Unit.</th><th>Valor Total</th><th>Data</th>
            </tr>
          </thead>
          <tbody>
            {compras.map(c => (
              <tr key={c.id}>
                <td>{c.id}</td>
                <td>{fornecedores.find(f => f.id === c.fornecedor_id)?.razao_social || c.fornecedor_id}</td>
                <td>{pecas.find(p => p.id === c.peca_id)?.nome || c.peca_id}</td>
                <td>{c.quantidade}</td>
                <td>R$ {Number(c.valor_unitario).toFixed(2)}</td>
                <td>R$ {Number(c.valor_total).toFixed(2)}</td>
                <td>{new Date(c.data_compra).toLocaleDateString()}</td>
              </tr>
            ))}
            {compras.length === 0 && !erro && (
              <tr><td colSpan={7} style={{ textAlign: 'center', padding: 40, color: '#888' }}>Nenhuma compra encontrada</td></tr>
            )}
          </tbody>
        </table>
      </div>
      {showModal && (
        <div className="modal-overlay" onClick={() => setShowModal(false)}>
          <div className="modal" onClick={e => e.stopPropagation()}>
            <h3>Nova Compra</h3>
            <form onSubmit={handleSubmit}>
              <div className="modal-grid">
                <div className="field"><label>Fornecedor</label>
                  <select value={form.fornecedor_id} onChange={e => setForm(f => ({ ...f, fornecedor_id: e.target.value }))} required>
                    <option value="">Selecione...</option>
                    {fornecedores.map(f => <option key={f.id} value={f.id}>{f.razao_social}</option>)}
                  </select>
                </div>
                <div className="field"><label>Peça</label>
                  <select value={form.peca_id} onChange={e => setForm(f => ({ ...f, peca_id: e.target.value }))} required>
                    <option value="">Selecione...</option>
                    {pecas.map(p => <option key={p.id} value={p.id}>{p.nome}</option>)}
                  </select>
                </div>
                <div className="field"><label>Quantidade</label><input type="number" min="1" value={form.quantidade} onChange={e => setForm(f => ({ ...f, quantidade: e.target.value }))} required /></div>
                <div className="field"><label>Valor Unitário</label><input type="number" step="0.01" min="0" value={form.valor_unitario} onChange={e => setForm(f => ({ ...f, valor_unitario: e.target.value }))} required /></div>
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
