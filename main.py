from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from model import load_model, preprocess_image
import torch
import cv2
from fastapi.templating import Jinja2Templates

# Create Jinja2 templates instance
templates = Jinja2Templates(directory="templates") # Update templates directory

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this based on your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = load_model() # Load model at startup
device = "cuda" if torch.cuda.is_available() else "cpu" # Set device

@app.get("/")
async def form(request: Request):
    return templates.TemplateResponse("futuristic.html", {"request": request}) # Render the form

@app.post("/predict")
async def predict_class(image: UploadFile = File(...)):
    content = await image.read()
    try:
        img_tensor = preprocess_image(content)
        model.eval()
        with torch.no_grad():
            outputs = model(img_tensor)
            predicted_class = torch.argmax(outputs, dim=1).item()
            class_labels = ['Inorganic', 'Organic', 'Metal']
            predicted_label = class_labels[predicted_class]
            return {"predicted_class": predicted_label}
    except Exception as e:
        return {"error": f"Failed to process image: {e}"}