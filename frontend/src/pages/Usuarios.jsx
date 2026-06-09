import { useState, useEffect } from 'react'
import { getUsuarios, criarUsuario } from '../api.js'

export default function Usuarios() {
  const [usuarios, setUsuarios] = useState([])
  const [erro, setErro] = useState('')
  const [showModal, setShowModal] = useState(false)
  const [form, setForm] = useState({ nome: '', email: '', senha: '' })

  function load() { getUsuarios().then(setUsuarios).catch(e => setErro(e.message)) }
  useEffect(load, [])

  async function handleSubmit(e) {
    e.preventDefault()
    try {
      await criarUsuario(form)
      setShowModal(false)
      setForm({ nome: '', email: '', senha: '' })
      load()
    } catch (err) { setErro(err.message) }
  }

  return (
    <div>
      <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: 12 }}>
        <button className="btn-primary" onClick={() => setShowModal(true)}>+ Novo Usuário</button>
      </div>
      {erro && <div className="error">{erro}</div>}
      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID</th><th>Nome</th><th>Email</th>
            </tr>
          </thead>
          <tbody>
            {usuarios.map(u => (
              <tr key={u.id}>
                <td>{u.id}</td><td>{u.nome}</td><td>{u.email}</td>
              </tr>
            ))}
            {usuarios.length === 0 && !erro && (
              <tr><td colSpan={3} style={{ textAlign: 'center', padding: 40, color: '#888' }}>Nenhum usuário encontrado</td></tr>
            )}
          </tbody>
        </table>
      </div>
      {showModal && (
        <div className="modal-overlay" onClick={() => setShowModal(false)}>
          <div className="modal" onClick={e => e.stopPropagation()}>
            <h3>Novo Usuário</h3>
            <form onSubmit={handleSubmit}>
              <div className="modal-grid">
                <div className="field"><label>Nome</label><input value={form.nome} onChange={e => setForm(f => ({ ...f, nome: e.target.value }))} required /></div>
                <div className="field"><label>Email</label><input type="email" value={form.email} onChange={e => setForm(f => ({ ...f, email: e.target.value }))} required /></div>
                <div className="field"><label>Senha</label><input type="password" value={form.senha} onChange={e => setForm(f => ({ ...f, senha: e.target.value }))} required minLength={6} /></div>
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
