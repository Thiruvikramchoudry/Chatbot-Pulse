import tensorflow as tf
import cv2

def check_cancer(image):

    model = tf.keras.models.load_model('pulse/models/Cancer_identification_model.h5')

    img = cv2.imread("pulse/static/user_images/"+str(image))
    img = cv2.resize(img, (28, 28))

    result = model.predict(img.reshape(1, 28, 28, 3))
    max_prob = max(result[0])
    class_ind = list(result[0]).index(max_prob)


    classes = {4: 'Melanocytic nevi', 6: 'Melanoma', 2: 'Keratosis-like lesions', 1: 'Basal cell carcinoma',
               5: "Bowen's disease", 0: 'Actinic keratoses',3: 'Dermatofibroma'}

    return classes[class_ind]

#Actinic keratoses