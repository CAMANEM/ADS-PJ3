import networkx as nx

G = nx.Graph()
e = [("A", "B", 1), ("B", "C", 2), ("A", "C", 3), ("C", "D", 4), ("D", "E", 2), ("B", "E", 1)]
G.add_weighted_edges_from(e)
print(nx.dijkstra_path(G, "A", "D"))
