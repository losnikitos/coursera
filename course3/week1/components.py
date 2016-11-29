# python3

import sys


class Graph:
    def __init__(self, edges=None):
        if edges is None:
            self.edges = []
            return
        self.edges = [[] for _ in edges]
        for edge in edges:
            if len(edge):
                a, b = edge
                self.edges[a - 1].append(b - 1)
                self.edges[b - 1].append(a - 1)

    def read(self):
        n_vertices, n_edges = map(int, sys.stdin.readline().split())
        self.edges = [[] for _ in range(n_vertices)]

        for line in range(n_edges):
            a, b = map(int, sys.stdin.readline().split())
            self.edges[a - 1].append(b - 1)
            self.edges[b - 1].append(a - 1)

        return self

    def n_components(self):
        vertices = list(range(len(self.edges)))
        # print('init vertices', vertices)
        color = 0
        while len(vertices):
            color += 1
            will_visit = vertices[-1:]
            # print('start', will_visit)
            visited = []
            while len(will_visit):
                current = will_visit.pop()
                if current in visited:
                    continue
                # print('goto', current)
                visited.append(current)
                vertices.remove(current)
                will_visit.extend(self.edges[current])
                # print('adjacent edges', self.edges[current])
                # print('left with this color', will_visit)
        return color


# TEST

# def test(adj, answer):
#     g = Graph(adj)
#     res = g.n_components()
#     print('ok' if res == answer else 'wrong: expected %s instead of %s' % (answer, res))
#
#
# g1 = [[1, 2], [3, 2], [4, 3], [1, 4]]
# g2 = [[1, 2], [3, 2], [], []]
# test(g1, 1)
# test(g2, 2)

# RUN

g = Graph().read()
print(g.n_components())
