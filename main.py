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

def extract_data(filePath):
    print('Extractin data from ' + filePath + ' , please wait')
    dataList = []
    rawData = np.genfromtxt(filePath, delimiter=',', names=True, dtype=None, encoding=None)

    for _ in rawData:
        tempVoltage = rawData[0][3]
        tempAngle = rawData[1][3]

        dataList.append([tempVoltage, tempAngle])

        rawData = np.delete(rawData, 0)
        rawData = np.delete(rawData, 0)

        if rawData.__len__() == 0:
            print("Data extracted from file: " + filePath)
            break

    return dataList


dataListTrain = extract_data('analog_values.csv')
dataListTest = extract_data('measurements.csv')
kM.KMeanFunction(4, dataListTrain, dataListTest)
