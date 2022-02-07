import networkx as nx
import matplotlib.pyplot as plt


m, n = 3, 4
G = nx.grid_2d_graph(m, n)

pos = {(i, j): (i, j) for (i, j) in G.nodes()} 

plt.figure()
plt.title("Problem")
nx.draw(G, pos=pos, node_size=100)
plt.show()
