import tensorflow as tf
import numpy as np

class StrokeModel:
    def __init__(self, model_path: str):
        # Laad het Keras-model vanaf het opgegeven pad
        self.model = tf.keras.models.load_model(model_path)

    def predict(self, image_array: np.ndarray) -> str:
        # Voeg batch-dimensie toe aan de afbeelding en converteer naar tensor
        input_tensor = tf.convert_to_tensor(image_array[np.newaxis, ...], dtype=tf.float32)

        # Maak een voorspelling met het geladen model
        pred = self.model.predict(input_tensor)[0][0]

        # Retourneer de voorspelde zijde van de beroerte op basis van drempelwaarde 0.5
        return "right" if pred >= 0.5 else "left"
