<template>
  <div class="container d-flex justify-content-center align-items-center min-vh-100">
    <div class="card shadow p-4" style="width: 100%; max-width: 400px;">
      <h3 class="mb-4 text-center">Login</h3>
      <form @submit.prevent="handleLogin">
        <div class="mb-3">
          <label for="username" class="form-label">Username</label>
          <input
            v-model="username"
            type="text"
            id="username"
            class="form-control"
            placeholder="Enter your username"
            required
          />
        </div>

        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input
            v-model="password"
            type="password"
            id="password"
            class="form-control"
            placeholder="Enter your password"
            required
          />
        </div>

        <div class="mb-3">
          <p class="text-muted">
            Don't have an account? <router-link to="/register">Register here</router-link>.
          </p>
        </div>

        <button type="submit" class="btn btn-primary w-100">Login</button>

        <div v-if="error" class="alert alert-danger mt-3" role="alert">
          {{ error }}
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import AuthService from '@/services/AuthService';
import { useAuthStore } from '@/stores/auth';

const router = useRouter();
const auth = useAuthStore();

const username = ref('');
const password = ref('');
const error = ref('');

async function handleLogin() {
  try {
    const result = await AuthService.login(username.value, password.value);
    auth.setToken(result.access_token);
    router.push('/predict');
  } catch (e) {
    error.value = 'Login failed. Please check your credentials.';
  }
}
</script>
