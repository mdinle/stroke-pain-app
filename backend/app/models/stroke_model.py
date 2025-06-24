import tensorflow as tf
import numpy as np

class StrokeModel:
    def __init__(self, model_path: str):
        self.model = tf.keras.models.load_model(model_path)

    def predict(self, image_array: np.ndarray) -> str:
        input_tensor = tf.convert_to_tensor(image_array[np.newaxis, ...], dtype=tf.float32)
        pred = self.model.predict(input_tensor)[0][0]
        return "right" if pred >= 0.5 else "left"