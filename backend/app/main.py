from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import io

from app.config import STROKE_MODEL_PATH, PAIN_MODEL_PATH, IMG_SIZE
from app.utils.face_utils import detect_face_landmarks, crop_half_face
from app.models.stroke_model import StrokeModel
from app.models.pain_model import PainModel

import cv2

# Load models
stroke_model = StrokeModel(STROKE_MODEL_PATH)
pain_model = PainModel(PAIN_MODEL_PATH)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Stroke and Pain Prediction API."}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Load image
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        np_image = np.array(image)

        # Get face landmarks
        landmarks = detect_face_landmarks(np_image)
        if landmarks is None:
            raise HTTPException(status_code=400, detail="No face detected")

        # Stroke side prediction
        resized = cv2.resize(np_image, IMG_SIZE)
        norm_img = resized / 255.0
        stroke_side = stroke_model.predict(norm_img)

        # Crop healthy side
        healthy_side = "left" if stroke_side == "right" else "right"
        cropped_np = crop_half_face(np_image, landmarks, healthy_side)
        cropped_img = Image.fromarray(cropped_np)

        # Pain prediction
        pain_score = pain_model.predict(cropped_img)

        return JSONResponse({
            "stroke_side": stroke_side,
            "healthy_side": healthy_side,
            "pain_score": pain_score
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))