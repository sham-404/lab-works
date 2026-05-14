import heapq

def memory_bounded_a_star(graph, heuristic, start, goal, memory_limit=5):
    open_list = []

    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))

    closed_list = {}

    while open_list:
        if len(open_list) > memory_limit:
            open_list.pop()

        f, g, node, path = heapq.heappop(open_list)

        if node == goal:
            return path, g

        closed_list[node] = g

        for neighbor, cost in graph.get(node, {}).items():
            new_g = g + cost
            new_f = new_g + heuristic.get(neighbor, 0)

            if neighbor not in closed_list or new_g < closed_list[neighbor]:
                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, float('inf')

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'D': 3, 'E': 1},
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

path, cost = memory_bounded_a_star(
    graph,
    heuristic,
    'A',
    'H',
    memory_limit=5
)

if path:
    print("Optimal Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")
