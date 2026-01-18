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

def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth {depth}...")

        if dls(graph, start, goal, depth + 1):
            print(f"Goal '{goal}' found at depth {depth}")
            return

    print(f"Goal '{goal}' NOT found within depth {max_depth}")


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["G"],
    "F": ["G"],
    "G": [],
}

iterative_deepening_search(graph, 'A', 'B', 2)
