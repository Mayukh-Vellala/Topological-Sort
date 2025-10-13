"""
Topological Sort Implementation
Author: Your Name
Date: October 2025

Implements two algorithms for topological sorting:
1. Kahn's Algorithm (BFS-based)
2. DFS-based Topological Sort

Also includes:
- Cycle detection
- Validation of topological order
- Dataset loading utilities
"""

from collections import defaultdict, deque
import json
import random
import time

def kahn_topological_sort(graph):
    """
    Kahn's Algorithm for Topological Sort
    graph: dict {node: list of neighbors}
    Returns: list of nodes in topological order, or None if cycle exists
    """
    # Calculate in-degrees
    in_degree = defaultdict(int)
    for node in graph:
        in_degree[node] = 0
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Queue for nodes with in-degree 0
    queue = deque([node for node in graph if in_degree[node] == 0])
    topo_order = []

    while queue:
        current = queue.popleft()
        topo_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we didn't visit all nodes, there's a cycle
    if len(topo_order) != len(graph):
        return None  # Cycle detected
    return topo_order

def dfs_topological_sort(graph):
    """
    DFS-based Topological Sort
    Returns: list of nodes in topological order, or None if cycle exists
    """
    visited = set()
    stack = []
    rec_stack = set()  # For cycle detection

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True  # Cycle detected
            elif neighbor in rec_stack:
                return True  # Back edge -> cycle

        rec_stack.remove(node)
        stack.append(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return None  # Cycle detected

    return stack[::-1]  # Reverse to get topological order

def is_valid_topological_order(graph, order):
    """
    Check if the given order is a valid topological sort.
    """
    if order is None:
        return False

    pos = {node: idx for idx, node in enumerate(order)}
    
    for node in graph:
        for neighbor in graph[node]:
            if pos[node] >= pos[neighbor]:  # Violation: neighbor should come after node
                return False
    return True

def generate_random_dag(n, edge_prob=0.3):
    """
    Generate a random DAG with n nodes.
    Uses topological ordering to ensure acyclicity.
    """
    graph = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i+1, n):  # Only forward edges -> guarantees DAG
            if random.random() < edge_prob:
                graph[i].append(j)
    return graph

def run_test_case(case_num, graph, description):
    print(f'Test Case {case_num}: {description}')
    print('Graph:', dict(list(graph.items())[:5]), "..." if len(graph) > 5 else "")
    
    start = time.perf_counter()
    kahn_result = kahn_topological_sort(graph)
    kahn_time = time.perf_counter() - start
    
    start = time.perf_counter()
    dfs_result = dfs_topological_sort(graph)
    dfs_time = time.perf_counter() - start
    
    print('Kahn result length:', len(kahn_result) if kahn_result else 'Cycle detected')
    print('DFS result length:', len(dfs_result) if dfs_result else 'Cycle detected')
    print(f'Kahn time: {kahn_time:.6f} seconds')
    print(f'DFS time: {dfs_time:.6f} seconds')
    
    if kahn_result:
        kahn_valid = is_valid_topological_order(graph, kahn_result)
        print(f'Kahn valid: {kahn_valid}')
    if dfs_result:
        dfs_valid = is_valid_topological_order(graph, dfs_result)
        print(f'DFS valid: {dfs_valid}')
    print()

# Main execution
if __name__ == "__main__":
    print("=== TOPOLOGICAL SORT DEMONSTRATION ===\n")

    # Edge Case 1: Single vertex
    run_test_case(1, {0: []}, 'Single vertex')

    # Edge Case 2: Two disconnected vertices
    run_test_case(2, {0: [], 1: []}, 'Two disconnected vertices')

    # Edge Case 3: Linear chain
    run_test_case(3, {0: [1], 1: [2], 2: [3], 3: []}, 'Linear chain')

    # Edge Case 4: Graph with cycle
    cyclic_graph = {0: [1], 1: [2], 2: [0]}  # Cycle: 0->1->2->0
    run_test_case(4, cyclic_graph, 'Graph with cycle')

    # Edge Case 5: Random DAG
    random_dag = generate_random_dag(10)
    run_test_case(5, random_dag, 'Random DAG (10 nodes)')

    # Edge Case 6: Large random DAG
    large_dag = generate_random_dag(100)
    run_test_case(6, large_dag, 'Large random DAG (100 nodes)')

    # Real-world dataset examples
    print("=== REAL-WORLD DATASETS ===\n")

    # MIT CS Curriculum
    mit_cs_courses = {
        '6.0001': ['6.0002'],
        '6.0002': ['6.006', '6.009'],
        '6.006': ['6.046'],
        '6.009': ['6.034'],
        '6.046': ['6.854'],
        '6.034': [],
        '6.036': ['6.867'],  # Machine Learning
        '6.867': [],
        '6.042': ['6.046'],  # Discrete Math -> Algorithms
    }
    run_test_case(7, mit_cs_courses, 'MIT CS Curriculum')

    # Maven Dependencies
    maven_dependencies = {
        'junit': [],
        'mockito': ['junit'],
        'slf4j-api': [],
        'logback-classic': ['slf4j-api'],
        'spring-core': ['slf4j-api'],
        'spring-context': ['spring-core', 'slf4j-api'],
        'spring-web': ['spring-context', 'spring-core'],
        'spring-boot-starter': ['spring-web', 'spring-context', 'logback-classic'],
        'my-app': ['spring-boot-starter', 'junit', 'mockito'],
    }
    run_test_case(8, maven_dependencies, 'Maven Build Dependencies')

    print("=== EXPERIMENTS COMPLETED ===")
