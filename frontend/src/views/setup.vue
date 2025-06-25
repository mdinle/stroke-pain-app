<template>
  <div class="container mx-auto p-6 max-w-5xl">
    <h1 class="text-3xl font-bold mb-6">🛠 Project Setup & Instructions</h1>

    <!-- Section: Install Instructions -->
    <section class="mb-10">
      <h2 class="text-xl font-semibold mb-2">🔧 Installation</h2>
      <pre class="bg-gray-100 p-4 rounded text-sm overflow-auto">
# Clone the repo
git clone https://github.com/your-org/your-project.git
cd your-project

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
      </pre>
    </section>

    <!-- Section: GitHub Code -->
    <section class="mb-10">
      <h2 class="text-xl font-semibold mb-2">📂 Source Code</h2>
      <p>All code is available on <a href="https://github.com/your-org/your-project" class="text-blue-600 underline">GitHub</a>.</p>
    </section>

    <!-- Section: Model Download -->
    <section class="mb-10">
      <h2 class="text-xl font-semibold mb-2">🧠 Download Trained Models</h2>
      <p>Click below to download the pretrained model:</p>
      <a
        href="/models/best_model.pt"
        class="inline-block bg-blue-600 text-white px-4 py-2 mt-2 rounded hover:bg-blue-700"
        download
      >Download best_model.pt</a>
    </section>

    <!-- Section: Backend Instructions -->
    <section class="mb-10">
      <h2 class="text-xl font-semibold mb-2">💻 Backend Setup</h2>
      <pre class="bg-gray-100 p-4 rounded text-sm overflow-auto">
# Backend (Flask or FastAPI example)

# Run server
python backend/app.py

# API will run at http://localhost:5000
      </pre>
    </section>

    <!-- Section: Frontend Instructions -->
    <section class="mb-10">
      <h2 class="text-xl font-semibold mb-2">🖼 Frontend Setup</h2>
      <pre class="bg-gray-100 p-4 rounded text-sm overflow-auto">
# Frontend (Vue 3)

cd frontend
npm install
npm run dev

# Site will run at http://localhost:5173
      </pre>
    </section>

    <!-- Section: Final Tips -->
    <section class="mb-10">
      <h2 class="text-xl font-semibold mb-2">✅ Run the Full Project</h2>
      <ul class="list-disc ml-6">
        <li>Backend must be running before uploading any images</li>
        <li>Frontend will automatically call prediction API</li>
        <li>Ensure <code>best_model.pt</code> is in the <code>/models</code> folder</li>
      </ul>
    </section>
  </div>
</template>

<script setup>
// nothing needed unless dynamic model link
</script>

<style scoped>
h1, h2 {
  color: #1e293b;
}
</style>
