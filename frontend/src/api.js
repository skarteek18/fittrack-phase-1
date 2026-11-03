
import axios from 'axios'

// Create Axios instance
const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  headers: {
    'Content-Type': 'application/json'
  }
})

// Automatically attach JWT token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')

    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }

    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Handle API errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token')

      if (window.location.pathname !== '/login') {
        window.location.href = '/login'
      }
    }

    return Promise.reject(error)
  }
)

// Authentication APIs
export const registerUser = (data) =>
  api.post('/auth/register', data)

export const loginUser = (data) =>
  api.post('/auth/login', data)

export const getProfile = () =>
  api.get('/auth/me')

// Workout APIs
export const addWorkout = (data) =>
  api.post('/workouts/', data)

export const getWorkouts = () =>
  api.get('/workouts/')

export const updateWorkout = (id, data) =>
  api.put(`/workouts/${id}`, data)

export const deleteWorkout = (id) =>
  api.delete(`/workouts/${id}`)

// Progress APIs
export const getDailyProgress = (date) =>
  api.get('/progress/daily', {
    params: date ? { progress_date: date } : {}
  })

export const getProgressHistory = () =>
  api.get('/progress/history')

export const getFitnessSummary = () =>
  api.get('/progress/summary')

// Goal APIs
export const createGoal = (data) =>
  api.post('/goals/', data)

export const getGoals = () =>
  api.get('/goals/')

export const updateGoal = (id, data) =>
  api.put(`/goals/${id}`, data)

export const getGoalStatus = (id) =>
  api.get(`/goals/${id}/status`)

export const deleteGoal = (id) =>
  api.delete(`/goals/${id}`)

// Reports APIs
export const getWeeklyReport = () =>
  api.get('/reports/weekly')

export const getMonthlyReport = (year, month) =>
  api.get('/reports/monthly', {
    params: { year, month }
  })

export const getCaloriesReport = () =>
  api.get('/reports/calories')

export const getCategoryReport = () =>
  api.get('/reports/categories')

// Notification APIs
export const createNotification = (data) =>
  api.post('/notifications/', data)

export const getNotifications = () =>
  api.get('/notifications/')

export const getUnreadNotifications = () =>
  api.get('/notifications/unread')

export const markNotificationRead = (id) =>
  api.put(`/notifications/${id}/read`)

export const markNotificationUnread = (id) =>
  api.put(`/notifications/${id}/unread`)

export const deleteNotification = (id) =>
  api.delete(`/notifications/${id}`)

export const createDailyReminder = () =>
  api.post('/notifications/daily-reminder')

export const createGoalAlert = () =>
  api.post('/notifications/goal-alert')

export default api
