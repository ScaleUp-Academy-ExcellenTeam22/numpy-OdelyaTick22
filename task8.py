import numpy as np


def if_equal(arr: np.array, num: int) -> None:
    print(np.where(arr == num, 0, arr))


def if_less_than(arr: np.array, num: int) -> None:
    print(np.where(arr < num, -1, arr))


def if_greater_than(arr: np.array, num: int) -> None:
    print(np.where(arr > num, 1, arr))


if __name__ == "__main__":
    my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(my_array)
    if_equal(my_array, 9)
    if_less_than(my_array, 3)
    if_greater_than(my_array, 7)
