import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

mp_face_mesh = mp.solutions.face_mesh

def detect_face_landmarks(image: np.ndarray):
    with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        if not results.multi_face_landmarks:
            return None
        return results.multi_face_landmarks[0]

def crop_half_face(image: np.ndarray, landmarks, side: str) -> np.ndarray:
    height, width = image.shape[:2]

    # Get x-coordinates of key facial midline landmarks
    nose = landmarks.landmark[1]
    mid_x = int(nose.x * width)

    if side == "left":
        return image[:, :mid_x]
    elif side == "right":
        return image[:, mid_x:]
    else:
        raise ValueError("Side must be 'left' or 'right'")
