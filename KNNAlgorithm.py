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

        print('KNN Algorithm finished the results are show next, but first...')
        print()
        printResults(centroids)

def trial(distance, status):
    toTrial = []
    for pledge, _ in enumerate(distance):
        toTrial.append(distance[pledge][1])
    verdict = max(Counter(toTrial))
    verdict.actualPoints.append(status)
    verdict.inKNN += 1

def printResults(centroids):
    for centroid in centroids:
            print("Centroid: " + str(centroid.label) + " has: " + str(len(centroid.actualPoints)) + ' status')
            print('Centroid Location: ' + str(centroid.position))
            print('After KNN Algorithm ' + str(centroid.inKNN) + " status more were added")
            print()

    decision = input('Do you want to display all elements assigned to each centroid? (1 = Yes)')
    if int(decision) == 1:
        for centroid in centroids:
            print('Centroid Location: ' + str(centroid.position))
            for status, i in enumerate(centroid.actualPoints):
                print('Status' + str(centroid.position))
            print()
