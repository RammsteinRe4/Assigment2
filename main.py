"""
Assignment II of Computer Applications for Powers Systems (CAPS) VT-19
Group 3:
Héctor Manuel Martínez Álvarez
Christian Carim Jiménez Saldaña

Some instructions: The default code will classify the learning set (analog_values.csv) with KMean Algorithm, then,
it will run the algorithm KNN to classify the test set (measurements.csv). The results will be save in a .png images,
the location of the images is the same as the program folder.
** Test set can also be classified with KMean Algorithm, see inside comments for details
"""

import numpy as np
import KMeanAlgorithm as kM


class Data:

    def __init__(self, name, voltage, angle, time):
        self.name = name
        self.voltage = voltage
        self.angle = angle
        self.time = time


class Status:

    def __init__(self, b1, b2, b3, b4, b5, b6, b7, b8, b9):
        self.buses = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
        #self.time = time
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= 8:
            self.start = -1
            raise StopIteration
        else:
            self.start += 1
            return self.buses[self.start]



def extract_data(filePath):
    print('Extracting data from ' + filePath + ' , please wait')
    dataList = []
    finalList = []
    rawData = np.genfromtxt(filePath, delimiter=',', names=True, dtype=None, encoding=None)
    sep = '_'

    for _ in rawData:
        tempVoltage = rawData[0][3]
        tempAngle = rawData[1][3]
        temptime = rawData[0][2]
        temptName = rawData[0][1]
        temptName = temptName.split(sep, 1)[0]

        dataList.append(Data(temptName, tempVoltage, tempAngle, temptime))

        rawData = np.delete(rawData, 0)
        rawData = np.delete(rawData, 0)

        if rawData.__len__() == 0:
            print("Data extracted from file: " + filePath)
            break

    while dataList:
        finalList.append(Status(dataList[0], dataList[1], dataList[2], dataList[3], dataList[4], dataList[5], dataList[6], dataList[7], dataList[8]))
        for i in range(9):
            dataList.pop(0)

    return finalList


dataListTrain = extract_data('measurements.csv')
dataListTest = extract_data('analog_values.csv')
kM.KMeanFunction(4, dataListTrain, dataListTest)
