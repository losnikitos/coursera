# python 3

inf = float("inf")


def read_graph():
    n_vertices, n_edges = map(int, input().split())
    edges = [map(int, input().split()) for _ in range(n_edges)]
    return Graph(n_vertices, edges)


class Graph:
    def __init__(self, n_vertices=0, edges=[]):
        self.vertices = set(range(n_vertices))
        self.weights = [0 for v in self.vertices]
        self.edges = [set() for v in self.vertices]
        for edge in edges:
            a, b, w = edge
            self.edges[a - 1].add((b - 1, w))

    def distance(self, fr, to):
        prev = []
        dist = []
        unknown = {}
        for v in self.vertices:
            prev.append(None)
            dist.append(inf if v != fr else 0)
            unknown[v] = inf if v != fr else 0

        while len(unknown):
            nearest = min(unknown, key=unknown.get)
            print('Unknown', unknown)
            del unknown[nearest]
            print('Nearest', nearest)

            for edge in self.edges[nearest]:
                neighbor, weight = edge
                print('Goto', neighbor)

                if dist[neighbor] > dist[nearest] + weight:
                    print('Relax %s-%s' % (nearest, neighbor))
                    dist[neighbor] = dist[nearest] + weight
                    prev[neighbor] = nearest
                    unknown[neighbor] = dist[neighbor]

        return dist[to]

    def __str__(self):
        return '\n'.join(['%s: %s' % (v, self.edges[v]) for v in self.vertices])


# TEST
def test(g, path, answer):
    fr, to = path
    res = g.distance(fr - 1, to - 1)
    print('ok' if res == answer else 'wrong: expected %s instead of %s' % (answer, res))


test(Graph(4, [(1, 2, 1), (4, 1, 2), (2, 3, 2), (1, 3, 5)]), (1, 3), 3)
# test(Graph(5, [(1, 2, 4), (1, 3, 2), (2, 3, 2), (3, 2, 1), (2, 4, 2),
#                (3, 5, 4), (5, 4, 1), (2, 5, 3), (3, 4, 4)]), (1, 5), 6)
# test(Graph(3, [(1, 2, 7), (1, 3, 5), (2, 3, 2)]), (3, 2), inf)

# RUN
g = read_graph()
fr, to = map(int, input().split())
dist = g.distance(fr - 1, to - 1)
print(-1 if dist == inf else dist)
