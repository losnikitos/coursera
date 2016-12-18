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
        self.coordinates = coordinates

    def connect(self):
        costs = [inf for v in self.vertices]
        costs[0] = 0
        known = set()
        total_cost = 0

        while len(known) < len(self.vertices):
            cost = inf
            vertex = None

            # find vertex with min cost
            for v, c in enumerate(costs):
                if c < cost and v not in known:
                    cost = c
                    vertex = v

            known.add(vertex)
            total_cost += cost

            # update cost with distances from recently added vertex
            for v, c in enumerate(costs):
                if v not in known:
                    x1, y1 = self.coordinates[vertex]
                    x2, y2 = self.coordinates[v]
                    costs[v] = min(costs[v], sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

        return total_cost


# TEST
def test(g, answer):
    res = g.connect()
    print('ok' if res == answer else 'wrong: expected %s instead of %s' % (answer, res))


# test(Graph([(0, 0), (0, 1), (1, 0), (1, 1)]), 3)
# test(Graph([(0, 0), (0, 2), (1, 1), (3, 0), (3, 2)]), 7.064495102)

# RUN
g = read_graph()
print(g.connect())
