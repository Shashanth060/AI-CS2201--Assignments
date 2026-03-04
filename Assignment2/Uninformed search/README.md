## I have implemented Breadth-First Search (BFS),Depth-First Search (DFS),Depth-Limited Search (DLS),Iterative Deepening DFS (IDDFS) for Missionaries and Cannibals problem 

## Problem Definition
The Missionaries and Cannibals problem involves 3 missionaries and 3 cannibals on the left bank of a river, needing to cross to the right bank using a boat that can carry maximum 2 people. The constraint: missionaries must never be outnumbered by cannibals on either bank (unless no missionaries are present).


### 1. Breadth-First Search (BFS)
- Explores nodes level by level
- Guarantees shortest path (optimal solution)
- Uses queue data structure
- **Pros**: Guarantees optimal solution, complete
- **Cons**: High memory usage, explores many nodes

### 2. Depth-First Search (DFS)
- Explores one path completely before backtracking
- May find longer path first
- Uses stack data structure
- **Pros**: Low memory, finds solution quickly
- **Cons**: May find suboptimal solution

### 3. Depth-Limited Search (DLS)
- DFS with a depth cutoff
- Prevents infinite paths
- Takes depth limit as parameter
- **Pros**: Controlled exploration, memory efficient
- **Cons**: Requires correct limit guess

### 4. Iterative Deepening DFS (IDDFS)
- Repeatedly calls DLS with increasing limits
- Combines BFS optimality with DFS memory efficiency
- **Pros**: Optimal + memory efficient
- **Cons**: Repeats work, slower

```
| Algorithm | Time Complexity | Space Complexity | 
|-----------|-----------------|------------------|
| BFS       | O(b^d)          | O(b^d)           |
| DFS       | O(b^d)          | O(bd)            | 
| DLS       | O(b^l)          | O(bl)            |
| IDS       | O(b^d)          | O(bd)            | 

*b = branching factor , d = solution depth, l = depth limit
```
## How to Run the Code

### Compilation
```bash
gcc src/BFS.c -o bfs
gcc src/DFS.c -o dfs
gcc src/DLS.c -o dls
gcc src/IDS.c -o ids

```
