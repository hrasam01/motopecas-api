import { useState, useEffect } from 'react'
import { getFornecedores, criarFornecedor } from '../api.js'

export default function Fornecedores() {
  const [fornecedores, setFornecedores] = useState([])
  const [erro, setErro] = useState('')
  const [showModal, setShowModal] = useState(false)
  const [form, setForm] = useState({ razao_social: '', cnpj: '', email: '', telefone: '', cep: '' })

  function load() { getFornecedores().then(setFornecedores).catch(e => setErro(e.message)) }
  useEffect(load, [])

  async function handleSubmit(e) {
    e.preventDefault()
    try {
      await criarFornecedor(form)
      setShowModal(false)
      setForm({ razao_social: '', cnpj: '', email: '', telefone: '', cep: '' })
      load()
    } catch (err) { setErro(err.message) }
  }

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: 12 }}>
        <button className="btn-primary" onClick={() => setShowModal(true)}>+ Novo Fornecedor</button>
      </div>
      {erro && <div className="error">{erro}</div>}
      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID</th><th>Razão Social</th><th>CNPJ</th><th>Email</th><th>Telefone</th><th>Cidade</th><th>Estado</th>
            </tr>
          </thead>
          <tbody>
            {fornecedores.map(f => (
              <tr key={f.id}>
                <td>{f.id}</td><td>{f.razao_social}</td><td>{f.cnpj}</td><td>{f.email}</td><td>{f.telefone}</td><td>{f.cidade}</td><td>{f.estado}</td>
              </tr>
            ))}
            {fornecedores.length === 0 && !erro && (
              <tr><td colSpan={7} style={{ textAlign: 'center', padding: 40, color: '#888' }}>Nenhum fornecedor encontrado</td></tr>
            )}
          </tbody>
        </table>
      </div>
      {showModal && (
        <div className="modal-overlay" onClick={() => setShowModal(false)}>
          <div className="modal" onClick={e => e.stopPropagation()}>
            <h3>Novo Fornecedor</h3>
            <form onSubmit={handleSubmit}>
              <div className="modal-grid">
                <div className="field"><label>Razão Social</label><input value={form.razao_social} onChange={e => setForm(f => ({ ...f, razao_social: e.target.value }))} required /></div>
                <div className="field"><label>CNPJ</label><input value={form.cnpj} onChange={e => setForm(f => ({ ...f, cnpj: e.target.value }))} required placeholder="00.000.000/0000-00" /></div>
                <div className="field"><label>Email</label><input type="email" value={form.email} onChange={e => setForm(f => ({ ...f, email: e.target.value }))} required /></div>
                <div className="field"><label>Telefone</label><input value={form.telefone} onChange={e => setForm(f => ({ ...f, telefone: e.target.value }))} required /></div>
                <div className="field"><label>CEP</label><input value={form.cep} onChange={e => setForm(f => ({ ...f, cep: e.target.value }))} required placeholder="00000-000" /></div>
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
