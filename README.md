# Topological Sort: Kahn's & DFS Algorithms

> **Course:** Design and Analysis of Algorithms  
> **Authors:** Yuvraj Singh Rajpurohit & Mayukh Vellala  
> **Institution:** Indian Statistical Institute, Bangalore  
> **Program:** B.Math(Hons.) 3rd Year  
> **Date:** October 2025

---

## Executive Summary

This project presents a comprehensive implementation and analysis of **Topological Sort** algorithms for Directed Acyclic Graphs (DAGs). We rigorously implement and compare two fundamental approaches: **Kahn's Algorithm** (BFS-based) and a **DFS-based approach**, both achieving optimal **O(V + E) time complexity**.

Our work includes:
- Correct implementations of both Kahn's and DFS-based topological sort algorithms.
- Rigorous proof of correctness and complexity analysis.
- Extensive validation on synthetic and real-world datasets (6 datasets across 3 scenarios).
- Generation and testing of a starter dataset (120 nodes).
- Detailed discussion of challenges, limitations, and lessons learned.
- Clean, well-documented Python code.
- Comprehensive academic report following a formal structure.

This repository contains all necessary components for a complete academic project.

---

##  Problem Statement

Given a Directed Acyclic Graph (DAG) `G = (V, E)`, find a **linear ordering** of its vertices such that for every directed edge `(u, v)`, vertex `u` comes before vertex `v` in the ordering.

### Key Challenges
- Achieving optimal O(V + E) time complexity.
- Correctly detecting cycles (no valid ordering exists).
- Handling diverse real-world dependency structures.
- Ensuring correctness across various edge cases (empty graphs, disconnected components).

---

##  Methodology: Kahn's & DFS-Based Algorithms

### 1. Kahn's Algorithm (BFS-based)
- **Idea:** Repeatedly remove nodes with in-degree zero (no prerequisites).
- **Process:**
  1. Calculate in-degrees of all vertices.
  2. Initialize a queue with vertices having in-degree 0.
  3. While the queue is not empty:
     - Remove a vertex `u`, add it to the topological order.
     - Decrement the in-degree of its neighbors.
     - If a neighbor's in-degree becomes 0, add it to the queue.
  4. If all vertices are processed, return the order; otherwise, a cycle exists.

### 2. DFS-Based Algorithm
- **Idea:** Use Depth-First Search to build the order via post-order traversal.
- **Process:**
  1. Initialize a visited set and a result stack.
  2. For each unvisited vertex `v`:
     - Perform DFS from `v`.
     - Maintain a recursion stack to detect back edges (cycles).
     - When DFS from a vertex completes, push it onto the stack.
  3. Reverse the stack to get the final topological order.

### Time Complexity: `O(V + E)`
Both algorithms visit each vertex and edge exactly once.

### Space Complexity: `O(V)`
Used for storing in-degrees, visited sets, recursion stack, and the output order.

---

## Experiments & Results

We conducted comprehensive experiments to validate correctness and performance.

### Experiment 1: Scalability on Random DAGs
- **Tested:** DAGs of increasing size (50, 100, 150, 200 nodes).
- **Result:** Runtime scaled linearly with `V + E`, confirming O(V + E) complexity.

### Experiment 2: Correctness Validation
- **Tested:** Various graph types (simple chains, complex DAGs, random DAGs).
- **Result:** Output validated using a function checking the topological property (`pos[u] < pos[v]` for all edges `(u, v)`).

### Experiment 3: Cycle Detection
- **Tested:** Graphs with and without cycles.
- **Result:** Both algorithms correctly returned `None` for cyclic graphs.

### Real-World Datasets (6 Total)
We implemented and tested on 2 datasets for each of the following 3 scenarios:

1. **Build Dependency Graphs:**
   - Maven Build Dependencies
   - Linux Kernel Module Dependencies
2. **Task Scheduling:**
   - Software Development Project Tasks
   - Manufacturing Assembly Line Tasks
3. **Course Prerequisites:**
   - MIT Computer Science Curriculum
   - Stanford Computer Science Curriculum

**All datasets processed successfully with both algorithms.**

### Starter Dataset
- **Generated:** A random DAG with 160 nodes (within 50-200 range).
- **Result:** Processed correctly and efficiently by both algorithms.

# Results and Discussion

Our implementation of both **Kahn’s algorithm** and the **DFS-based topological sort** was rigorously tested across synthetic datasets, real-world scenarios, and the provided starter dataset.  
This section presents the findings on correctness, validation, and performance.

---

## Correctness and Validation

The correctness of both algorithms was verified through multiple approaches:

- **Edge Case Handling:**  
  Both algorithms correctly handled trivial cases like single vertices, disconnected components, and linear chains.  
  Example: For the graph `{A: [B], B: [C], C: []}`, both returned `[A, B, C]`.

