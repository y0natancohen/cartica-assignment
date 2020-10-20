# Installation

  `pip3 install -r requirements.txt`

# Using the program
  `python3 reachable.py my_input.json`
  
or
  
  `python3 reachable.py my_input --format csv`
  
add `--verbose` for verbose printing

# Running the tests

  `python3 test.py`

# How it works

1. Use the traversal rules and turn the array into a directed graph.

2. Build a spanning tree using BFS, starting from the first element/node.

3. Check if the spanning tree includes the last element/node. 

Why BFS? linear time (`O(V+E)`), loop implementation (DFS uses a recursive implementation), edges have the same weigts, so no need for Dijkstra.
