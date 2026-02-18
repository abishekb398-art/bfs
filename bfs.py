from collections import deque

def bfs(graph, start):
    visited = set()          # To keep track of visited nodes
    queue = deque([start])   # Queue for BFS

    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()   # Remove from front
        print(node, end=" ")

        # Visit all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Call BFS
bfs(graph, 'A')
