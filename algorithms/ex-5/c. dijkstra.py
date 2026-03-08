# Combined weights: 0 means no edge, >0 is the weight
graph = [
    [0, 0, 1, 2, 0, 0, 0],
    [0, 0, 2, 0, 0, 3, 0],
    [1, 2, 0, 1, 3, 0, 0],
    [2, 0, 1, 0, 0, 0, 1],
    [0, 0, 3, 0, 0, 2, 0],
    [0, 3, 0, 0, 2, 0, 1],
    [0, 0, 0, 1, 0, 1, 0]
]

n = len(graph)
dist = [0] + [float("inf")] * (n - 1)
visited = [False] * n

for _ in range(n):
    # Find min distance node among unvisited
    u = -1
    for i in range(n):
        if not visited[i] and (u == -1 or dist[i] < dist[u]):
            u = i
    
    visited[u] = True
    
    # Update neighbors
    for v, weight in enumerate(graph[u]):
        if weight > 0 and not visited[v]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist

for i, d in enumerate(dist):
    print(f"Distance of {chr(97 + i)} from source: {d}")
