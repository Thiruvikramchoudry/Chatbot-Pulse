import tensorflow as tf
from keras.models import load_model
import cv2
import numpy as np

def spread_prediction(image):
    model = load_model("pulse/models/benign_malignent_model.h5")

    image_size = (150, 150)

    input_image_path = "pulse/static/user_images/"+str(image)
    input_image = cv2.imread(input_image_path)
    input_image = cv2.resize(input_image, image_size)
    input_image = np.expand_dims(input_image, axis=0)
    input_image = input_image / 255.0



    prediction = model.predict(input_image)
    predicted_class = np.argmax(prediction)


    if predicted_class==1:
        return "malignant"

    else:
        return "benign"
