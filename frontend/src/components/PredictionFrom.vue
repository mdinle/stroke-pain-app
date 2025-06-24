<template>
  <div class="container mt-5">
    <div class="card p-4 shadow-sm">
      <h3 class="mb-4">Upload Face Image</h3>
      <input type="file" class="form-control mb-3" @change="handleFile" accept="image/jpeg" />
      <button class="btn btn-primary" @click="submitImage" :disabled="!image">Submit</button>

      <div v-if="result" class="alert alert-success mt-4">
        <p><strong>Stroke Side:</strong> {{ result.stroke_side }}</p>
        <p><strong>Healthy Side:</strong> {{ result.healthy_side }}</p>
        <p><strong>Pain Score:</strong> {{ result.pain_score }}</p>
      </div>

      <div v-if="error" class="alert alert-danger mt-3">{{ error }}</div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { predictStrokeAndPain } from '@/api/predictApi'

const image = ref(null)
const result = ref(null)
const error = ref(null)

function handleFile(event) {
  image.value = event.target.files[0]
  result.value = null
  error.value = null
}

async function submitImage() {
  try {
    const response = await predictStrokeAndPain(image.value)
    result.value = response
  } catch (err) {
    error.value = err.response?.data?.detail || err.message || 'API error'
  }
}
</script>
