import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import os
import django
import pickle

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_website.settings")  # replace with your settings
django.setup()

from core.models import Item  # adjust if your app name is different

# Load pretrained ResNet50 and remove final classification layer
model = models.resnet50(pretrained=True)
model = torch.nn.Sequential(*(list(model.children())[:-1]))  # remove last layer
model.eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

def get_embedding(img_path):
    img = Image.open(img_path).convert("RGB")
    img = transform(img).unsqueeze(0)
    with torch.no_grad():
        vec = model(img).squeeze().numpy()
    return vec / np.linalg.norm(vec)  # normalize

# Generate embeddings for all items
for item in Item.objects.all():
    if item.image:
        embedding = get_embedding(item.image.path)
        item.set_embedding(embedding)
        item.save()
        print(f"Saved embedding for: {item.title}")
