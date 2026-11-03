
import React from 'react'

function GoalCard({ goal }) {
  const percentage = Math.min(
    (goal.current_value / goal.target_value) * 100,
    100
  )

  return (
    <div className="summary-card">
      <h3>{goal.goal_type}</h3>

      <p>Target: {goal.target_value}</p>
      <p>Current: {goal.current_value}</p>

      <div className="progress-bar">
        <div
          className="progress-fill"
          style={{ width: `${percentage}%` }}
        />
      </div>

      <p>{percentage.toFixed(1)}% Completed</p>
      <p>Deadline: {goal.deadline}</p>
    </div>
  )
}

export default GoalCard
