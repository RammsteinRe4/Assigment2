import numpy as np
from collections import Counter


class KNNFunction:
    def __init__(self, pointsListTest, centroids, k=5):
        print('KNN Algorithm loading...')
        print('This will take a while, in the meantime imagine this:')
        print('You are in a Mexican beach with a señorita and a bucket of beer')
        print("listening to Humperdinck's Can't Take My Eyes Off You")
        self.find_neighbour(pointsListTest, centroids, k)

    def find_neighbour(self, dataTrain, centroids, jury):
        for point, _ in enumerate(dataTrain):
            dist = []
            for centroid in centroids:
                for x, _ in enumerate(centroid.actualPoints):
                    euclidean = np.linalg.norm(np.array(dataTrain[point]) - np.array(centroid.actualPoints[x]))
                    dist.append([euclidean, centroid.label])
            self.trial(centroids, sorted(dist)[:jury], dataTrain[point])

    def trial(self, centroids, list, point):

        toTrial = []
        for pledge, _ in enumerate(list):
            toTrial.append(list[pledge][1])
        verdict = max(Counter(toTrial))
        self.assign_to_group(centroids,verdict, point )

    def assign_to_group(self, centroids, verdict, point):
        for centroid in centroids:
            if centroid.label == verdict:
                centroid.actualPoints.append(point)
                break
