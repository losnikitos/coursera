# python3


def read_graph():
    n_vertices, n_edges = map(int, input().split())
    edges = [map(int, input().split()) for _ in range(n_edges)]
    return Graph(n_vertices, edges)


class Graph:
    def __init__(self, n_vertices=0, edges=[]):
        self.vertices = set(range(n_vertices))
        self.edges = [set() for v in self.vertices]
        for edge in edges:
            a, b = edge
            self.edges[a - 1].add(b - 1)
            self.edges[b - 1].add(a - 1)

    def visit(self, fr, dist):
        if dist[fr] != -1:
            return False

        dist[fr] = 0
        queue = [fr]
        while len(queue):
            vertex = queue.pop(0)
            for neighbor in self.edges[vertex]:
                if dist[neighbor] == -1:
                    queue.append(neighbor)
                    dist[neighbor] = (dist[vertex] + 1) % 2
                elif dist[vertex] == dist[neighbor]:  # new vertex is same color
                    return True
        return False

    def is_bipartite(self):
        dist = [-1 for v in self.vertices]
        return 0 if any([self.visit(v, dist) for v in self.vertices]) else 1

    def __str__(self):
        return '\n'.join(['%s: %s' % (v, self.edges[v]) for v in self.vertices])


# TEST
# def test(g, answer):
#     res = g.is_bipartite()
#     print('ok' if res == answer else 'wrong: expected %s instead of %s' % (answer, res))
#
#
# test(Graph(4, [(1, 2), (4, 1), (2, 3), (3, 1)]), 0)
# test(Graph(5, [(5, 2), (4, 2), (3, 4), (1, 4)]), 1)
# test(Graph(3, []), 1)
# test(Graph(3, [(1, 2), (2, 3), (1, 3)]), 0)
# test(Graph(6, [(1, 2), (2, 3), (4, 5), (5, 6)]), 1)
# test(Graph(7, [(1, 2), (2, 3), (4, 5), (5, 6), (6, 7)]), 1)
# test(Graph(7, [(1, 2), (2, 3), (4, 5), (5, 6), (6, 7), (2, 5), (3, 5)]), 0)
# test(Graph(1, []), 1)
# test(Graph(4, [(1, 2), (2, 3), (3, 4), (4, 1)]), 1)
# test(Graph(4, [(1, 2), (2, 3), (1, 3)]), 0)

# RUN
g = read_graph()
print(g.is_bipartite())
