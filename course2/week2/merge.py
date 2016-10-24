# python3

import sys


class Table:
    def __init__(self, length):
        self.length = length
        self.link = None

    # def real(self):
    #     if not self.link:
    #         return self
    #
    #     real = self.link.real()
    #     self.link = real
    #     return real


def mergeTables(dest, src):
    if src is dest:
        return

    if src.link:
        mergeTables(src.link, dest)
        dest.link = src.link  # todo: compress path
        return

    if dest.link:
        mergeTables(src, dest.link)
        # src.link = dest.link
        # src.length = 0
        return

    dest.length += src.length
    src.length = 0
    src.link = dest


def merge(tables, merges):
    tables = [Table(t) for t in tables]
    maxLengths = []
    for merge in merges:
        dest, src = [int(i) - 1 for i in merge]  # 0-based indices
        mergeTables(tables[dest], tables[src])
        maxLengths.append(max(table.length for table in tables))

    return maxLengths


# TEST
def test(tables, merges, expected):
    result = merge(tables, merges)
    print('ok' if result == expected else 'wrong: expected %s instead of %s' % (expected, result))


test([1, 1, 1, 1, 1], [(3, 5), (2, 4), (1, 4), (5, 4), (5, 3)], [2, 2, 3, 5, 5])
test([10, 0, 5, 0, 3, 3], [(6, 6), (6, 5), (5, 4), (4, 3)], [10, 10, 10, 11])

# RUN

ntables, nmerges = [int(a) for a in sys.stdin.readline().split()]
tables = [int(a) for a in sys.stdin.readline().split()]
merges = [tuple(sys.stdin.readline().split()) for _ in range(nmerges)]

# print(tables, merges)
result = merge(tables, merges)

for l in result:
    print(l)
