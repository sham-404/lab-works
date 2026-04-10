V = 4
INF = 99999

def floyd_warshall(graph):
    dist = [row[:] for row in graph]  # copy

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def print_solution(dist):
    for row in dist:
        print(" ".join("INF" if x == INF else f"{x:2}" for x in row))


graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

dist = floyd_warshall(graph)
print_solution(dist)
