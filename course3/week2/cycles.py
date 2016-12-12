# python3

import sys


class Graph:
    def __init__(self, num_vertices=0, edges=[]):
        self.num_vertices = num_vertices
        self.edges = [[] for _ in range(num_vertices)]
        for edge in edges:
            fr, to = map(lambda x: x - 1, edge)
            self.edges[fr].append(to)

    def read(self):
        self.num_vertices, n_edges = map(int, sys.stdin.readline().split())
        self.edges = [[] for _ in range(self.num_vertices)]

        for line in range(n_edges):
            a, b = map(int, sys.stdin.readline().split())
            self.edges[a - 1].append(b - 1)

        return self

    def visit(self, vertex, visited=set(), path=set()):
        if vertex in visited:
            return False

        visited.add(vertex)
        path.add(vertex)
        for neighbor in self.edges[vertex]:
            if neighbor in path or self.visit(neighbor):
                return True
        path.remove(vertex)
        return False

    def has_loops(self):
        return any(self.visit(v) for v in range(self.num_vertices))

    def __str__(self):
        return '\n'.join(['%s: %s' % (i, self.edges[i]) for i in range(self.num_vertices)])


# TEST

# def test(g, answer):
#     res = g.has_loops()
#     print('ok' if res == answer else 'wrong: expected %s instead of %s' % (answer, res))
#
#
# test(Graph(4, [(1, 2), (4, 1), (2, 3), (3, 1)]), True)
# test(Graph(5, [(1, 2), (2, 3), (1, 3), (3, 4), (1, 4), (2, 5), (3, 5)]), False)

# RUN

g = Graph().read()
print(1 if g.has_loops() else 0)
