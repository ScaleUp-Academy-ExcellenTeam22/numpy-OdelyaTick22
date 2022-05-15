import numpy as np
import matplotlib.pyplot as plt


def sinus_drawing(x: np.array) -> None:
    """
    Function for computing the x and y coordinates for points on a sine curve and plot the points.
    :param x: An array of x values along a sine curve.
    :return: None
    """
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    x = np.arange(0, 2 * np.pi, 0.1)
    sinus_drawing(x)
