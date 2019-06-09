import numpy as np
from plotPoints import plot_graph
import KMeanAlgorithm as kM


def extract_data(filePath):

    rawData = np.genfromtxt(filePath, delimiter=',', names=True, dtype=None, encoding=None)

    for _ in rawData:
        tempVoltage = rawData[0][3]
        tempAngle = rawData[1][3]

        dataList.append([tempVoltage, tempAngle])

        rawData = np.delete(rawData, 0)
        rawData = np.delete(rawData, 0)

        if rawData.__len__() == 0:
            print("Data extracted")
            break

    return dataList


dataList = []
dataListTrain = extract_data('analog_values.csv')
#dataListTest = extract_data('measurements.csv')


# plot_graph(dataListTrain)
kM.KMeanFunction(4, dataListTrain)
#kM.KMeanFunction.cluster_point(dataListTrain)
#kM.KMeanFunction.position_centroid([5, 3, 0])


