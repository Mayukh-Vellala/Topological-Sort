# Topological Sort — Design and Analysis of Algorithms Project

**Authors:** Yuvraj Singh Rajpurohit and Mayukh Vellala  
**Course:** Design and Analysis of Algorithms  
**Institution:** Indian Statistical Institute, Bengaluru  
**Date:** October 2025

---

## Project Overview

This project implements **Topological Sorting** on **Directed Acyclic Graphs (DAGs)** using two efficient algorithms:

- **Kahn’s Algorithm (BFS-based)**
- **DFS-based Topological Sort**

Both algorithms achieve optimal **O(V + E)** time complexity and are applied to a variety of datasets — synthetic and real-world — to validate correctness, performance, and robustness.

---

## Features

- Implementation of **Kahn’s** and **DFS-based** topological sort algorithms
- Automatic **cycle detection** for non-DAG graphs
- **Validation function** to check correctness of produced order
- Multiple **experiments** to evaluate scalability and correctness
- **Real-world datasets**:
  - Software build dependencies (Maven, Linux kernel)
  - Project task scheduling
  - Course prerequisite chains (MIT & Stanford CS curricula)
- **Starter dataset generator** (120 nodes)

---

## Algorithms Implemented

### 1. Kahn’s Algorithm
Iteratively removes nodes with in-degree zero and updates in-degrees of their neighbors.

### 2. DFS-based Algorithm
Performs depth-first search and appends vertices to the result stack after processing dependencies.

Both algorithms correctly handle:
- Disconnected graphs
- Empty graphs
- Cyclic graphs (detected and reported)

---

## Experiments

### **Experiment 1 — Randomly Generated DAGs**
Tests scalability and correctness of Kahn’s algorithm on randomly generated DAGs of increasing size.

```python
# Experiment 1: Random DAG Testing
for size in [10, 50, 100, 200]:
    dag = generate_random_DAG(size, edge_prob=0.1)
    topo_order = kahn_topological_sort(dag)
    print(f"Size: {size}, Order length: {len(topo_order)}")
