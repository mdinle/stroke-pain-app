# StrokePain App

A two-part application for predicting stroke-affected side and pain levels using facial images.

## Project Structure

- `/backend`: FastAPI server with image processing and prediction logic
- `/frontend`: Vue 3 SPA with Bootstrap and Axios

## How to Run Locally

### Backend

## Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop) installed  
- Model files downloaded (see below)

```bash
cd backend
docker build -t stroke-pain-backend .
docker run -p 8000:8000 stroke-pain-backend
```
### Frontend

## Prerequisites
- [Node.js & npm](https://nodejs.org/) installed

```bash
cd frontend
npm install
npm run dev
```

## Download Trained Models

The trained model files are not included in the Git repository due to size limits.

You can download them here:
- [Download cnn_stroke_model.keras](https://github.com/mdinle/stroke-pain-app/releases/latest)
- [Download pain_model.pth](https://github.com/mdinle/stroke-pain-app/releases/latest)

Place them in:

stroke-pain-app/
├── backend/
│ └── models/
│ ├── cnn_stroke_model.keras
│ └── pain_model.pth
