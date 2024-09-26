import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return -2 * np.sin(x - 2) + 1


if __name__ == "__main__":
    x = np.linspace(-6.28, 6.28, 3000)
    plt.plot(x, f(x))
    plt.show()
