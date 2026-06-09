import { useState } from 'react'
import { login } from '../api.js'

export default function Login({ onLogin }) {
  const [email, setEmail] = useState('admin@motopecas.com')
  const [senha, setSenha] = useState('admin123')
  const [erro, setErro] = useState('')
  const [carregando, setCarregando] = useState(false)

  async function handleSubmit(e) {
    e.preventDefault()
    setErro('')
    setCarregando(true)
    try {
      const data = await login(email, senha)
      onLogin(data.access_token)
    } catch (err) {
      setErro(err.message)
    } finally {
      setCarregando(false)
    }
  }

  return (
    <div className="login-page">
      <form className="login-card" onSubmit={handleSubmit}>
        <h1>🏍️ MotoPeças</h1>
        <p>Faça login para acessar o sistema</p>
        {erro && <div className="error">{erro}</div>}
        <div className="field">
          <label>Email</label>
          <input type="email" value={email} onChange={e => setEmail(e.target.value)} required />
        </div>
        <div className="field">
          <label>Senha</label>
          <input type="password" value={senha} onChange={e => setSenha(e.target.value)} required />
        </div>
        <button type="submit" disabled={carregando}>
          {carregando ? 'Entrando...' : 'Entrar'}
        </button>
      </form>
    </div>
  )
}
