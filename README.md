# smartbin_server
 This is a local host server developed using Fastapi for deployment of machine learning model outside of jupyter notebooks so you can see the action in real time !
# Trash Classification Web App

This project is a web application that uses a yolov8 model refer to this repo [https://github.com/ManikSinghSarmaal/yolov8_sbin] for model weights (this repo contains pre-trained VGG16 model which was discontinued by me) to classify images of trash into three categories: Inorganic, Organic, and Metal. The application is built using FastAPI for the backend and HTML/JavaScript for the frontend.

## Features

- Upload an image of trash through the web interface
- Get the predicted class (Inorganic, Organic, or Metal) for the uploaded image
- User-friendly interface with a file input and prediction display

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/trash-classification-app.git
```

2. Navigate to the project directory:
```
cd trash-classification-app
```
# Usage

1. Start the FastAPI server:
```uvicorn main:app --reload```
2. Open your web browser and navigate to http://localhost:8000.
3. Click the "Choose File" button and select an image of trash.
4. Click the "Predict Class" button to get the predicted class for the uploaded image.

# Customizations
You can customize the project by modifying the following files:

1. model.py: Update the model loading and preprocessing steps according to your requirements.
2. main.py: Modify the FastAPI routes or add new functionality as needed.
3. index.html: Customize the user interface by editing the HTML and JavaScript code.

# Live Server
![Your interface should look like this]([Images])
