import numpy as np
from collections import Counter
import KMeanAlgorithm as KM


class KNNFunction:
    def __init__(self, dataListTest, centroids):
        print('KNN Algorithm loading...')
        k = 5
        self.find_neighbour(dataListTest, centroids, k)

    def find_neighbour(self, dataListTest, centroids, jury):
        euclidean = 0
        dist = []

        for status in dataListTest:
            state = KM.extract_point(status)
            for centroid in centroids:
                for point in centroid.actualPoints:
                    for bus in range(9):
                        euclidean += np.square(point[bus][0] - state[bus][0]) + np.square(point[bus][1] - state[bus][1])
                    dist.append([np.sqrt(euclidean), centroid])
                    euclidean = 0
            trial(sorted(dist)[:jury], state)
            dist = []

        print('KNN Algorithm finished the results are:')
        print()
        printResults(centroids)

def trial(distance, status):
    toTrial = []
    for pledge, _ in enumerate(distance):
        toTrial.append(distance[pledge][1])
    verdict = max(Counter(toTrial))
    verdict.actualPoints.append(status)

def printResults(centroids):
    for centroid in centroids:
        print("Centroid: " + str(centroid.label) + " has: " + str(len(centroid.actualPoints)) + ' status')
        print()
        print()
