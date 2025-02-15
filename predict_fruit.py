from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
import cv2
import ast
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    """
    TODO: Implement a fruit classification endpoint that:
    1. Accepts an image file
    2. Preprocesses the image
    3. Makes a prediction using the model
    4. Returns the predicted fruit with confidence score
    """
    
    # TODO: Check if image is provided in the request
    # Return error if no image is found
    
    # TODO: Read and decode the image
    # Hint: Use request.files, cv2.imdecode
    
    # TODO: Preprocess the image
    # 1. Resize to 100x100
    # 2. Convert BGR to RGB
    # 3. Normalize pixel values to [0,1]
    
    # TODO: Load the model
    # Hint: Use try-except for error handling
    
    # TODO: Make prediction
    # Hint: Use model.predict() and handle exceptions
    
    # TODO: Get top 5 predictions
    # Hint: Use np.argsort()
    
    # TODO: Load fruits dictionary from 'Backend/directories.txt'
    # Hint: Use ast.literal_eval()
    
    # TODO: Return prediction
    # Format: {
    #   'fruit': fruit_name,
    #   'confidence': confidence_score,
    #   'class_id': class_id
    # }
    
    pass  # Remove this line when implementing the function

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)


