def dls(graph, start, end, limit):
    stack = [(start, 0)]
    visited = set()

    while stack:
        node, depth = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        if limit <= depth:
            continue

        if node == end:
            return True

        for neighbors in graph.get(node, []):
            if neighbors not in visited:
                stack.append((neighbors, depth + 1))

    return False


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["G"],
    "F": ["G"],
    "G": [],
}

print(dls(graph, "A", "G", 1))
