from collections import deque 


def bfs(graph, start):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        print(f"{node} ", end="")

        for neighbors in graph.get(node, []):
            if neighbors not in visited:
                queue.append(neighbors)


graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 7],
    6: [3],
    7: [5],
}

bfs(graph, 1)
