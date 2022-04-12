import matplotlib.pyplot as plt
import networkx as nx


A = {
    1: [4, 5], 
    2: [5], 
    3: [6],
}
B = {
    4: [1, 2], 
    5: [2], 
    6: [3],
}

A_nodes = [i for i in A.keys()]
B_nodes = [i for i in B.keys()]
nodes = A_nodes + B_nodes

patterns = []
for top, connect_tops in A.items():
    for connect_top in connect_tops:
        patterns.append((top, connect_top))

for top, connect_tops in B.items():
    for connect_top in connect_tops:
        patterns.append((top, connect_top))

fig = plt.figure()
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(patterns)
nx.draw(G, with_labels=True)
plt.show()
fig.savefig("../images/graph_10_2.png")
