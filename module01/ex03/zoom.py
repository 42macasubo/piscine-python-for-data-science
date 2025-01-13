import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    """display image after zooming and performing grayscale conversion"""
    image_array = ft_load("../animal.jpeg")
    print(image_array)
    image_array_cropped = image_array[100:500, 400:800]
    grayscale = image_array_cropped.mean(axis=2)
    print("New shape after slicing:", grayscale.shape)
    print(grayscale)
    plt.imshow(grayscale, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
