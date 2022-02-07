import matplotlib.pyplot as plt
import networkx as nx


A = {
    1: [4, 5, 6], 
    2: [4, 5, 6], 
    3: [4, 5, 6]
}
B = {
    4: [1, 2, 3], 
    5: [1, 2, 3], 
    6: [1, 2, 3]
}

A_nodes = [i for i in A.keys()]
B_nodes = [i for i in B.keys()]
nodes = A_nodes + B_nodes

patterns = []
for top, connect_tops in A.items():
    for connect_top in connect_tops:
        patterns.append((top, connect_top))

fig = plt.figure()
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(patterns)
nx.draw(G, with_labels=True)
plt.show()
fig.savefig("../images/graph_10_3.png")
