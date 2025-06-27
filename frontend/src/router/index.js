import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth';
import HomePage from '@/views/HomePage.vue'
import PredictPage from '@/views/PredictPage.vue'
import LoginForm from '@/components/LoginForm.vue'
import RegisterForm from '@/components/RegisterForm.vue'
import Docs from '@/views/DocsPage.vue'
import Setup from '@/views/SetupPage.vue'  

const routes = [
  { path: '/', component: HomePage },
  {
    path: '/login',
    component: LoginForm,
    beforeEnter: () => {
      const auth = useAuthStore()
      if (auth.token) return '/'
    }
  },
  {
    path: '/register',
    component: RegisterForm,
    beforeEnter: () => {
      const auth = useAuthStore()
      if (auth.token) return '/'
    }
  },
  {
    path: '/predict',
    component: PredictPage,
    meta: { requiresAuth: true },
  },
  { path: '/docs', name: 'Docs', component: Docs },
  { path: '/setup', name: 'Setup', component: Setup }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const auth = useAuthStore()
  if (to.meta.requiresAuth && !auth.token) {
    next('/login')
  } else {
    next()
  }
});

export default router
