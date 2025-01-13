import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """load JPG/JPEG image"""
    image = Image.open(path)
    image_array = np.array(image)
    print("The shape of image is:", image_array)
    print(image_array.shape)
    return image_array
