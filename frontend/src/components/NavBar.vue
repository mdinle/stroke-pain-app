<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark px-4">
    <router-link to="/" class="navbar-brand fw-bold">
      StrokePain
    </router-link>

    <button class="navbar-toggler" type="button" @click="toggleMenu">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" :class="{ show: isMenuOpen }">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <router-link to="/" class="nav-link">Home</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/predict" class="nav-link">Predict</router-link>
        </li>
      </ul>

      <template v-if="isLoggedIn">
        <button @click="logout" class="btn btn-outline-warning ms-3">Logout</button>
      </template>
      <template v-else>
        <router-link to="/login" class="btn btn-outline-light ms-3">Login</router-link>
      </template>
    </div>
  </nav>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const isMenuOpen = ref(false)
function toggleMenu() {
  isMenuOpen.value = !isMenuOpen.value
}

const auth = useAuthStore()
const router = useRouter()

const isLoggedIn = computed(() => !!auth.token)

function logout() {
  auth.clearToken()
  router.push('/login')
}
</script>