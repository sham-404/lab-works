import heapq

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 3, 'E': 1, 'C': 2},
    'C': {'F': 5, 'G': 3},
    'D': {},
    'E': {'H': 4},
    'F': {'H': 3},
    'G': {'H': 2},
    'H': {}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 5,
    'E': 4,
    'F': 3,
    'G': 1,
    'H': 0
}

def a_star(graph, heuristic, start, goal):
    queue = [(0, start)]
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    came_from = {}

    while queue:
        _, current = heapq.heappop(queue)

        if current == goal:
            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)

            return path[::-1]

        for neighbor, cost in graph[current].items():
            temp_g = g_score[current] + cost

            if temp_g < g_score[neighbor]:
                g_score[neighbor] = temp_g
                f_score = temp_g + heuristic[neighbor]

                heapq.heappush(queue, (f_score, neighbor))
                came_from[neighbor] = current

    return None

start = 'A'
goal = 'H'

path = a_star(graph, heuristic, start, goal)

print(f"Shortest Path: {' -> '.join(path)}" if path else "No path found")
