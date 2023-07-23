from PIL import Image
import numpy as np

import joblib

def resize_image(image_path, target_size=(28, 28)):
    # Open the image using Pillow
    img = Image.open(image_path).convert('RGB')

    # Resize the image to the target size (28x28 pixels)
    img_resized = img.resize(target_size, Image.ANTIALIAS)

    return img_resized

def image_to_rgb_grid(image_path, target_size=(28, 28)):
    # Resize the image
    img_resized = resize_image(image_path, target_size)

    # Convert the image to a NumPy array
    img_array = np.array(img_resized)

    # Normalize the pixel values to the range [0, 1]
    img_array = img_array

    return img_array

# Replace 'path/to/your/image.jpg' with the actual path to your image file


# Load the model




def validate_image(image):
    model = joblib.load('pulse/models/Skin_NonSkin_model.pkl')
    # Convert the image to a 28x28 grid of RGB values
    # Print the shape of the RGB grid (should be (28, 28, 3) for RGB images)
    rgb_grid = image_to_rgb_grid(image)
    skin_count = 0
    non_skin_count = 0
    for x in rgb_grid:

        predictions = model.predict(x)
        for i, prediction in enumerate(predictions):
            if prediction == 1:
                skin_count += 1
            else:
                non_skin_count += 1
    percentage=100*skin_count/(skin_count+non_skin_count)
    return percentage

