"""
Code for KMean Algorithm
"""
import numpy as np
import matplotlib.pyplot as plt
import operator
import random as rd
import KNNAlgorithm as kN
from operator import attrgetter

"""
KMean main function is executed here, first random centroids are created, then relocated to have 
an even distribution of the centroids for data to be assign in 4 clusters, then, each point is located
to the closest cluster. After,the centroids are re-located according to their points. The cluster are label
to finally plot the plot results 
"""

class KMeanFunction:
    def __init__(self, num_of_centroids, pointsListTrain, pointsListTest):
        print('K-Means Algorithm loading...')
        self.num_of_centroids = num_of_centroids
        self.centroids = []

        for x in range(num_of_centroids):
            self.centroids.append(Centroid(np.array([rd.uniform(0.0, 1.5), rd.uniform(0.0, 1.5)])))

        color_centroids = ("red", "green", "blue", "orange")
        for pos, centroid in enumerate(self.centroids):
            centroid.color = color_centroids[pos]

        self.locate_centroid(pointsListTrain)
        self.point_to_cluster(pointsListTrain, train=True)
        #self.point_to_cluster(pointsListTrain, train=False)
        self.label_centroids()
        self.plot_graph('KMeans Algorithm')
        print('K-Mean Algorithm finished, plot has been same in program folder')
        kN.KNNFunction(pointsListTest, self.centroids)
        self.plot_graph('KNN Algorithm')
        print('KNN Algorithm finished, plot has been same in program folder')
        print('Process Finished, this was AI :)')

    def locate_centroid(self, pointList, item=0):

        dist = []
        longo = max(pointList)

        for _ in self.centroids:
            if item == 0:
                self.centroids[item].position = longo
                item += 1

            elif item == 1:
                longo = min(pointList)
                self.centroids[item].position = longo
                item += 1

            elif item > 1:
                for index, _ in enumerate(pointList):
                    fur_point = pointList[index]
                    cen_point = self.centroids[item-1].position
                    temp = np.linalg.norm(np.array(cen_point) - np.array(fur_point))
                    dist.append(temp)
                    comp = max(dist)
                    if temp == comp:
                        self.centroids[item].position = fur_point
                item += 1

    def point_to_cluster(self, pointsList, train):
        halt = False

        while not halt:
            for point in pointsList:
                toPoint = [point[0], point[1]]
                closest_cluster = self.assign_to_cluster(toPoint)
                closest_cluster.actualPoints.append(toPoint)

            if len([c for c in self.centroids if c.actualPoints == c.pastPoints]) == self.num_of_centroids:
                halt = True
                if train:
                    self.relocation(reset=False)
            elif train:
                self.relocation()

    def assign_to_cluster(self, point):

        dist = {}
        x = 0

        for centroid in self.centroids:
            dist[centroid] = np.linalg.norm(self.centroids[x].position - np.array(point))
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

            pre_x = 0
            pre_y = 0

            if reset:
                centroid.actualPoints = []

    def label_centroids(self):

        mynewC = []
        myCentroids = self.centroids
        maxV = max(myCentroids, key=attrgetter('position'))
        maxV.label = "Low Load"
        minV = min(myCentroids, key=attrgetter('position'))
        minV.label = "High Load"

        for centroid in myCentroids:
            if centroid.label == 'none':
                mynewC.append(centroid)

        maxV = max(mynewC, key=attrgetter('position'))
        maxV.label = "Generator Down"
        minV = min(mynewC, key=attrgetter('position'))
        minV.label = "Line Down"

    def plot_graph(self,type):

        for i, c in enumerate(self.centroids):
            plt.scatter(c.position[0], c.position[1], marker='o', color=c.color, s=75)
            x_cors = [x[0] for x in c.actualPoints]
            y_cors = [y[1] for y in c.actualPoints]
            plt.scatter(x_cors, y_cors, marker='.', color=c.color, label=c.label)
            plt.legend(loc='upper left')

        title = type
        plt.xlabel('Voltage')
        plt.ylabel('Angle')
        plt.title(title)
        plt.savefig('{}.png'.format(title))
        plt.clf()


class Centroid:
    def __init__(self, position):
        self.position = position
        self.actualPoints = []
        self.pastPoints = []
        self.color = None
        self.label = 'none'
