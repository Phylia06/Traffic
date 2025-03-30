import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image, ImageTk

# Constants
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43  # Ensure this matches your dataset

# Load the trained model
model = tf.keras.models.load_model("best_model8.h5")

# Define category labels (Replace this with your dataset labels)
CATEGORY_LABELS = {
    9: "no overtaking",
    22: "uneven",
    23: "slippery road",
    17: "no entry",
    24: "narrow road right",
    25: "road work",
    28: "children",
    29: "no cycling",
    31: "Deer Crossing",
    40: "Roundabout"
    # Add all categories up to NUM_CATEGORIES
}

def preprocess_image(image_path):
    """Load and preprocess the image for prediction."""
    img = cv2.imread(image_path)
    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
    img = img / 255.0  # Normalize pixel values
    return np.expand_dims(img, axis=0)

def predict_sign(image_path):
    """Predict the traffic sign from the image."""
    img = preprocess_image(image_path)
    predictions = model.predict(img)
    predicted_index = np.argmax(predictions)
    confidence = np.max(predictions)
    sign_name = CATEGORY_LABELS.get(predicted_index, "Unknown")
    return predicted_index, sign_name, confidence

def upload_and_predict():
    """Handle image upload and prediction display."""
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        predicted_index, sign_name, confidence = predict_sign(file_path)
        result_label.config(text=f"Predicted: {sign_name} ({predicted_index}), Confidence: {confidence:.3f}")
        
        # Display the image
        img = Image.open(file_path)
        img = img.resize((150, 150))
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img

# Create Tkinter GUI
root = tk.Tk()
root.title("Traffic Sign Predictor")

tk.Button(root, text="Upload Image", command=upload_and_predict).pack(pady=10)

img_label = tk.Label(root)
img_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()