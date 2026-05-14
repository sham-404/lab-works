import heapq

def greedy_bfs(graph, heuristics, start, goal):
    queue = [(heuristics[start], start)]
    visited = set()
    path = []

    while queue:
        _, current = heapq.heappop(queue)
        path.append(current)

        if current == goal:
            return path

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(queue, (heuristics[neighbor], neighbor))

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}

heuristics = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 4,
    'G': 3,
    'H': 0
}

start, goal = 'A', 'H'

path = greedy_bfs(graph, heuristics, start, goal)

print(f"Path found: {' → '.join(path)}" if path else "No path found")
