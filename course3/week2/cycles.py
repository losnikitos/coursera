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

    # def explore(self, vertex, visited=[], preorder=None, postorder=None):
    #     self.deep += 1
    #     if vertex in visited:
    #         self.deep -= 1
    #         return
    #
    #     visited.append(vertex)
    #
    #     print('  ' * self.deep, 'at', vertex)
    #
    #     for neighbor in self.edges[vertex]:
    #         print('  '*self.deep, 'neighbor', neighbor)
    #         preorder(neighbor, visited) if preorder else 0
    #         self.explore(neighbor, visited, preorder, postorder)
    #         postorder(neighbor, visited) if postorder else 0
    #
    #     self.deep -= 1
    #
    # def dfs(self, preorder=None, postorder=None):
    #     print(self)
    #     visited = []
    #     for node in range(self.num_vertices):
    #         if node not in visited:
    #             print('START', node)
    #             self.explore(node, visited, preorder, postorder)
    #
    # def has_loops(self):
    #     looped = []
    #
    #     def pre(node, visited):
    #         print('  '*self.deep, 'visited %s, going to %s' % (visited, node))
    #         if node in visited:
    #             print('CYCLE!')
    #             looped.append(node)
    #
    #     self.dfs(pre)
    #     return len(looped) > 0

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
