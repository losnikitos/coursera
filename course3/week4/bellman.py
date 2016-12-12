# python 3

inf = float("inf")


def read_graph():
    n_vertices, n_edges = map(int, input().split())
    edges = [map(int, input().split()) for _ in range(n_edges)]
    return Graph(n_vertices, edges)


class Graph:
    def __init__(self, n_vertices=0, edges=[]):
        self.vertices = set(range(n_vertices))
        self.edges = [set() for v in self.vertices]
        for (a, b, w) in edges:
            self.edges[a - 1].add((b - 1, w))

    def visit(self, u, visited=set(), path=set()):
        if u in visited:
            return False

        visited.add(u)
        path.add(u)
        for v in self.edges[u]:
            if v in path or self.visit(v):
                return True
        path.remove(u)
        return False

    def has_cycles(self, fr, dist):

        dist[fr] = 0

        for i in range(len(self.vertices) - 1):
            changed = False
            for u in self.vertices:
                for (v, w) in self.edges[u]:
                    if dist[v] > dist[u] + w:
                        changed = True
                        dist[v] = dist[u] + w
            if not changed:
                return False

        changed = False
        for u in self.vertices:
            for (v, w) in self.edges[u]:
                if dist[v] > dist[u] + w:
                    changed = True
                    dist[v] = dist[u] + w

        return changed

    def has_negative_weight_cycles(self):
        dist = [inf for v in self.vertices]
        for v in self.vertices:
            if dist[v] == inf:
                if self.has_cycles(v, dist):
                    return True

        return False

    def __str__(self):
        return '\n'.join(['%s: %s' % (v, self.edges[v]) for v in self.vertices])


# TEST
def test(g, answer):
    res = g.has_negative_weight_cycles()
    print('ok' if res == answer else 'wrong: expected %s instead of %s' % (answer, res))


# test(Graph(4, [(1, 2, -5), (4, 1, 2), (2, 3, 2), (3, 1, 1)]), True)
# test(Graph(4, [(1, 2, 5), (4, 1, 2), (2, 3, 2), (3, 1, 1)]), False)
# test(Graph(4, [(2, 3, -1), (3, 4, -1), (4, 2, -1)]), True)

# RUN
g = read_graph()
print(1 if g.has_negative_weight_cycles() else 0)
