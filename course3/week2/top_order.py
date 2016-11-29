# python3


class Graph:
    def __init__(self, n_vertices=0, edges=[]):
        self.ordered = []
        self.vertices = set(range(n_vertices))
        self.edges = [set() for _ in range(n_vertices)]
        for edge in edges:
            a, b = edge
            self.edges[a - 1].add(b - 1)

    def read(self):
        n_vertices, n_edges = map(int, input().split())
        self.vertices = set(range(n_vertices))
        self.edges = [set() for _ in range(n_vertices)]

        for line in range(n_edges):
            a, b = map(int, input().split())
            self.edges[a - 1].add(b - 1)

        return self

    def remove(self, node):
        self.vertices.remove(node)
        for edge in self.edges:
            if node in edge:
                edge.remove(node)

    def visit(self, node):
        if node not in self.vertices:
            return

        for neighbor in self.edges[node]:
            self.visit(neighbor)

        # post visit
        if len(self.edges[node]) == 0:
            self.remove(node)
            self.ordered.insert(0, node)

    def top_order(self):
        for v in self.vertices:
            self.visit(v)
        return self.ordered

    def __str__(self):
        return '\n'.join(['%s: %s' % (v, self.edges[v]) for v in self.vertices])


# TEST
def test(g, answer):
    res = g.top_order()
    print('ok' if res == answer else 'wrong: expected %s instead of %s' % (answer, res))


test(Graph(4, [(1, 2), (4, 1), (3, 1)]), [4, 3, 1, 2])
test(Graph(4, [(3, 1)]), [2, 3, 1, 4])
test(Graph(5, [(2, 1), (3, 2), (3, 1), (4, 3), (4, 1), (5, 2), (5, 3)]), [5, 4, 3, 2, 1])

# RUN
g = Graph().read()
print(' '.join(g.top_order()))
