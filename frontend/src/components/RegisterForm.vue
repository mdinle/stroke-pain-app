<template>
  <div class="container d-flex justify-content-center align-items-center min-vh-100">
    <div class="card shadow p-4" style="width: 100%; max-width: 400px;">
      <h3 class="mb-4 text-center">Register</h3>
      <form @submit.prevent="handleRegister">
        <div class="mb-3">
          <label for="username" class="form-label">Username</label>
          <input
            v-model="username"
            type="text"
            id="username"
            class="form-control"
            placeholder="Choose a username"
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
            placeholder="Choose a password"
            required
          />
        </div>

        <div class="mb-3">
          <p class="text-muted">
            Already have an account? <router-link to="/login">Login here</router-link>.
          </p>
        </div>

        <button type="submit" class="btn btn-success w-100">Register</button>

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

const router = useRouter();
const username = ref('');
const password = ref('');
const error = ref('');

async function handleRegister() {
  try {
    await AuthService.register(username.value, password.value);
    alert('Registered successfully. Please log in.');
    router.push('/login');
  } catch (e) {
    error.value = 'Registration failed. Try a different username.';
  }
}
</script>
