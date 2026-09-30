import networkx as nx

g = nx.Graph()
g.add_edge("gate", "A", length=160)
g.add_edge("A", "B", length=160)
g.add_edge("B", "C", length=160)
speed_m_per_min = 80
for _, _, data in g.edges(data=True):
    data["minutes"] = data["length"] / speed_m_per_min
reachable = nx.single_source_dijkstra_path_length(
    g, "gate", cutoff=5, weight="minutes")
assert reachable == {"gate":0, "A":2.0, "B":4.0}
print(reachable)
print("B-C 간선의 앞 80m도 5분 이내지만 노드 결과에는 나타나지 않습니다.")
