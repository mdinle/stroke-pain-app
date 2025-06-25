<template>
  <div class="container mx-auto p-6 max-w-5xl">
    <h1 class="text-3xl font-bold mb-6">Project Setup & Installation Guide</h1>

    <!-- Installation -->
    <section class="mb-10">
      <h2 class="text-xl font-semibold mb-2">Installation</h2>
      <p>This guide helps you set up the full project (frontend and backend) locally. Make sure you have Python 3.8+ and Node.js 16+ installed.</p>
      <pre class="bg-gray-100 p-4 rounded text-sm overflow-auto">
# Clone the repository
git clone https://github.com/your-org/your-project.git
cd your-project
      </pre>
    </section>

    <!-- Backend Setup -->
    <section class="mb-10">
      <h2 class="text-xl font-semibold mb-2">Backend Setup (FastAPI)</h2>
      <pre class="bg-gray-100 p-4 rounded text-sm overflow-auto">
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install backend dependencies
pip install -r backend/requirements.txt

# Run the FastAPI server
uvicorn backend.app:app --reload

# API available at: http://localhost:8000/docs
      </pre>
    </section>

    <!-- Frontend Setup -->
    <section class="mb-10">
      <h2 class="text-xl font-semibold mb-2">Frontend Setup (Vue 3)</h2>
      <pre class="bg-gray-100 p-4 rounded text-sm overflow-auto">
# Navigate to the frontend folder
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev

# App available at: http://localhost:5173
      </pre>
    </section>

    <!-- Pretrained Model -->
    <section class="mb-10">
      <h2 class="text-xl font-semibold mb-2">Download Pretrained Model</h2>
      <p>Ensure the trained PyTorch model file is placed in the correct directory.</p>
      <a
        href="/models/best_model.pt"
        class="inline-block bg-blue-600 text-white px-4 py-2 mt-2 rounded hover:bg-blue-700"
        download
      >
        Download best_model.pt
      </a>
      <p class="mt-2 text-sm text-gray-600">Place this file in the <code>/models</code> folder inside the backend directory.</p>
    </section>

    <!-- GitHub Link -->
    <section class="mb-10">
      <h2 class="text-xl font-semibold mb-2">GitHub Repository</h2>
      <p>The full project source code is available here:</p>
      <a href="https://github.com/your-org/your-project" class="text-blue-600 underline">
        github.com/your-org/your-project
      </a>
    </section>

    <!-- Final Notes -->
    <section class="mb-10">
      <h2 class="text-xl font-semibold mb-2">Running the Full System</h2>
      <ul class="list-disc ml-6">
        <li>Ensure the backend is running before using the prediction page.</li>
        <li>Frontend will call the backend API automatically for inference.</li>
        <li>Use <code>/docs</code> endpoint in backend to test API routes (via Swagger).</li>
      </ul>
    </section>
  </div>
</template>

<script setup>
// No script logic needed
</script>

<style scoped>
h1, h2 {
  color: #1e293b;
}
</style>
