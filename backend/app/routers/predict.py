from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import io
import cv2

# Importeer padconfiguraties en hulpfuncties
from app.config import STROKE_MODEL_PATH, PAIN_MODEL_PATH, IMG_SIZE
from app.utils.face_utils import detect_face_landmarks, crop_half_face
from app.models.stroke_model import StrokeModel
from app.models.pain_model import PainModel

router = APIRouter()

# Laad de modellen één keer bij het starten van de applicatie
stroke_model = StrokeModel(STROKE_MODEL_PATH)
pain_model = PainModel(PAIN_MODEL_PATH)

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Lees het geüploade bestand als bytes
        image_bytes = await file.read()
        
        # Open de afbeelding en converteer naar RGB (voor consistentie)
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        
        # Zet om naar NumPy-array (nodig voor verdere verwerking)
        np_image = np.array(image)

        # Detecteer gezichtslandmarks (nodig voor het bepalen van de gezichtshelft)
        landmarks = detect_face_landmarks(np_image)
        if landmarks is None:
            raise HTTPException(status_code=400, detail="No face detected")

        # Normaliseer de afbeelding voor de stroke-predictie
        resized = cv2.resize(np_image, IMG_SIZE)
        norm_img = resized / 255.0

        # Voorspel aan welke kant de beroerte zich bevindt
        stroke_side = stroke_model.predict(norm_img)

        # Bepaal de gezonde kant op basis van voorspelling
        healthy_side = "left" if stroke_side == "right" else "right"

        # Crop de gezonde helft van het gezicht uit de afbeelding
        cropped_np = crop_half_face(np_image, landmarks, healthy_side)
        
        # Zet het gecropte beeld om naar PIL-formaat voor de pain predictor
        cropped_img = Image.fromarray(cropped_np)

        # Voorspel pijnscore op basis van gezonde gezichtshelft
        pain_score = pain_model.predict(cropped_img)

        # Geef de resultaten terug als JSON
        return JSONResponse({
            "stroke_side": stroke_side,
            "healthy_side": healthy_side,
            "pain_score": pain_score
        })

    except Exception as e:
        # Foutafhandeling voor onverwachte fouten
        raise HTTPException(status_code=500, detail=str(e))
