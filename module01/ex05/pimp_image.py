import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def ft_invert(array: np.array) -> np.array:
    """Inverts the color of the image received."""
    return np.array([[[255 - r, 255 - g, 255 - b] for r,g,b in array[r]] for r in range(array.shape[0])])


def ft_red(array: np.array) -> np.array:
    """keep only red channel of the image received."""
    return np.array([[[r, 0, 0] for r,g,b in array[r]] for r in range(array.shape[0])])


def ft_green(array: np.array) -> np.array:
    """keep only green channel of the image received."""
    return np.array([[[0, g, 0] for r,g,b in array[r]] for r in range(array.shape[0])])


def ft_blue(array: np.array) -> np.array:
    """keep only blue channel of the image received."""
    return np.array([[[0, 0, b] for r,g,b in array[r]] for r in range(array.shape[0])])


def ft_grey(array: np.array) -> np.array:
    """perform grayscale on the image received."""
    return np.array([[int((int(r) + int(g) + int(b)) / 3) for r,g,b in array[r]] for r in range(array.shape[0])])


def main():
    image_array = ft_load("../landscape.jpg")

    print(ft_grey(image_array))
    plt.imshow(ft_grey(image_array), cmap='gray')
    plt.show()

    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
