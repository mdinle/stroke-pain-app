<template>
  <div class="d-flex flex-wrap gap-4 align-items-start">
    <div class="position-relative border rounded shadow">
      <video ref="video" autoplay muted playsinline width="640" height="480" class="rounded"></video>
      <canvas ref="canvas" width="640" height="480" class="position-absolute top-0 start-0"></canvas>
    </div>

    <div v-if="result" class="bg-light p-3 rounded shadow" style="min-width: 260px">
      <h5>Live Prediction</h5>
      <p><strong>Stroke Side:</strong> {{ result.stroke_side }}</p>
      <p><strong>Healthy Side:</strong> {{ result.healthy_side }}</p>
      <p><strong>Pain Score:</strong> {{ result.pain_score.toFixed(2) }}</p>
    </div>

    <div v-if="error" class="alert alert-danger mt-3">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import * as faceapi from 'face-api.js'
import { predictStrokeAndPain } from '@/services/predictService'

const video = ref(null)
const canvas = ref(null)
const result = ref(null)
const error = ref(null)
let interval = null

async function detectAndPredict() {
  const options = new faceapi.TinyFaceDetectorOptions()
  const detection = await faceapi.detectSingleFace(video.value, options)
  const ctx = canvas.value.getContext('2d')
  ctx.clearRect(0, 0, canvas.value.width, canvas.value.height)

  if (detection) {
    const { x, y, width, height } = detection.box
    ctx.strokeStyle = 'lime'
    ctx.lineWidth = 2
    ctx.strokeRect(x, y, width, height)

    const faceCanvas = document.createElement('canvas')
    faceCanvas.width = width
    faceCanvas.height = height
    faceCanvas.getContext('2d').drawImage(video.value, x, y, width, height, 0, 0, width, height)

    const blob = await new Promise(resolve => faceCanvas.toBlob(resolve, 'image/jpeg'))

    try {
      result.value = await predictStrokeAndPain(blob)
      error.value = null
    } catch (err) {
      result.value = null
      error.value = err?.response?.data?.detail || 'Prediction failed'
    }
  } else {
    error.value = 'No face detected'
  }
}

async function startCamera() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true })
    video.value.srcObject = stream
    interval = setInterval(detectAndPredict, 1500)
  } catch {
    error.value = 'Camera access denied'
  }
}

onMounted(async () => {
  await faceapi.nets.tinyFaceDetector.loadFromUri('/models/tiny_face_detector')
  await startCamera()
})

onUnmounted(() => {
  clearInterval(interval)
  video.value?.srcObject?.getTracks().forEach(t => t.stop())
})
</script>

<style scoped>
canvas {
  pointer-events: none;
}
</style>
