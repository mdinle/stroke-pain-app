<!-- src/views/Docs.vue -->
<template>
  <div class="container mt-4">
    <h1 class="mb-4">Documentation</h1>

    <!-- Document List -->
    <ul class="list-group mb-4">
      <li
        class="list-group-item"
        v-for="doc in docs"
        :key="doc.name"
        :class="{ active: selectedDoc && selectedDoc.filename === doc.filename && selectedDoc.name === doc.name }"
        @click="selectDoc(doc)"
        style="cursor: pointer"
      >
        {{ doc.name }}
      </li>
    </ul>

    <!-- PDF Viewer -->
    <div v-if="selectedDoc">
      <h5 class="mb-2">Viewing: {{ selectedDoc.name }}</h5>
      <iframe
        :src="`/docs/${selectedDoc.filename}`"
        width="100%"
        height="600"
        style="border: 1px solid #ccc; border-radius: 8px;"
      ></iframe>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const docs = [
  { name: 'Dataset Description', filename: 'dataset_description.pdf' },
  { name: 'Models Overview', filename: 'model_overview.pdf' },
  { name: 'Technical Overview', filename: 'tec_overview.pdf' },
  { name: 'Pain detection code implementation', filename: 'pain_model_code_and_results.pdf' },
  { name: 'Stroke Detecting Model Training', filename: 'stroke_model_annotated.pdf' },
  { name: 'Stroke Models Comparison', filename: 'comparison.pdf' }
]

const selectedDoc = ref(null)

function selectDoc(doc) {
  selectedDoc.value = doc
}
</script>