- **Cycle Detection:**  
  Both algorithms successfully identified cycles.  
  Example: For `{0: [1], 1: [2], 2: [0]}`, both returned `None`, indicating a cycle was detected.

- **Order Validation:**  
  A dedicated function `is_valid_topological_order(graph, order)` was implemented to verify that for each edge `(u, v)`, the position of `u` precedes `v`.  
  All valid outputs from both algorithms passed this validation test.

**Summary:**  
Kahn’s algorithm ensures all predecessors of a vertex are processed before the vertex itself, while the DFS approach achieves this via post-order traversal, ensuring that vertices with dependencies appear later in the sequence.

---

## Performance Analysis

Performance was evaluated through the three experiments, confirming the theoretical time complexity of **O(V + E)**.

- **Experiment 1 (Scalability):**  
  Tested on randomly generated DAGs of increasing sizes (50, 100, 150, 200 nodes).  
  Runtime increased linearly with the number of nodes and edges, confirming **O(V + E)** scaling.  
  DFS was slightly faster in some cases due to smaller constant factors.

- **Experiment 2 (Real-World Datasets):**  
  Performance on six real-world datasets (Maven, Linux Kernel, Software Tasks, etc.) was **excellent**, completing almost instantaneously.  
  Confirms practical efficiency for realistic problem sizes.

- **Starter Dataset (120 Nodes):**  
  The starter dataset was processed correctly and efficiently by both algorithms, further validating correctness and scalability.

**Space Complexity:**  
Confirmed as **O(V)** — due to in-degree arrays (Kahn) or recursion stacks (DFS) and the result list.

---

## Summary of Findings

- Both Kahn’s and DFS-based algorithms correctly produce topological orderings for DAGs.  
- Both detect cycles accurately when present.  
- Performance scales linearly with graph size (**O(V + E)**).  
- Algorithms are robust across all edge cases and real-world datasets.

---

# Challenges Faced and Lessons Learned

Developing and testing both algorithms provided valuable technical and design insights.

---

## Technical Challenges

- **Cycle Detection Implementation:**  
  Managing the recursion stack in DFS was critical for distinguishing tree edges from back edges.  
  Early confusion between `visited` and recursion stack caused incorrect cycle detection in disconnected graphs.

- **Edge Case Handling:**  
  Handling graphs with no edges, single vertices, and multiple disconnected components required careful initialization.  
  For instance, ensuring nodes with zero in-degree were included in Kahn’s queue.

- **Dataset Format Consistency:**  
  Each graph had to be a complete dictionary.  
  If `u → v` existed, `v` had to appear as a key even if it had no outgoing edges.  
  This was important for JSON-based dataset generation.

---

## Design and Implementation Lessons

- **Algorithm Choice:**  
  - Kahn’s Algorithm is iterative, intuitive, and suitable for practical applications.  
  - DFS-based is elegant and concise but may suffer from recursion limits in very deep graphs.

- **Importance of Validation:**  
  Writing a separate validation function (`is_valid_topological_order`) was crucial for testing correctness across datasets.

- **Real-World Relevance:**  
  Applying the algorithms to real systems (builds, task scheduling, courses) strengthened understanding of their practical impact.

---

## Overall Insights

This project highlighted the **power and elegance of graph algorithms** in solving real-world dependency problems efficiently.  
Seemingly complex constraints (like task ordering or course prerequisites) can be handled systematically using **BFS (Kahn)** or **DFS (recursive)** paradigms.

Testing with diverse datasets and edge cases was key to ensuring **robustness and correctness**.

---

# Conclusion

---

## Discussion

Both **Kahn’s algorithm** and **DFS-based topological sort** outperform brute-force methods dramatically, achieving optimal **O(V + E)** time complexity.

Even on large inputs, both are extremely fast and practical.  
Their main challenge lies in **cycle detection** and **edge case management** rather than raw performance.

In contrast, a naive algorithm checking all permutations would take **O(n!)**, making it infeasible for real use.  
Efficient algorithms make topological sorting **scalable and realistic** for large graphs.

### Limitations
- Only applicable to **DAGs** (Directed Acyclic Graphs)  
- Cannot produce valid ordering if cycles exist (only detect them)  
- Memory usage grows linearly with number of vertices  
- Requires full in-memory graph representation  

---

## Summary

Both algorithms achieve their design goal of efficient topological sorting.  
They perform correctly on a wide range of datasets and scale predictably with input size.

---

## Key Findings

- Both methods are **optimal** for the problem with **O(V + E)** complexity  
- Offer substantial performance gains over naive methods  
- Require only **linear extra space**  
- Include **built-in cycle detection**  

---

## Possible Extensions

Future improvements could include:
- Generating **all possible topological orderings**  
- Handling **dynamic graphs** (where edges can change)  
- Developing **parallel or distributed** implementations for massive graphs  

---
