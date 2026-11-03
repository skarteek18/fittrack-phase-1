
import React from 'react'

function SummaryCard({ title, value, icon }) {
  return (
    <div className="summary-card">
      <h3>{icon} {title}</h3>
      <h2>{value}</h2>
    </div>
  )
}

export default SummaryCard
