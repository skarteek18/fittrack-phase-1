
import React from 'react'
import { Link, useNavigate } from 'react-router-dom'

function Navbar() {
  const navigate = useNavigate()

  const logout = () => {
    localStorage.removeItem('token')
    navigate('/login')
  }

  return (
    <nav className="navbar">
      <h2>FitTrack</h2>

      <div className="nav-links">
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/workouts">Workouts</Link>
        <Link to="/progress">Progress</Link>
        <Link to="/goals">Goals</Link>
        <Link to="/reports">Reports</Link>
        <Link to="/notifications">Notifications</Link>
      </div>

      <button onClick={logout}>Logout</button>
    </nav>
  )
}

export default Navbar
