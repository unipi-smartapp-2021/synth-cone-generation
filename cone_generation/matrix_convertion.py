from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from random import choices


def convert_image_to_matrix(filepath: str):
    """
    Convert an image to grayscale and then to a numpy matrix.

    :param filepath: filepath of image
    :return: the matrix
    """
    with Image.open(filepath) as image:
        # Convert the image to GrayScale, so we convert a tensor into a simple 2D matrix
        gray_scale_image = image.convert('L')

        # Convert to a numpy array
        np_arr = np.asarray(gray_scale_image)

        (width, height) = np_arr.shape

        # with this two cycle we set to 255 the
        # pixel where the cone is placed.
        for i in range(0, width):
            for j in range(0, height):
                pixel = np_arr[i][j]
                if pixel == 255:
                    pixel = 0  # this is the background
                else:
                    pixel = 255
                # set the pixel
                np_arr[i][j] = pixel

        # return the matrix
        return np_arr

