<template>
  <div class="container mt-4">
    <h2 class="mb-2">Stroke & Pain Prediction</h2>
    <div class="btn-group mb-3">
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

    <UploadForm v-if="mode === 'upload'" />
    <LiveCamera v-else />

      <div class="mt-4 text-muted small d-flex gap-5 text-center justify-content-center">
  <p>ℹ️ <strong>Stroke Model Output</strong><br>
  Output is between 0 and 1.<br>
  Closer to <strong>0</strong>: left side is affected<br>
  Closer to <strong>1</strong>: right side is affected</p>

  <p>ℹ️ <strong>PSPI Score Scale</strong><br>
  Pain score ranges from <strong>0 to 11</strong>.<br>
  Closer to <strong>0</strong>: low pain or no pain<br>
  Closer to <strong>10+</strong>: significant pain detected</p>
</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import UploadForm from '@/components/UploadForm.vue'
import LiveCamera from '@/components/LiveCamera.vue'


const mode = ref('upload')
</script>