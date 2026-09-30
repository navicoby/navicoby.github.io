import networkx as nx

g = nx.Graph()
g.add_edge("street_a", "junction", length=120)
g.add_edge("junction", "park_gate", length=180)
origin_connector_m = 25
gate_connector_m = 10
network_m = nx.shortest_path_length(
    g, "street_a", "park_gate", weight="length")
total_m = origin_connector_m + network_m + gate_connector_m
assert network_m == 300 and total_m == 335
print("network:", network_m, "m; door-to-gate estimate:", total_m, "m")
