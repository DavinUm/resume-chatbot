import { useState } from 'react'

function App() {
  const [status, setStatus] = useState('idle')

  const checkHealth = async () => {
    setStatus('loading')
    try {
      const res = await fetch('http://localhost:8000/health')
      const data = await res.json()
      setStatus(data.status === 'ok' ? 'connected' : 'error')
    } catch {
      setStatus('error')
    }
  }

  return (
    <div style={{ padding: '2rem', fontFamily: 'system-ui' }}>
      <h1>AI Resume Chatbot</h1>
      <p>Frontend connected to FastAPI backend.</p>
      <button
        onClick={checkHealth}
        disabled={status === 'loading'}
        style={{ padding: '0.5rem 1rem', cursor: 'pointer' }}
      >
        {status === 'loading' && 'Checking...'}
        {status === 'idle' && 'Check API Health'}
        {status === 'connected' && '✓ Backend connected'}
        {status === 'error' && '✗ Backend unreachable'}
      </button>
    </div>
  )
}

export default App
