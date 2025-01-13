import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    """display image after zooming, performing grayscale conversion and transposing it"""
    image_array = ft_load("../animal.jpeg")
    image_array_cropped = image_array[100:500, 400:800]
    grayscale = image_array_cropped.mean(axis=2)
    print("The shape of image is:", grayscale.shape)
    print(grayscale)

    grayscale_transposed = np.empty([grayscale.shape[1], grayscale.shape[0]], dtype = int)
    for i in range(grayscale.shape[0]):
        for j in range(grayscale.shape[1]):
            grayscale_transposed[i][j]= grayscale[j][i]
    plt.imshow(grayscale_transposed, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
