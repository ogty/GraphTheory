import networkx as nx
import matplotlib.pyplot as plt


m, n = 3, 4
G = nx.grid_2d_graph(m, n)

pos = {(i, j): (i, j) for (i, j) in G.nodes()} 
edges = nx.max_weight_matching(G)

plt.title("Maximum Matching")
nx.draw(G, pos=pos, width=5, node_size=10, edgelist=edges, edge_color="orange")
plt.show()