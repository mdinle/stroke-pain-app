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
  </div>
</nav>
</template>

<script setup>
import { ref } from 'vue'

const isMenuOpen = ref(false)

function toggleMenu() {
  isMenuOpen.value = !isMenuOpen.value
}
</script>