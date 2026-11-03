
import React from 'react'
import { NavLink } from 'react-router-dom'

function Sidebar() {
  return (
    <aside className="sidebar">
      <h2>FitTrack</h2>

      <NavLink to="/dashboard">Dashboard</NavLink>
      <NavLink to="/workouts">Workouts</NavLink>
      <NavLink to="/progress">Progress</NavLink>
      <NavLink to="/goals">Fitness Goals</NavLink>
      <NavLink to="/reports">Reports</NavLink>
      <NavLink to="/notifications">Notifications</NavLink>
    </aside>
  )
}

export default Sidebar
