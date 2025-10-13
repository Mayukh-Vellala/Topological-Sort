This code implements Topological Sort to address the three tasks:
1. Implement topological sorting using DFS or Kahn's algorithm.
2. Validate on DAGs and discuss limitations on cyclic graphs.
3. Apply to scheduling and dependency resolution problems.
"""

from collections import defaultdict, deque
import json
import random
import time

# Task 1: Implement Topological Sorting using Kahn's Algorithm
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

# Task 1: Implement Topological Sorting using DFS-based Algorithm
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

# Task 2: Validate output ordering correctness
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

# Task 2: Generate random DAGs for testing
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

# Task 2: Validate on DAGs and discuss limitations on cyclic graphs
def validate_on_dags():
    """
    Validate the algorithms on various DAGs and discuss limitations on cyclic graphs.
    """
    print("=== VALIDATION ON DAGS AND CYCLIC GRAPHS ===\n")
    
    # Test Case 1: Simple DAG
    simple_dag = {0: [1], 1: [2], 2: []}
    print("Test Case 1: Simple DAG")
    kahn_result = kahn_topological_sort(simple_dag)
    dfs_result = dfs_topological_sort(simple_dag)
    print(f"Kahn's result: {kahn_result}")
    print(f"DFS result: {dfs_result}")
    print(f"Valid? {is_valid_topological_order(simple_dag, kahn_result)}\n")

    # Test Case 2: Complex DAG
    complex_dag = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    print("Test Case 2: Complex DAG")
    kahn_result = kahn_topological_sort(complex_dag)
    dfs_result = dfs_topological_sort(complex_dag)
    print(f"Kahn's result: {kahn_result}")
    print(f"DFS result: {dfs_result}")
    print(f"Valid? {is_valid_topological_order(complex_dag, kahn_result)}\n")

    # Test Case 3: Cyclic Graph
    cyclic_graph = {0: [1], 1: [2], 2: [0]}  # Cycle: 0->1->2->0
    print("Test Case 3: Cyclic Graph")
    kahn_result = kahn_topological_sort(cyclic_graph)
    dfs_result = dfs_topological_sort(cyclic_graph)
    print(f"Kahn's result: {kahn_result} (Cycle detected)")
    print(f"DFS result: {dfs_result} (Cycle detected)\n")

    # Discussion on Limitations
    print("=== DISCUSSION ON LIMITATIONS ===")
    print("Topological sort is only defined for Directed Acyclic Graphs (DAGs).")
    print("- If a cycle exists, no valid topological ordering exists because dependencies form a loop.")
    print("- Both algorithms correctly detect cycles by returning None.")
    print("- In real applications (like course prerequisites), cycles indicate logical errors that must be resolved manually.")

# Task 3: Apply to scheduling and dependency resolution problems
def apply_to_scheduling():
    """
    Apply topological sort to scheduling and dependency resolution problems.
    """
    print("=== APPLICATION TO SCHEDULING AND DEPENDENCY RESOLUTION ===\n")
    
    # Example 1: Course Prerequisite Scheduler
    courses = {
        'CS101': ['CS201'],
        'CS201': ['CS301', 'CS302'],
        'CS301': ['CS401'],
        'CS302': [],
        'CS401': [],
    }
    print("Example 1: Course Prerequisite Scheduler")
    kahn_result = kahn_topological_sort(courses)
    dfs_result = dfs_topological_sort(courses)
    print(f"Course Schedule (Kahn): {kahn_result}")
    print(f"Course Schedule (DFS): {dfs_result}")
    print(f"Valid? {is_valid_topological_order(courses, kahn_result)}\n")

    # Example 2: Software Build Dependencies
    build_dependencies = {
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
    print("Example 2: Software Build Dependencies")
    kahn_result = kahn_topological_sort(build_dependencies)
    dfs_result = dfs_topological_sort(build_dependencies)
    print(f"Build Order (Kahn): {kahn_result}")
    print(f"Build Order (DFS): {dfs_result}")
    print(f"Valid? {is_valid_topological_order(build_dependencies, kahn_result)}\n")

    # Example 3: Task Scheduling
    task_schedule = {
        'requirements': ['design', 'planning'],
        'design': ['implementation'],
        'planning': ['implementation'],
        'implementation': ['testing'],
        'testing': ['deployment'],
        'documentation': ['deployment'],
        'deployment': [],
        'code_review': ['testing'],
        'unit_tests': ['code_review'],
    }
    print("Example 3: Task Scheduling")
    kahn_result = kahn_topological_sort(task_schedule)
    dfs_result = dfs_topological_sort(task_schedule)
    print(f"Task Order (Kahn): {kahn_result}")
    print(f"Task Order (DFS): {dfs_result}")
    print(f"Valid? {is_valid_topological_order(task_schedule, kahn_result)}\n")

# Main execution
if __name__ == "__main__":
    print("=== TOPLOGICAL SORT IMPLEMENTATION FOR ALL THREE TASKS ===\n")
    
    # Task 1: Implementation
    print("TASK 1: IMPLEMENTATION OF TOPOLOGICAL SORT ALGORITHMS")
    print("Both Kahn's and DFS-based algorithms are implemented above.\n")
    
    # Task 2: Validation
    validate_on_dags()
    
    # Task 3: Application
    apply_to_scheduling()
    
    print("=== ALL THREE TASKS COMPLETED ===")
    print("The implementation successfully addresses all three tasks:")
    print("1. Implementation of topological sorting algorithms")
    print("2. Validation on DAGs and discussion of limitations on cyclic graphs")
    print("3. Application to scheduling and dependency resolution problems")
