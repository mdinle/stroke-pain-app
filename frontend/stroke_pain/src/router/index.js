import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import PredictPage from '@/views/PredictPage.vue'

const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/predict', name: 'Predict', component: PredictPage }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
