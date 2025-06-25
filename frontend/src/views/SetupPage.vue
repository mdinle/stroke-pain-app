<template>
  <div class="container mt-5">
    <h1 class="mb-4 fw-bold">Project Setup & Installation Guide</h1>

    <!-- Installation -->
    <section class="mb-5">
      <h2 class="h5 mb-2">Installation</h2>
      <p>Install Python 3.8+ and Node.js 16+, then clone the repo:</p>
      <pre class="bg-light p-3 rounded"><code>
# Clone the repository
git clone https://github.com/your-org/your-project.git
cd your-project
      </code></pre>
    </section>

    <!-- Backend Setup -->
    <section class="mb-5">
      <h2 class="h5 mb-2">Backend Setup (FastAPI)</h2>
      <pre class="bg-light p-3 rounded"><code>
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt

# Run the FastAPI server
uvicorn backend.app:app --reload

# Visit: http://localhost:8000/docs
      </code></pre>
    </section>

    <!-- Frontend Setup -->
    <section class="mb-5">
      <h2 class="h5 mb-2">Frontend Setup (Vue 3)</h2>
      <pre class="bg-light p-3 rounded"><code>
cd frontend
npm install
npm run dev

# Visit: http://localhost:5173
      </code></pre>
    </section>

    <!-- Pretrained Model -->
    <section class="mb-5">
      <h2 class="h5 mb-2">Download Pretrained Model</h2>
      <p>Place the file below in the <code>/models</code> folder inside the backend:</p>
      <a
        href="/models/best_model.pt"
        class="btn btn-primary mt-2"
        download
      >Download best_model.pt</a>
    </section>

    <!-- GitHub Repository -->
    <section class="mb-5">
      <h2 class="h5 mb-2">GitHub Repository</h2>
      <p>You can view the full source code here:</p>
      <a
        href="https://github.com/mdinle/stroke-pain-app.git"
        class="btn btn-outline-dark mt-2"
        target="_blank"
        rel="noopener"
      >
        View on GitHub
      </a>
    </section>

    <!-- Final Notes -->
    <section class="mb-5">
      <h2 class="h5 mb-2">Final Notes</h2>
      <ul class="list-unstyled ms-3">
        <li>• Start the backend first before opening the frontend.</li>
        <li>• Frontend connects automatically to the backend.</li>
        <li>• Use <code>/docs</code> in the backend to test API endpoints.</li>
      </ul>
    </section>
  </div>
</template>

<script setup>
// No logic needed
</script>

<style scoped>
code {
  font-family: monospace;
  font-size: 0.9rem;
}
</style>
