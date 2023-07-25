from keras.models import load_model
import tensorflow as tf
import numpy as np



def predict_disease(image):
    model = load_model('pulse/models/skin_disease_model.h5')
    img = tf.keras.utils.load_img("pulse/static/user_images/"+str(image),target_size=(256, 256))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    class_names =['Acne and Rosacea Photos','Bullous Disease Photos','Eczema Photos','Poison Ivy Photos and other Contact Dermatitis','Normal skin','Psoriasis pictures Lichen Planus and related diseases','Urticaria Hives']

    return class_names[np.argmax(score)]

