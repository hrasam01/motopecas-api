import { useState, useEffect } from 'react'
import { getVendas, criarVenda, getClientes, getPecas } from '../api.js'

export default function Vendas() {
  const [vendas, setVendas] = useState([])
  const [clientes, setClientes] = useState([])
  const [pecas, setPecas] = useState([])
  const [erro, setErro] = useState('')
  const [showModal, setShowModal] = useState(false)
  const [form, setForm] = useState({ cliente_id: '', peca_id: '', quantidade: '', valor_unitario: '' })

  function load() {
    getVendas().then(setVendas).catch(e => setErro(e.message))
    getClientes().then(setClientes).catch(() => {})
    getPecas().then(setPecas).catch(() => {})
  }
  useEffect(load, [])

  async function handleSubmit(e) {
    e.preventDefault()
    try {
      await criarVenda({
        cliente_id: parseInt(form.cliente_id),
        peca_id: parseInt(form.peca_id),
        quantidade: parseInt(form.quantidade),
        valor_unitario: parseFloat(form.valor_unitario)
      })
      setShowModal(false)
      setForm({ cliente_id: '', peca_id: '', quantidade: '', valor_unitario: '' })
      load()
    } catch (err) { setErro(err.message) }
  }

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: 12 }}>
        <button className="btn-primary" onClick={() => setShowModal(true)}>+ Nova Venda</button>
      </div>
      {erro && <div className="error">{erro}</div>}
      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID</th><th>Cliente</th><th>Peça</th><th>Qtd</th><th>Valor Unit.</th><th>Valor Total</th><th>Data</th>
            </tr>
          </thead>
          <tbody>
            {vendas.map(v => (
              <tr key={v.id}>
                <td>{v.id}</td>
                <td>{clientes.find(c => c.id === v.cliente_id)?.nome || v.cliente_id}</td>
                <td>{pecas.find(p => p.id === v.peca_id)?.nome || v.peca_id}</td>
                <td>{v.quantidade}</td>
                <td>R$ {Number(v.valor_unitario).toFixed(2)}</td>
                <td>R$ {Number(v.valor_total).toFixed(2)}</td>
                <td>{new Date(v.data_venda).toLocaleDateString()}</td>
              </tr>
            ))}
            {vendas.length === 0 && !erro && (
              <tr><td colSpan={7} style={{ textAlign: 'center', padding: 40, color: '#888' }}>Nenhuma venda encontrada</td></tr>
            )}
          </tbody>
        </table>
      </div>
      {showModal && (
        <div className="modal-overlay" onClick={() => setShowModal(false)}>
          <div className="modal" onClick={e => e.stopPropagation()}>
            <h3>Nova Venda</h3>
            <form onSubmit={handleSubmit}>
              <div className="modal-grid">
                <div className="field"><label>Cliente</label>
                  <select value={form.cliente_id} onChange={e => setForm(f => ({ ...f, cliente_id: e.target.value }))} required>
                    <option value="">Selecione...</option>
                    {clientes.map(c => <option key={c.id} value={c.id}>{c.nome}</option>)}
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
