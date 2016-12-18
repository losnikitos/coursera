# python 3

from math import sqrt

inf = float('inf')


def read_graph():
    n_vertices = int(input())
    coordinates = [tuple(map(int, input().split())) for _ in range(n_vertices)]
    return Graph(coordinates)


class Graph:
    def __init__(self, coordinates):
        self.vertices = range(len(coordinates))
        self.edges = []
        for a in self.vertices:
            for b in self.vertices:
                if a != b:
                    x1, y1 = coordinates[a]
                    x2, y2 = coordinates[b]
                    edge = (sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), a, b)
                    self.edges.append(edge)

    def connect(self, n_segments):
        self.edges = sorted(self.edges)
        clusters = [i for i in self.vertices]
        n_clusters = len(self.vertices)

        def merge(a, b):
            c1 = clusters[a]
            c2 = clusters[b]
            for v in self.vertices:
                if clusters[v] == c1:
                    clusters[v] = c2

        for edge in self.edges:
            length, fr, to = edge
            # print('Check %s->%s len %s' % (fr, to, length))

            if n_clusters == n_segments and clusters[fr] != clusters[to]:
                return length

            if clusters[fr] != clusters[to]:
                # print('Merge clusters %s and %s' % (fr, to))
                merge(fr, to)
                # print(clusters)
                n_clusters -= 1

        return -1


# TEST
def test(g, n_segments, answer):
    res = g.connect(n_segments)
    print('ok' if res == answer else 'wrong: expected %s instead of %s' % (answer, res))

#
# test(Graph([(7, 6), (4, 3), (5, 1), (1, 7), (2, 7), (5, 7), (3, 3), (7, 8), (2, 8), (4, 4), (6, 7), (2, 6)]), 3, 2.828427124746)
# test(Graph([(3, 1), (1, 2), (4, 6), (9, 8), (9, 9), (8, 9), (3, 11), (4, 12)]), 4, 5)

# RUN
g = read_graph()
n_segments = int(input())
print(g.connect(n_segments))
