<template>
  <div class="container mt-4">
    <h2 class="mb-2">Stroke & Pain Prediction</h2>

  <!-- Description Section -->
<div class="mb-4 text-muted small">
  <p>ℹ️ <strong>Stroke Model Output</strong><br>
  Output is between 0 and 1.<br>
  Closer to <strong>0</strong>: left side is affected<br>
  Closer to <strong>1</strong>: right side is affected</p>

  <p>ℹ️ <strong>PSPI Score Scale</strong><br>
  Pain score ranges from <strong>0 to 11</strong>.<br>
  Closer to <strong>0</strong>: low pain or no pain<br>
  Closer to <strong>10+</strong>: significant pain detected</p>
</div>


    <!-- Toggle between Upload or Live Camera -->
    <div class="btn-group mb-3" role="group">
      <button
        class="btn"
        :class="mode === 'upload' ? 'btn-primary' : 'btn-outline-primary'"
        @click="mode = 'upload'"
      >Upload Image</button>
      <button
        class="btn"
        :class="mode === 'camera' ? 'btn-primary' : 'btn-outline-primary'"
        @click="mode = 'camera'"
      >Live Camera</button>
    </div>

    <!-- Upload Image Mode -->
    <div v-if="mode === 'upload'" class="card p-4 shadow-sm">
      <h5 class="mb-3">Upload a face image</h5>
      <input type="file" class="form-control mb-3" @change="handleFile" accept="image/jpeg,image/png" />
      <button class="btn btn-success" @click="submitImage" :disabled="!image">Submit</button>
    </div>

    <!-- Live Camera Mode -->
    <div v-if="mode === 'camera'" class="d-flex flex-wrap gap-4 align-items-start">
      <!-- Camera -->
      <div class="position-relative border rounded shadow">
        <video ref="video" autoplay muted playsinline width="640" height="480" class="rounded"></video>
        <canvas ref="canvas" width="640" height="480" class="position-absolute top-0 start-0"></canvas>
      </div>

      <!-- Results Next to Camera -->
      <div v-if="result" class="bg-light p-3 rounded shadow" style="min-width: 260px">
        <h5>Live Prediction</h5>
        <p><strong>Stroke Side:</strong> {{ result.stroke_side }}</p>
        <p><strong>Healthy Side:</strong> {{ result.healthy_side }}</p>
        <p><strong>Pain Score:</strong> {{ result.pain_score.toFixed(2) }}</p>
      </div>
    </div>

    <!-- Upload Result -->
    <div v-if="mode === 'upload' && result" class="mt-4 p-3 bg-light rounded shadow">
      <p><strong>Stroke Side:</strong> {{ result.stroke_side }}</p>
      <p><strong>Healthy Side:</strong> {{ result.healthy_side }}</p>
      <p><strong>Pain Score:</strong> {{ result.pain_score.toFixed(2) }}</p>
    </div>

    <!-- Error Message -->
    <div v-if="error" class="alert alert-danger mt-3">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import * as faceapi from 'face-api.js'
import { predictStrokeAndPain } from '@/api/predictApi'

const image = ref(null)
const result = ref(null)
const error = ref(null)
const mode = ref('upload')

const video = ref(null)
const canvas = ref(null)
let interval = null

function handleFile(event) {
  image.value = event.target.files[0]
  result.value = null
  error.value = null
}

async function submitImage() {
  try {
    const res = await predictStrokeAndPain(image.value)
    result.value = res
    error.value = null
  } catch (err) {
    result.value = null
    error.value = err?.response?.data?.detail || err.message
  }
}

async function startCamera() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true })
    video.value.srcObject = stream
  } catch {
    error.value = 'Camera access denied or not available'
  }
}

async function detectAndPredict() {
  const options = new faceapi.TinyFaceDetectorOptions()
  const detection = await faceapi.detectSingleFace(video.value, options)

  const ctx = canvas.value.getContext('2d')
  ctx.clearRect(0, 0, canvas.value.width, canvas.value.height)

  if (detection) {
    const box = detection.box
    ctx.strokeStyle = 'lime'
    ctx.lineWidth = 2
    ctx.strokeRect(box.x, box.y, box.width, box.height)

    const faceCanvas = document.createElement('canvas')
    faceCanvas.width = box.width
    faceCanvas.height = box.height
    faceCanvas.getContext('2d').drawImage(
      video.value,
      box.x,
      box.y,
      box.width,
      box.height,
      0,
      0,
      box.width,
      box.height
    )

    const blob = await new Promise(resolve => faceCanvas.toBlob(resolve, 'image/jpeg'))

    try {
      result.value = await predictStrokeAndPain(blob)
      error.value = null
    } catch (err) {
      result.value = null
      error.value = err?.response?.data?.detail || 'Prediction failed'
    }
  } else {
    result.value = null
    error.value = 'No face detected'
  }
}

watch(mode, async (newMode) => {
  result.value = null
  error.value = null

  if (newMode === 'camera') {
    await faceapi.nets.tinyFaceDetector.loadFromUri('/models/tiny_face_detector')
    await startCamera()
    interval = setInterval(detectAndPredict, 1500)
  } else {
    clearInterval(interval)
    if (video.value?.srcObject) {
      video.value.srcObject.getTracks().forEach(t => t.stop())
    }
  }
})

onUnmounted(() => {
  clearInterval(interval)
  video.value?.srcObject?.getTracks().forEach(t => t.stop())
})
</script>

<style scoped>
canvas {
  position: absolute;
  top: 0;
  left: 0;
  pointer-events: none;
}
</style>
