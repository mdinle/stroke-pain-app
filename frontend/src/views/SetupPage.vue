<template>
  <div class="container mt-5">
    <!-- Deployed App Info -->
    <section class="mb-5 text-center">
      <h1 class="fw-bold mb-3">Stroke Pain Prediction App</h1>
      <p class="lead">
        🔗 The application is live at:
        <a
          href="https://strokepain-frontend-app.azurewebsites.net/"
          target="_blank"
          rel="noopener"
          class="fw-semibold"
        >
          strokepain-frontend-app.azurewebsites.net
        </a>
      </p>
    </section>

    <!-- Intro -->
    <section class="mb-4">
      <h2 class="h5 mb-2">Local Deployment Guide</h2>
      <p>
        This guide helps you set up the project locally for development and testing.
        Use the credentials below to log in:
      </p>
      <ul class="list-unstyled ms-3">
        <li>• <strong>Username:</strong> admin</li>
        <li>• <strong>Password:</strong> admin</li>
      </ul>
    </section>

    <!-- Installation -->
    <section class="mb-5">
      <h2 class="h5 mb-2">1. Installation</h2>
      <p>Ensure you have Python 3.8+ and Node.js 16+ installed. Then clone the repository:</p>
      <pre class="bg-light p-3 rounded"><code>
# Clone the repository
git clone https://github.com/mdinle/stroke-pain-app.git
cd stroke-pain-app
      </code></pre>
    </section>

    <!-- Backend Setup -->
    <section class="mb-5">
      <h2 class="h5 mb-2">2. Backend Setup (FastAPI)</h2>
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
      <h2 class="h5 mb-2">3. Frontend Setup (Vue 3)</h2>
      <pre class="bg-light p-3 rounded"><code>
cd frontend
npm install
npm run dev

# Visit: http://localhost:5173
      </code></pre>
    </section>

    <!-- Pretrained Model -->
    <section class="mb-5">
      <h2 class="h5 mb-2">4. Download Pretrained Model</h2>
      <p>Place the downloaded model file in the <code>/models</code> folder under the backend directory:</p>
      <a
        href="/models/best_model.pt"
        class="btn btn-primary mt-2"
        download
      >Download best_model.pt</a>
    </section>

    <!-- GitHub Repository -->
    <section class="mb-5">
      <h2 class="h5 mb-2">5. GitHub Repository</h2>
      <p>View the complete source code on GitHub:</p>
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
      <h2 class="h5 mb-2">6. Final Notes</h2>
      <ul class="list-unstyled ms-3">
        <li>• Start the backend before launching the frontend.</li>
        <li>• The frontend will connect to the backend automatically.</li>
        <li>• Use <code>/docs</code> (e.g., http://localhost:8000/docs) to test API endpoints.</li>
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
