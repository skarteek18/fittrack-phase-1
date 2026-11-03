
import React from 'react'
import { Routes, Route, Navigate, Link, useNavigate } from 'react-router-dom'

function ProtectedRoute({ children }) {
  const token = localStorage.getItem('token')

  return token ? children : <Navigate to="/login" />
}

function Login() {
  const navigate = useNavigate()

  const [email, setEmail] = React.useState('')
  const [password, setPassword] = React.useState('')

  const handleLogin = async (e) => {
    e.preventDefault()

    try {
      const response = await fetch('http://127.0.0.1:8000/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
      })

      const data = await response.json()

      if (!response.ok) {
        alert(data.detail || 'Login failed')
        return
      }

      localStorage.setItem('token', data.access_token)
      navigate('/dashboard')

    } catch (error) {
      alert('Unable to connect to server')
    }
  }

  return (
    <div className="auth-container">
      <form className="auth-card" onSubmit={handleLogin}>
        <h1>FitTrack</h1>
        <p>Welcome Back! Login to continue.</p>

        <input
          type="email"
          placeholder="Email Address"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">Login</button>

        <p>
          Don't have an account? <Link to="/register">Register</Link>
        </p>
      </form>
    </div>
  )
}

function Register() {
  const navigate = useNavigate()

  const [username, setUsername] = React.useState('')
  const [email, setEmail] = React.useState('')
  const [password, setPassword] = React.useState('')

  const handleRegister = async (e) => {
    e.preventDefault()

    try {
      const response = await fetch('http://127.0.0.1:8000/auth/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, email, password })
      })

      const data = await response.json()

      if (!response.ok) {
        alert(data.detail || 'Registration failed')
        return
      }

      alert('Registration successful! Please login.')
      navigate('/login')

    } catch (error) {
      alert('Unable to connect to server')
    }
  }

  return (
    <div className="auth-container">
      <form className="auth-card" onSubmit={handleRegister}>
        <h1>Create Account</h1>
        <p>Join FitTrack and start your fitness journey.</p>

        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />

        <input
          type="email"
          placeholder="Email Address"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <button type="submit">Register</button>

        <p>
          Already have an account? <Link to="/login">Login</Link>
        </p>
      </form>
    </div>
  )
}

function Dashboard() {
  const navigate = useNavigate()

  const logout = () => {
    localStorage.removeItem('token')
    navigate('/login')
  }

  return (
    <div className="dashboard">
      <header className="navbar">
        <h2>FitTrack</h2>

        <nav>
          <Link to="/dashboard">Dashboard</Link>
          <Link to="/workouts">Workouts</Link>
          <Link to="/progress">Progress</Link>
          <Link to="/goals">Goals</Link>
          <Link to="/reports">Reports</Link>
          <Link to="/notifications">Notifications</Link>
        </nav>

        <button onClick={logout}>Logout</button>
      </header>

      <main className="dashboard-content">
        <h1>Welcome to FitTrack!</h1>
        <p>Track your fitness journey and achieve your goals.</p>

        <div className="summary-cards">
          <div className="summary-card">
            <h3>Total Workouts</h3>
            <h2>0</h2>
          </div>

          <div className="summary-card">
            <h3>Calories Burned</h3>
            <h2>0</h2>
          </div>

          <div className="summary-card">
            <h3>Fitness Goals</h3>
            <h2>0</h2>
          </div>

          <div className="summary-card">
            <h3>Workout Time</h3>
            <h2>0 min</h2>
          </div>
        </div>

        <div className="welcome-card">
          <h2>Stay Healthy. Stay Active.</h2>
          <p>
            Start adding workouts, monitor your daily progress,
            and achieve your fitness goals with FitTrack.
          </p>
          <Link to="/workouts" className="action-link">
            Manage Workouts
          </Link>
        </div>
      </main>
    </div>
  )
}

function ComingSoon({ title }) {
  return (
    <div className="page-container">
      <Link to="/dashboard">← Back to Dashboard</Link>
      <h1>{title}</h1>
      <p>This section is ready for implementation.</p>
    </div>
  )
}

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" />} />

      <Route path="/login" element={<Login />} />

      <Route path="/register" element={<Register />} />

      <Route
        path="/dashboard"
        element={
          <ProtectedRoute>
            <Dashboard />
          </ProtectedRoute>
        }
      />

      <Route
        path="/workouts"
        element={
          <ProtectedRoute>
            <ComingSoon title="Workout Management" />
          </ProtectedRoute>
        }
      />

      <Route
        path="/progress"
        element={
          <ProtectedRoute>
            <ComingSoon title="Daily Progress" />
          </ProtectedRoute>
        }
      />

      <Route
        path="/goals"
        element={
          <ProtectedRoute>
            <ComingSoon title="Fitness Goals" />
          </ProtectedRoute>
        }
      />

      <Route
        path="/reports"
        element={
          <ProtectedRoute>
            <ComingSoon title="Reports & Analytics" />
          </ProtectedRoute>
        }
      />

      <Route
        path="/notifications"
        element={
          <ProtectedRoute>
            <ComingSoon title="Notifications" />
          </ProtectedRoute>
        }
      />

      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  )
}

export default App
