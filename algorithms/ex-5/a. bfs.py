graph = {
    5: [3, 7], 
    3: [2, 4],
    7: [8],
    2: [],
    4: [8],
    8: [],
}

def bfs(graph, node):
    queue = [node]
    visited = []

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

print("Breadth First Search")
bfs(graph, 5)
