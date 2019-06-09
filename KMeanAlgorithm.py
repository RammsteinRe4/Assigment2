import numpy as np
import matplotlib.pyplot as plt
import operator
import random as rd


class KMeanFunction:
    def __init__(self, num_of_centroids, pointsListTrain):

        self.num_of_centroids = num_of_centroids
        self.centroids = []

        for x in range(num_of_centroids):
            self.centroids.append(Centroid(np.array([rd.uniform(0.0, 1.5), rd.uniform(0.0, 1.5)])))

        color_centroids = ("red", "green", "blue", "orange")
        for pos, centroid in enumerate(self.centroids):
            centroid.color = color_centroids[pos]

        self.locate_centroid(pointsListTrain)

        self.cluster_point(pointsListTrain)
        #self.cluster_point(pointsListTest)
        self.plot_graph()
        print('Process Finished')

    def locate_centroid(self, pointList, item=0):

        dist = []
        x = 1
        sorted_list = sorted(pointList, key=lambda k: [k[1], k[0]])
        longo = max(sorted_list)

        for _ in self.centroids:
            if item == 0:
                self.centroids[item].location = longo
                item += 1

            elif item != 0:
                for _ in pointList:
                    dist.append(np.linalg.norm(self.centroids[item-1].position - pointList[x]))
                    x += 1
                self.centroids[item].location = max(dist)
                item += 1



    def cluster_point(self, pointsList):

        halt = False

        while not halt:
            for point in pointsList:
                toPoint = [point.angle, point.voltage]
                closest_cluster = self.assign_to_cluster(toPoint)
                closest_cluster.actualPoints.append(toPoint)

            if len([c for c in self.centroids if c.actualPoints == c.pastPoints]) == self.num_of_centroids:
                halt = True
                self.relocation(reset=False)
            else:
                self.relocation()

    def assign_to_cluster(self, point):

        dist = {}
        x = 0

        for centroid in self.centroids:
            dist[centroid] = np.linalg.norm(self.centroids[x].position - point)
            x += 1

        close_cluster = min(dist.items(), key=operator.itemgetter(1))[0]

        return close_cluster

    def relocation(self, pre_x=0, pre_y=0, reset=True):

        for centroid in self.centroids:
            centroid.pastPoints = centroid.actualPoints

            x = 0
            for _ in centroid.actualPoints:
                pre_x += float(centroid.actualPoints[x][0])
                x += 1

            y = 0
            for _ in centroid.actualPoints:
                pre_y += float(centroid.actualPoints[y][1])
                y += 1

            try:
                centroid.position[0] = pre_x / x
                centroid.position[1] = pre_y / y
            except:
                pass

            if reset:
                centroid.actualPoints = []

    def plot_graph(self):

        for i, c in enumerate(self.centroids):
            plt.scatter(c.position[0], c.position[1], marker='o', color=c.color, s=75)
            x_cors = [x[0] for x in c.actualPoints]
            y_cors = [y[1] for y in c.actualPoints]
            plt.scatter(x_cors, y_cors, marker='.', color=c.color)

        title = 'K-Means'
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(title)
        plt.show()


class Centroid:
    def __init__(self, position):
        self.position = position
        self.actualPoints = []
        self.pastPoints = []
        self.color = None


