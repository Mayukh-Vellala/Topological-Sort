def validate_topological_order(graph, topo_order):
2 position = {node: idx for idx, node in enumerate(topo_order)}
3 for u in graph:
4 for v in graph[u]:
5 \subsection*{\textbf{Experiment 3: Analyze detection of cycles and error ←-
,→ reporting}}
6 if position[u] > position[v]:
7 return False
8 return True
9
10 dag = generate_random_DAG(50, 0.15)
11 topo_order = kahn_topological_sort(dag)
12 is_valid = validate_topological_order(dag, topo_order)
13 print(f"\textbf{Valid topological order:} {is_valid}")
