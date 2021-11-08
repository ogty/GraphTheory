import networkx as nx
import matplotlib.pyplot as plt


m, n = 3, 4
G = nx.grid_2d_graph(m, n)
pos = {(i, j): (i, j) for (i, j) in G.nodes()} 

# Problem
plt.figure()
nx.draw(G, pos=pos, node_size=100)
plt.show()

# Maximal Matching
edges = nx.maximal_matching(G)
nx.draw(G, pos=pos, width=5, node_size=10, edgelist=edges, edge_color="orange")
plt.show()

# Maximum Matching
edges = nx.max_weight_matching(G)
nx.draw(G, pos=pos, width=5, node_size=10, edgelist=edges, edge_color="orange")
plt.show()