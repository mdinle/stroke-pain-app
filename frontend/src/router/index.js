import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/views/HomePage.vue'
import PredictPage from '@/views/PredictPage.vue'
import Docs from '@/views/Docs.vue'
import Setup from '@/views/Setup.vue'  // case sensitive!

const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/predict', name: 'Predict', component: PredictPage },
  { path: '/docs', name: 'Docs', component: Docs },
  { path: '/setup', name: 'Setup', component: Setup }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
