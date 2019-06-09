import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize


def plot_graph(dataListTrain, dataListTest):

    for i, c in enumerate(self.centroids):
        plt.scatter(c.pos[0], c.pos[1], marker='o', color=c.color, s=75)
        x_cors = [x[0] for x in c.points]
        y_cors = [y[1] for y in c.points]
        plt.scatter(x_cors, y_cors, marker='.', color=c.color)

    title = 'K-Means'
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.savefig('{}.png'.format(title))
    plt.show()

