from heapq import heappush, heappop

class PrimMST:
    def __init__(self, g, start=0) -> None:
        self.graph = dict()
        self.start = start
        self.cost = float("inf")
        self.mst_edges = []
        for i, row in enumerate(g):
            self.graph[i] = []
            for j, weight in enumerate(row):
                if weight > 0:
                    self.graph[i].append((weight, j))

    def mst(self):
        visited = set()
        heap = []
        self.cost = 0

        heappush(heap, (0, self.start, None)) # (weight, node, parent)

        while heap and len(self.graph) > len(visited):
            weight, node, parent = heappop(heap)

            if node in visited:
                continue
            visited.add(node)

            if parent is not None:
                self.mst_edges.append((parent, node, weight))
                self.cost += weight

            for edge_weight, n in self.graph[node]:
                if n not in visited:
                    heappush(heap, (edge_weight, n, node))

    def print_mst(self):
        self.mst()
        print("Edges\tWeight")
        for u, v, w in self.mst_edges:
            print(f"{u} -> {v}     {w}")
            
        print(f"\nCost of the MST is {self.cost}")


graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0],
]

mst = PrimMST(graph)
mst.print_mst()

