
import React from 'react'

function WorkoutCard({ workout, onEdit, onDelete }) {
  return (
    <div className="summary-card">
      <h3>{workout.workout_name}</h3>

      <p>Category: {workout.category}</p>
      <p>Duration: {workout.duration} minutes</p>
      <p>Calories: {workout.calories_burned} kcal</p>
      <p>Date: {workout.workout_date}</p>

      <button onClick={() => onEdit(workout)}>
        Edit
      </button>

      <button onClick={() => onDelete(workout.id)}>
        Delete
      </button>
    </div>
  )
}

export default WorkoutCard
