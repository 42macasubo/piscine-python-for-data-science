import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """print shape and RGB content of JPG/JPEG image"""
    image = Image.open(path)
    image_array = np.array(image)
    print("The shape of image is:", image_array.shape)
    return image_array
