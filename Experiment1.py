import random
2 from collections import defaultdict, deque
3
4 def generate_random_DAG(num_nodes, edge_prob=0.2):
5 graph = defaultdict(list)
6 for i in range(num_nodes):
7 for j in range(i+1, num_nodes):
8 if random.random() < edge_prob:
9 graph[i].append(j)
10 return graph
11
12 def kahn_topological_sort(graph):
13 in_degree = defaultdict(int)
14 for u in graph:
15 for v in graph[u]:
16 in_degree[v] += 1
17 queue = deque([u for u in range(len(graph)) if in_degree[u] == 0])
18 topo_order = []
19 while queue:
20 u = queue.popleft()
21 topo_order.append(u)
22 for v in graph[u]:
23 in_degree[v] -= 1
24 if in_degree[v] == 0:
25 queue.append(v)
26 return topo_order
27
28 for size in [10, 50, 100, 200]:
29 dag = generate_random_DAG(size, edge_prob=0.1)
30 topo_order = kahn_topological_sort(dag)
31 print(f"\textbf{Size:} {size}, \textbf{Order length:} {len(topo_order)}")
