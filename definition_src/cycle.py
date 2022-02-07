import matplotlib.pyplot as plt
import networkx as nx


graph_data = {
    1: [2],
    2: [3],
    3: [4],
    4: [1]
}

nodes = [i for i in graph_data.keys()]
patterns = []
for top, connect_tops in graph_data.items():
    for connect_top in connect_tops:
        patterns.append((top, connect_top))

fig = plt.figure()
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(patterns)
nx.draw(G, with_labels=True)
plt.show()
fig.savefig("../images/graph_10_5.png")
