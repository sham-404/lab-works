def dfs(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        print(f"{node} ", end="")

        for neighbors in graph.get(node, []):
            if neighbors not in visited:
                stack.append(neighbors)


graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 7],
    6: [3],
    7: [5],
}

dfs(graph, 1)
