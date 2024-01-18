import matplotlib.pyplot as plt
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from([1, 2, 3, 4])

# Add edges
G.add_edges_from([(1, 2), (2, 4), (3, 4), (4, 3),(1,4)])

# Draw the graph
nx.draw(G, with_labels=True, font_weight='bold')

# Display the graph
plt.show()
