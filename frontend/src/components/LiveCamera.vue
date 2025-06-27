<template>
  <div class="d-flex flex-wrap gap-4 align-items-start">
    <!-- Videoframe met overlay canvas voor gezichtsdetectie -->
    <div class="position-relative border rounded shadow">
      <video ref="video" autoplay muted playsinline width="640" height="480" class="rounded"></video>
      <canvas ref="canvas" width="640" height="480" class="position-absolute top-0 start-0"></canvas>
    </div>

    <!-- Resultaat van de voorspelling -->
    <div v-if="result" class="bg-light p-3 rounded shadow" style="min-width: 260px">
      <h5>Live Prediction</h5>
      <p><strong>Stroke Side:</strong> {{ result.stroke_side }}</p>
      <p><strong>Healthy Side:</strong> {{ result.healthy_side }}</p>
      <p><strong>Pain Score:</strong> {{ result.pain_score.toFixed(2) }}</p>
    </div>

    <!-- Foutmelding indien aanwezig -->
    <div v-if="error" class="alert alert-danger mt-3">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import * as faceapi from 'face-api.js'
import { predictStrokeAndPain } from '@/services/predictService'

// Refs voor videostream en canvas-overlay
const video = ref(null)
const canvas = ref(null)

// Reactieve variabelen voor resultaat en fouten
const result = ref(null)
const error = ref(null)

let interval = null // Interval voor periodieke detectie

// Detecteert gezicht en stuurt gezichtsafbeelding naar predictie-API
async function detectAndPredict() {
  const options = new faceapi.TinyFaceDetectorOptions()
  const detection = await faceapi.detectSingleFace(video.value, options)

  // Teken canvas leeg
  const ctx = canvas.value.getContext('2d')
  ctx.clearRect(0, 0, canvas.value.width, canvas.value.height)

  if (detection) {
    // Teken kader rond gedetecteerd gezicht
    const { x, y, width, height } = detection.box
    ctx.strokeStyle = 'lime'
    ctx.lineWidth = 2
    ctx.strokeRect(x, y, width, height)

    // Crop gezicht uit videobeeld
    const faceCanvas = document.createElement('canvas')
    faceCanvas.width = width
    faceCanvas.height = height
    faceCanvas.getContext('2d').drawImage(video.value, x, y, width, height, 0, 0, width, height)

    // Converteer naar blob voor verzending
    const blob = await new Promise(resolve => faceCanvas.toBlob(resolve, 'image/jpeg'))

    try {
      // Verstuur afbeelding naar API en sla resultaat op
      result.value = await predictStrokeAndPain(blob)
      error.value = null
    } catch (err) {
      // Toon foutmelding bij mislukking
      result.value = null
      error.value = err?.response?.data?.detail || 'Prediction failed'
    }
  } else {
    // Geen gezicht gedetecteerd
    error.value = 'No face detected'
  }
}

// Start webcam en begin met periodieke detectie
async function startCamera() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true })
    video.value.srcObject = stream
    interval = setInterval(detectAndPredict, 1500)
  } catch {
    error.value = 'Camera access denied'
  }
}

// Initialiseer gezichtsdetectie bij laden van component
onMounted(async () => {
  await faceapi.nets.tinyFaceDetector.loadFromUri('/models/tiny_face_detector')
  await startCamera()
})

// Stop video en interval bij verlaten van component
onUnmounted(() => {
  clearInterval(interval)
  video.value?.srcObject?.getTracks().forEach(t => t.stop())
})
</script>

<style scoped>
/* Zorg dat canvas niet aanklikbaar is */
canvas {
  pointer-events: none;
}
</style>