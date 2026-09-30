import networkx as nx

g = nx.Graph()
g.add_edge("home", "crossing", length=100)
g.add_edge("crossing", "park", length=150)
g.add_edge("home", "park", length=400)
assert all("length" in d and d["length"] >= 0 for _,_,d in g.edges(data=True))
route = nx.shortest_path(g, "home", "park", weight="length")
distance = nx.shortest_path_length(g, "home", "park", weight="length")
assert route == ["home", "crossing", "park"]
assert distance == 250
print(route, distance, "m")
