V = 4

def transitive_closure(graph):
    reach = [row[:] for row in graph]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

    return reach


def print_solution(reach):
    for i in range(V):
        print(" ".join(str(1 if i == j else reach[i][j]) for j in range(V)))


graph = [
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

reach = transitive_closure(graph)
print_solution(reach)
