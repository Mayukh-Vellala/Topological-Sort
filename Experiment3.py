def kahn_topological_sort_with_cycle_detection(graph):
2 in_degree = defaultdict(int)
3 for u in graph:
4 for v in graph[u]:
5 in_degree[v] += 1
6 queue = deque([u for u in graph if in_degree[u] == 0])
7 topo_order = []
8 while queue:
9 u = queue.popleft()
10 topo_order.append(u)
11 for v in graph[u]:
12 in_degree[v] -= 1
13 if in_degree[v] == 0:
14 queue.append(v)
15 if len(topo_order) != len(graph):
16 print("\textbf{Cycle detected! No valid topological order.}")
17 else:
18 print("\textbf{No cycle detected. Valid topological order found.}")
19 return topo_order
20
21 # Introduce a cycle manually for testing
22 dag_with_cycle = {0: [1], 1: [2], 2: [0]}
23 kahn_topological_sort_with_cycle_detection(dag_with_cycle)
