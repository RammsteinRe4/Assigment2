import numpy as np


def euclideanDistance(firstData, secondData, lenght):

    distance = 0

    for a in range(lenght):
        distance += np.square(firstData - secondData)
    return np.sqrt(distance)


print(euclideanDistance(47, 32, 1))
