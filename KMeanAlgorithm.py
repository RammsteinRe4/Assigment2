"""

Code for KMean Algorithm """
"""Assignment II of Computer Applications for Powers Systems (CAPS) VT-19
Group 3:
Héctor Manuel Martínez Álvarez 910218
Cristhian Carim Jiménez Saldaña 931023 0397
"""
import numpy as np
import operator
import random as rd
import KNNAlgorithm as kN

"""
KMean main function is executed here, first random centroids are created, then relocated to have 
an even distribution of the centroids for data to be assign in 4 clusters, then, each point is located
to the closest cluster. After,the centroids are re-located according to their points. The cluster are label
to finally plot the plot results 
"""


class Centroid:
    def __init__(self):
        self.position = []
        self.actualPoints = []
        self.pastPoints = []
        self.color = None
        self.label = 'none'
        self.aV = 0
        self.aA = 0

        for _ in range(9):
            self.position.append(([rd.uniform(0.0, 1.5), rd.uniform(0.0, 1.5)]))

        self.inKNN = 0
        self.defPost = [[1.0, 0.0], [0.9999999999999998, -21.234761856647637], [1.0, -25.650748058437067], [0.8935596216674565, -15.451415250157352], [0.853067982447191, -28.140322613737737], [0.9553350523459541, -28.6394349989884], [0.9057645575872234, -33.42412682343994], [0.9375200518487891, -27.4730883527749], [0.8021914969333384, -30.237854437768455]]


def extract_point(status):
    """Extract voltage and angle for each bus, 9 buses are a status"""
    points = []

    for bus in status:
        points.append([bus.voltage, bus.angle])

    return points


def getPosition(status):
    position = []

    for bus in status:
        position.append([bus.voltage, bus.angle])

    return position


