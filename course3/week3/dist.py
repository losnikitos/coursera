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

    def distance(self, fr, to):
        dist = [-1 for v in self.vertices]
        dist[fr] = 0
        queue = [fr]
        while len(queue):
            vertex = queue.pop(0)
            if vertex == to:
                return dist[to]
            for neighbor in self.edges[vertex]:
                if dist[neighbor] == -1:
                    queue.append(neighbor)
                    dist[neighbor] = dist[vertex] + 1
        return -1

    def __str__(self):
        return '\n'.join(['%s: %s' % (v, self.edges[v]) for v in self.vertices])


# TEST
# def test(g, fr, to, answer):
#     res = g.distance(fr - 1, to - 1)
#     print('ok' if res == answer else 'wrong: expected %s instead of %s' % (answer, res))


# test(Graph(4, [(1, 2), (4, 1), (2, 3), (3, 1)]), 2, 4, 2)
# test(Graph(5, [(5, 2), (1, 3), (3, 4), (1, 4)]), 3, 5, -1)

# RUN
g = read_graph()
fr, to = map(int, input().split())
print(g.distance(fr - 1, to - 1))
