import numpy as np

if __name__ == "__main__":
    one = np.arange(4)
    print("One dimensional array:")
    print(one)
    two = np.arange(8).reshape(2, 4)
    print("Two-dimensional array:")
    print(two)
    for x, y in np.nditer([one, two]):
        print("%d:%d" % (x, y), )
