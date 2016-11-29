# python3

import sys


class Graph:
    def __init__(self, edges=None):
        self.edges = edges if edges is not None else []

    def read(self):
        n_vertices, n_edges = map(int, sys.stdin.readline().split())
        self.edges = [[] for _ in range(n_vertices)]

        for line in range(n_edges):
            a, b = map(int, sys.stdin.readline().split())
            self.edges[a - 1].append(b - 1)
            self.edges[b - 1].append(a - 1)

        return self

    def has_path(self, fr, to):
        will_visit = [fr]
        visited = []
        while len(will_visit):
            current = will_visit.pop()
            if current in visited:
                continue
            if current == to:
                return 1
            visited.append(current)
            will_visit.extend(self.edges[current])
        return 0

    def __repr__(self):
        return ['%s: %s' % (i, e) for i, e in enumerate(self.edges)]


# TEST

# def test(adj, fr, to, answer):
#     g = Graph(adj)
#     res = g.has_path(fr, to)
#     print('ok' if res == answer else 'wrong: expected %s instead of %s' % (answer, res))
#
#
# g1 = [[0, 1], [2, 1], [3, 2], [0, 3]]
# g2 = [[0, 1], [2, 1], [], []]
# test(g1, 0, 3, 1)
# test(g2, 0, 3, 0)

# RUN

g = Graph().read()
fr, to = map(int, sys.stdin.readline().split())
print(1 if g.has_path(fr - 1, to - 1) else 0)
