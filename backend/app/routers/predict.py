from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import io
import cv2

from app.config import STROKE_MODEL_PATH, PAIN_MODEL_PATH, IMG_SIZE
from app.utils.face_utils import detect_face_landmarks, crop_half_face
from app.models.stroke_model import StrokeModel
from app.models.pain_model import PainModel

router = APIRouter()

# Load models once
stroke_model = StrokeModel(STROKE_MODEL_PATH)
pain_model = PainModel(PAIN_MODEL_PATH)

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        np_image = np.array(image)

        landmarks = detect_face_landmarks(np_image)
        if landmarks is None:
            raise HTTPException(status_code=400, detail="No face detected")

        resized = cv2.resize(np_image, IMG_SIZE)
        norm_img = resized / 255.0
        stroke_side = stroke_model.predict(norm_img)

        healthy_side = "left" if stroke_side == "right" else "right"
        cropped_np = crop_half_face(np_image, landmarks, healthy_side)
        cropped_img = Image.fromarray(cropped_np)

        pain_score = pain_model.predict(cropped_img)

        return JSONResponse({
            "stroke_side": stroke_side,
            "healthy_side": healthy_side,
            "pain_score": pain_score
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
