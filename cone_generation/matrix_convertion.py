from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from random import choices


def convert_image_to_matrix(filepath: str):
    with Image.open(filepath) as image:
        # Convert the image to GrayScale, so we convert a tensor into a simple matrix
        gray_scale_image = image.convert('L')
        # Convert to a numpy array
        np_arr = np.asarray(gray_scale_image)

        (width, height) = np_arr.shape

        print(np.unique(np_arr))

        for i in range(0, width):
            for j in range(0, height):
                pixel = np_arr[i][j]
                if pixel == 255:
                    pixel = 0  # this is the background
                else:
                    pixel = choices(
                        population=[255, 0],
                        weights=[0.1, 0.9],
                        k=1
                    )

                    pixel = pixel[0]

                # set the pixel
                np_arr[i][j] = pixel

        plt.imshow(np_arr)
        plt.show()


convert_image_to_matrix('./tmp/Figure_1.png')

