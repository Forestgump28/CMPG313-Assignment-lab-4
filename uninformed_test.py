import networkx as nx
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs
from id_dfs import iddfs

# Your graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Create directed graph
G = nx.DiGraph()

# Add edges
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Draw
plt.figure(figsize=(6, 5))
pos = nx.spring_layout(G)  # auto layout

nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold',
    arrows=True
)

plt.title("Graph Representation")
plt.show()

START_NODE = 'A'
MAX_DEPTH = 3  # The deepest path A→B→E→G has 3 edges from root

print("BFS:", bfs(graph, START_NODE))
print("DFS:", dfs(graph, START_NODE))
print("IDDFS:", iddfs(graph, START_NODE, MAX_DEPTH))