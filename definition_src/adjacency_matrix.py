import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


A = np.array([
    [0, 1, 1, 1], 
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
])
fig = plt.figure()
tmp = nx.MultiGraph()
G = nx.from_numpy_matrix(A, parallel_edges=True, create_using=tmp)
nx.draw(G, with_labels=True)
plt.show()
fig.savefig("../images/graph_14.png")
