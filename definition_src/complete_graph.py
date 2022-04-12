import matplotlib.pyplot as plt
import networkx as nx


graph_data = {
    1: [2, 3, 4, 5],
    2: [1, 3, 4, 5],
    3: [1, 2, 4, 5],
    4: [1, 2, 3, 5],
    5: [1, 2, 3, 4]
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
fig.savefig("../images/graph_10_1.png")


# nx.complete_graphを使っても同様の結果が得られる
# G2 = nx.complete_graph(5)
# pos = nx.circular_layout(G2)
# plt.subplots(figsize=(6, 6))
# nx.draw_networkx(G2, pos, node_color="lightgray", edgecolors='k')
# plt.show()
