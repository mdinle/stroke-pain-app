<template>
  <div class="card p-4 shadow-sm">
    <h5 class="mb-3">Upload a face image</h5>
    <input type="file" class="form-control mb-3" @change="handleFile" accept="image/jpeg,image/png" />
    <button class="btn btn-success" @click="submitImage" :disabled="!image">Submit</button>

    <div v-if="result" class="mt-3 bg-light p-3 rounded">
      <p><strong>Stroke Side:</strong> {{ result.stroke_side }}</p>
      <p><strong>Healthy Side:</strong> {{ result.healthy_side }}</p>
      <p><strong>Pain Score:</strong> {{ result.pain_score.toFixed(2) }}</p>
    </div>

    <div v-if="error" class="alert alert-danger mt-3">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { predictStrokeAndPain } from '@/services/predictService'

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
    result.value = await predictStrokeAndPain(image.value)
    error.value = null
  } catch (err) {
    result.value = null
    error.value = err?.response?.data?.detail || err.message
  }
}
</script>
