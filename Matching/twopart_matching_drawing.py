import matplotlib.pyplot as plt
import networkx as nx


R = 10

foods = []
users = []
colorlist = ["red", "orange", "gold", "greenyellow", "green"] # Evaluation color

G = nx.DiGraph()

with open("./data/foods.txt", "r") as f:
    lines = f.readlines()
    
    for i in range(R):
        j = i * 9

        # Product ID
        line = lines[j]
        product_id = str(line.split(": ")[1])
        foods.append(product_id)
        
        # Profile Name
        line = lines[j + 2]
        profile_name = str(line.split(": ")[1])
        users.append(profile_name)
        
        # Score
        line = lines[j + 4]
        score = float(line.split(": ")[1])
        c = colorlist[int(score - 1)] # Correspond to the "colorlist index"
        
        G.add_node(product_id)
        G.add_node(profile_name)
        G.add_edge(profile_name, product_id, color=c)

edges = G.edges()
ecolors = [G[u][v]["color"] for u, v in edges]

pos = dict()
pos.update((node, (1, index)) for index, node in enumerate(foods))
pos.update((node, (0, index)) for index, node in enumerate(users))

plt.figure(figsize=(15, 15))
nx.draw(G, pos=pos, node_color="burlywood", edge_color=ecolors, with_labels=True)
plt.show()
