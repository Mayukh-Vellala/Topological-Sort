
## Implementation

Implemented in Python 3. The main functions `kahn_topological_sort` and `dfs_topological_sort` take a graph represented as an adjacency list (Python dictionary) and return the topological order or `None` if a cycle is detected.

## How to Run

### Prerequisites
*   Python 3.6 or higher

### Instructions
1.  Save the main Python code (containing `kahn_topological_sort`, `dfs_topological_sort`, `is_valid_topological_order`, `generate_random_dag`, `validate_on_dags`, `apply_to_scheduling`, etc.) as `toposort.py`.
2.  Create the `datasets` folder and place the JSON files containing the real-world datasets inside it (e.g., `maven_dependencies.json`, `mit_cs_courses.json`, etc.).
3.  Ensure the `starter_dataset.json` file is in the root directory if generated separately.
4.  Open your terminal or command prompt.
5.  Navigate to the `topological-sort-project` directory using `cd topological-sort-project`.
6.  Run the script using the Python interpreter:
    ```bash
    python toposort.py
    ```
    This will execute the main function which runs validation tests (Task 2) and applies the algorithms to scheduling examples (Task 3), demonstrating all three required tasks.

## Authors

*   **Yuvraj Singh Rajpurohit**
*   **Mayukh Vellala**
