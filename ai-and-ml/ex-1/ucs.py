from heapq import heappush, heappop


def ucs(graph, start, end):
    heap = [(0, start)]
    visited = set()

    while heap:
        cost, node = heappop(heap)

        if node in visited:
            continue
        visited.add(node)

        if node == end:
            return cost

        for neighbor, node_cost in graph.get(node, []):
            if neighbor not in visited:
                heappush(heap, (node_cost + cost, neighbor))


graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("F", 3)],
    "D": [("G", 1)],
    "E": [("G", 2)],
    "F": [("G", 6)],
    "G": [],
}

print(ucs(graph, "A", "G"))
