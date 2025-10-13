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
