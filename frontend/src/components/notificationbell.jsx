
import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { getUnreadNotifications } from '../api'

function NotificationBell() {
  const [count, setCount] = useState(0)

  useEffect(() => {
    getUnreadNotifications()
      .then(response => {
        setCount(response.data.length)
      })
      .catch(error => {
        console.error('Notification error:', error)
      })
  }, [])

  return (
    <Link to="/notifications" className="notification-bell">
      🔔
      {count > 0 && (
        <span className="notification-count">
          {count}
        </span>
      )}
    </Link>
  )
}

export default NotificationBell
