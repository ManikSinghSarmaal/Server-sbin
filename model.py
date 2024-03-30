import torch
from torchvision import transforms, models
import numpy as np
import io
import cv2
from PIL import Image
device ='cpu'
def load_model():
    model = models.vgg16(pretrained=False)
    model.load_state_dict(torch.load('/Users/maniksinghsarmaal/Downloads/s_bin/Sbin_f/saved_models/vgg16.pth'))
    return model

def preprocess_image(content):
    img = Image.open(io.BytesIO(content))  # Use BytesIO to load image from bytes
    
    # Apply transformations (same as before)
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    img_tensor = transform(img).unsqueeze(0)
    return img_tensor.to(device)
