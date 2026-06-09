import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/auth': 'http://localhost:8000',
      '/categorias': 'http://localhost:8000',
      '/pecas': 'http://localhost:8000',
      '/clientes': 'http://localhost:8000',
      '/fornecedores': 'http://localhost:8000',
      '/compras': 'http://localhost:8000',
      '/vendas': 'http://localhost:8000',
      '/financeiro': 'http://localhost:8000',
      '/dashboard': 'http://localhost:8000',
      '/usuarios': 'http://localhost:8000',
    }
  }
})
