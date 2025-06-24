import torch
import torchvision.transforms as transforms
from PIL import Image
from app.config import IMG_SIZE, NORMALIZATION_MEAN, NORMALIZATION_STD, DEVICE

class PainModel:
    def __init__(self, model_path: str):
        from torchvision import models
        self.device = DEVICE
        self.model = models.resnet18(weights=None)
        self.model.fc = torch.nn.Linear(self.model.fc.in_features, 1)
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Resize(IMG_SIZE),
            transforms.ToTensor(),
            transforms.Normalize(mean=NORMALIZATION_MEAN, std=NORMALIZATION_STD)
        ])

    def predict(self, img: Image.Image) -> float:
        with torch.no_grad():
            tensor = self.transform(img).unsqueeze(0).to(self.device)
            score = self.model(tensor).item()
        return round(score, 2)