class KMeanFunction:
    def __init__(self, num_of_centroids, dataListTrain, dataListTest):
        print('K-Means Algorithm loading...')

        """Initialize centroids"""
        self.num_of_centroids = num_of_centroids
        self.centroids = []
        for _ in range(num_of_centroids):
            self.centroids.append(Centroid())

        """Assign colors to centroids"""
        color_centroids = ("red", "green", "blue", "orange")
        for pos, centroid in enumerate(self.centroids):
            centroid.color = color_centroids[pos]

        self.locate_centroid(dataListTrain)
        self.point_to_cluster(dataListTrain, train=True)
        self.label_centroids()
        kN.KNNFunction(dataListTest, self.centroids)

    def locate_centroid(self, dataListTrain):
        tempSum1 = 0
        tempSum2 = 0
        tempSum3 = 0
        tempSum4 = 0
        LAPD = 0
        dist = {}


        #For centroid 1

        for status in dataListTrain:
            pointsList = extract_point(status)
            for points in pointsList:
                tempSum1 += np.square(self.centroids[0].position[LAPD][0] - points[0]) + np.square(self.centroids[0].position[LAPD][1] - points[1])
                LAPD += 1
            tempSum1 = np.sqrt(tempSum1)
            dist[status] = tempSum1
            tempSum1 = 0
            LAPD = 0

        newPosition = getPosition(max(dist.items(), key=operator.itemgetter(1))[0])
        self.centroids[0].position = newPosition
        dist = {}

        #For centroid 2

        for status in dataListTrain:
            pointsList = extract_point(status)
            for points in pointsList:
                tempSum1 += np.square(self.centroids[0].position[LAPD][0] - points[0]) + np.square(self.centroids[0].position[LAPD][1] - points[1])
                tempSum2 += np.square(self.centroids[1].position[LAPD][0] - points[0]) + np.square(self.centroids[1].position[LAPD][1] - points[1])
                LAPD += 1
            dist[status] = (np.sqrt(tempSum1) + np.sqrt(tempSum2)) / 2
            tempSum1 = 0
            tempSum2 = 0
            LAPD = 0

        newPosition = getPosition(min(dist.items(), key=operator.itemgetter(1))[0])
        if newPosition > self.centroids[1].defPost:
            self.centroids[1].position = self.centroids[1].defPost
        dist = {}

        #For centroid 3

        for status in dataListTrain:
            pointsList = extract_point(status)
            for points in pointsList:
                tempSum1 += np.square(self.centroids[0].position[LAPD][0] - points[0]) + np.square(self.centroids[0].position[LAPD][1] - points[1])
                tempSum2 += np.square(self.centroids[1].position[LAPD][0] - points[0]) + np.square(self.centroids[1].position[LAPD][1] - points[1])
                tempSum3 += np.square(self.centroids[2].position[LAPD][0] - points[0]) + np.square(self.centroids[2].position[LAPD][1] - points[1])
                LAPD += 1
            dist[status] = (np.sqrt(tempSum1) + np.sqrt(tempSum2) + np.sqrt(tempSum3)) / 3
            tempSum1 = 0
            tempSum2 = 0
            tempSum3 = 0
            LAPD = 0

        newPosition = getPosition(max(dist.items(), key=operator.itemgetter(1))[0])
        self.centroids[2].position = newPosition
        dist = {}

        # For centroid 4

        for status in dataListTrain:
            pointsList = extract_point(status)
            for points in pointsList:
                tempSum1 += np.square(self.centroids[0].position[LAPD][0] - points[0]) + np.square(self.centroids[0].position[LAPD][1] - points[1])
                tempSum2 += np.square(self.centroids[1].position[LAPD][0] - points[0]) + np.square(self.centroids[1].position[LAPD][1] - points[1])
                tempSum3 += np.square(self.centroids[2].position[LAPD][0] - points[0]) + np.square(self.centroids[2].position[LAPD][1] - points[1])
                tempSum4 += np.square(self.centroids[3].position[LAPD][0] - points[0]) + np.square(self.centroids[3].position[LAPD][1] - points[1])
                LAPD += 1
            dist[status] = (np.sqrt(tempSum1) + np.sqrt(tempSum2) + np.sqrt(tempSum3) + np.sqrt(tempSum4)) / 4
            tempSum1 = 0
            tempSum2 = 0
            tempSum3 = 0
            tempSum4 = 0
            LAPD = 0

        newPosition = getPosition(max(dist.items(), key=operator.itemgetter(1))[0])
        self.centroids[3].position = newPosition

        return print()

    def point_to_cluster(self, dataListTrain, train):
        """Given points are assign to each cluster"""
        halt = False
        final = 0

        while not halt:
            for status in dataListTrain:
                points = extract_point(status)
                closest_cluster = self.assign_to_cluster(points)
                closest_cluster.actualPoints.append(points)

            if self.checkStop():
                halt = True
            elif train:
                self.relocation()

    def checkStop(self):
        stop = False
        if self.centroids[0].actualPoints == self.centroids[0].pastPoints:
            if self.centroids[1].actualPoints == self.centroids[1].pastPoints:
                if self.centroids[2].actualPoints == self.centroids[2].pastPoints:
                    if self.centroids[3].actualPoints == self.centroids[3].pastPoints:
                        stop = True

        return stop

    def assign_to_cluster(self, points):
        """Find the closet closer to the points according to the euclidean distance"""
        dist = {}
        tempSum = 0
        LAPD = 0

        for centroid in self.centroids:
            for point in points:
                tempSum += np.square(centroid.position[LAPD][0] - point[0]) + np.square(centroid.position[LAPD][1] - point[1])
                LAPD += 1
            tempSum = np.sqrt(tempSum)
            dist[centroid] = tempSum
            LAPD = 0
            tempSum = 0

        close_cluster = min(dist.items(), key=operator.itemgetter(1))[0]

        return close_cluster

    def relocation(self):
        newPosition = []
        pre_x = [0] * 9
        pre_y = [0] * 9

        for centroid in self.centroids:
            if centroid.actualPoints:
                for pointIn in centroid.actualPoints:
                    for bus in range(9):
                        pre_x[bus] += pointIn[bus][0]
                        pre_y[bus] += pointIn[bus][1]
                for bus in range(9):
                    newPosition.append([pre_x[bus] / len(centroid.actualPoints), pre_y[bus] / len(centroid.actualPoints)])
                centroid.position = newPosition
                pre_x = [0]*9
                pre_y = [0]*9
                newPosition = []

            centroid.pastPoints = centroid.actualPoints
            centroid.actualPoints = []

    def label_centroids(self):
        #For high and low load

        temp = 0
        te = {}

        for centroid in self.centroids:
            for point in centroid.actualPoints:
                temp += point[0][1] - point[3][1]
            te[centroid] = temp / len(centroid.actualPoints)
            temp = 0

        tempLoad = max(te.items(), key=operator.itemgetter(1))[0]
        tempLoad.label = 'High Load'
        tempLoad = min(te.items(), key=operator.itemgetter(1))[0]
        tempLoad.label = 'Low Load'

        #For Generator Down

        temp = 0
        te = {}

        for centroid in self.centroids:
            for point in centroid.actualPoints:
                temp += point[2][1] - point[5][1]
                te[centroid] = temp / len(centroid.actualPoints)
            temp = 0
        tempLoad = min(te.items(), key=operator.itemgetter(1))[0]
        tempLoad.label = 'Generator Down'


        #For Line Down

        #By Default

        for centroid in self.centroids:
         if centroid.label == 'none':
             centroid.label = "Line Down"
             break


        #By Calculation

        temp = 0
        te = {}
        PtR1 = 0
        PtR2 = 0

        # for centroid in self.centroids:
        #      for point in centroid.actualPoints:
        #          PtR1 = cmath.rect(point[4][0], (point[4][1] * np.pi)/180)
        #          PtR2 = cmath.rect(point[5][0], (point[5][1] * np.pi)/180)
        #          temp += PtR1 - PtR2
        #      te[centroid] = np.absolute(temp / len(centroid.actualPoints))
        #      temp = 0
        # newL = te
        #
        self.printResults()

    def printResults(self):
        for centroid in self.centroids:
            print("Centroid: " + str(centroid.label) + " has: " + str(len(centroid.actualPoints)) + ' status')
            print()
