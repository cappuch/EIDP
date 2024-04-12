import base64
import json
from PIL import Image
import numpy as np
import torch
from torchvision import transforms
from io import BytesIO
from model import Model

def load_image_from_bytes(image_bytes):
    image = Image.open(BytesIO(image_bytes))
    image = image.convert('RGB')
    return image

def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)

def infer_single_image(image_bytes, model):
    image = load_image_from_bytes(image_bytes)
    preprocessed_image = preprocess_image(image)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    model.eval()

    with torch.no_grad():
        outputs = model(preprocessed_image.to(device))
        rotation_pred, l2_pred, r2_pred = outputs[:, 0], outputs[:, 1], outputs[:, 2]

    return rotation_pred.item(), l2_pred.item(), r2_pred.item()

def inference(inputfile, model_dir='pytorch_model.pth'):
    model = Model(num_classes=3)
    model.load_state_dict(torch.load(model_dir))

    with open(inputfile, "rb") as f:
        image_bytes = f.read()

    rotation, l2, r2 = infer_single_image(image_bytes, model)

    return {
        "rot": rotation,
        "l2": l2,
        "r2": r2
    }
