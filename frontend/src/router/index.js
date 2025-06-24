import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import PredictPage from '@/views/PredictPage.vue'
import Docs from '@/views/Docs.vue'


const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/predict', name: 'Predict', component: PredictPage },
  { path: '/docs', name: 'Docs', component: Docs }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
