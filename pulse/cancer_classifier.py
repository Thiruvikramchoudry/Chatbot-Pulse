import tensorflow as tf
import cv2

def check_cancer(image):

    model = tf.keras.models.load_model('pulse/models/Cancer_identification_model.h5')
    # ISIC_0024306.jpg-melanocytic nevi
    img = cv2.imread("pulse/static/user_images/"+str(image))
    img = cv2.resize(img, (28, 28))

    result = model.predict(img.reshape(1, 28, 28, 3))
    max_prob = max(result[0])
    class_ind = list(result[0]).index(max_prob)

    # 0029301

    classes = {4: ' melanocytic nevi', 6: 'melanoma', 2: 'benign keratosis-like lesions', 1: ' basal cell carcinoma',
               5: ' pyogenic granulomas and hemorrhage', 0: 'Actinic keratoses and intraepithelial carcinomae',
               3: 'dermatofibroma'}

    return classes[class_ind]