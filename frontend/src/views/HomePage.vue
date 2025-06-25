<template>
  <div class="container py-5">
    <h1 class="display-4 fw-bold mb-4">Welcome to StrokePain AI</h1>
    <p class="lead mb-4">
      <strong>StrokePain</strong> is an intelligent system that analyzes facial expressions from stroke patients to detect pain intensity — using only the unaffected side of the face. This is achieved through two advanced deep learning models: a stroke-side detector and a pain regressor trained on real patient data.
    </p>

    <!-- Sections -->
    <div class="mb-5">
      <h3 class="text-primary"> How It Works</h3>
      <ul class="list-group list-group-flush">
        <li class="list-group-item"> Detects the stroke-affected side using a CNN classifier</li>
        <li class="list-group-item"> Uses the healthy side to predict pain intensity (PSPI score)</li>
        <li class="list-group-item"> Just upload a face image, and the app handles everything</li>
      </ul>
    </div>

    <div class="mb-5">
      <h3 class="text-success"> Technical Stack</h3>
      <ul class="list-group list-group-flush">
        <li class="list-group-item"> Backend: PyTorch models (ResNet18 & Custom CNN)</li>
        <li class="list-group-item"> Deployed using Docker and Azure Cloud</li>
        <li class="list-group-item"> Frontend: Vue 3 + Bootstrap</li>
        <li class="list-group-item"> Full pipeline exposed via REST API</li>
      </ul>
    </div>

    <div class="mb-5">
      <h3 class="text-info"> Project Resources</h3>
      <div class="d-grid gap-2 d-md-flex">
        <a href="https://github.com/your-org/strokepain" class="btn btn-outline-dark" target="_blank">GitHub Repository</a>
        <router-link to="/setup" class="btn btn-outline-success">Setup Instructions</router-link>
        <router-link to="/docs" class="btn btn-outline-secondary">View Documentation</router-link>
      </div>
    </div>

    <div class="alert alert-warning mt-4">
       This tool is for academic use and medical research. Not intended for clinical diagnosis.
    </div>
  </div>
</template>

<script setup>
// No JS logic required here yet
</script>

<style scoped>
.container {
  max-width: 850px;
}
</style>
