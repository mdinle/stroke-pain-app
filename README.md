# StrokePain App

A two-part application for predicting stroke-affected side and pain levels using facial images.

## Project Structure

- `/backend`: FastAPI server with image processing and prediction logic
- `/frontend`: Vue 3 SPA with Bootstrap and Axios

## How to Run Locally

### Backend
```bash
cd backend
docker build -t stroke-pain-backend .
docker run -p 8000:8000 stroke-pain-backend
