graph = {
    5: [3, 7], 
    3: [2, 4],
    7: [8],
    2: [],
    4: [8],
    8: [],
}

def dfs(graph, node):
    stack = [node]
    visited = set()

    while stack:
        n = stack.pop()

        if n in visited:
            continue
        visited.add(n)
        print(n, end=" ")

        stack.extend(graph[n])


print("Depth First Search")
dfs(graph, 5)
