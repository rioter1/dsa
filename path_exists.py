from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_path_exists(self, start, end, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)

        if start == end:
            return True

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                if self.dfs_path_exists(neighbor, end, visited):
                    return True

        return False

    def bfs_path_exists(self, start, end):
        visited = set()
        queue = deque([start])

        while queue:
            current = queue.popleft()

            if current == end:
                return True

            visited.add(current)

            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return False

# Example usage:
# Construct a graph
#   1 -- 2 -- 4
#   |    |
#   v    v
#   3 -- 5

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 5)

start_vertex = 1
end_vertex = 4

# Check if a path exists using DFS
if graph.dfs_path_exists(start_vertex, end_vertex):
    print(f"Path exists between {start_vertex} and {end_vertex} using DFS.")
else:
    print(f"No path exists between {start_vertex} and {end_vertex} using DFS.")

# Check if a path exists using BFS
if graph.bfs_path_exists(start_vertex, end_vertex):
    print(f"Path exists between {start_vertex} and {end_vertex} using BFS.")
else:
    print(f"No path exists between {start_vertex} and {end_vertex} using BFS.")
