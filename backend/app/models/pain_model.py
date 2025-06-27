import torch
import torchvision.transforms as transforms
from PIL import Image
from app.config import IMG_SIZE, NORMALIZATION_MEAN, NORMALIZATION_STD, DEVICE

class PainModel:
    def __init__(self, model_path: str):
        from torchvision import models

        # Sla het apparaat op waarop het model zal draaien (bijv. 'cpu' of 'cuda')
        self.device = DEVICE

        # Laad een ResNet18-model zonder vooraf getrainde gewichten
        self.model = models.resnet18(weights=None)

        # Vervang de laatste volledig verbonden laag om 1 enkele waarde (pain score) te voorspellen
        self.model.fc = torch.nn.Linear(self.model.fc.in_features, 1)

        # Laad het getrainde modelgewicht vanaf bestand
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))

        # Zet het model in evaluatiemodus
        self.model.eval()

        # Definieer de preprocessing-transformaties voor invoerafbeeldingen
        self.transform = transforms.Compose([
            transforms.Resize(IMG_SIZE),  # Schaal afbeelding naar juiste grootte
            transforms.ToTensor(),        # Zet afbeelding om naar PyTorch-tensor
            transforms.Normalize(mean=NORMALIZATION_MEAN, std=NORMALIZATION_STD)  # Normaliseer pixelwaarden
        ])

    def predict(self, img: Image.Image) -> float:
        with torch.no_grad():
            # Pas transformaties toe en voeg batch-dimensie toe
            tensor = self.transform(img).unsqueeze(0).to(self.device)

            # Voer voorspelling uit met het model
            score = self.model(tensor).item()

        # Rond de pijnscore af op twee decimalen
        return round(score, 2)
