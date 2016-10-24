# python3

import sys


class Table:
    def __init__(self, length):
        self.length = length
        self.link = None

    def real(self):
        if not self.link:
            return self

        real = self.link.real()
        self.link = real
        return real

    def mergeTo(self, dest):
        src = self.real()
        dest = dest.real()
        if src is dest:
            return 0

        dest.length += src.length
        src.length = 0
        src.link = dest
        return dest.length


def merge(tables, merges):
    tables = [Table(t) for t in tables]
    maxLengths = []
    maxLength = max(table.length for table in tables)
    for merge in merges:
        dest, src = [int(i) - 1 for i in merge]  # 0-based indices
        newLen = tables[src].mergeTo(tables[dest])
        maxLength = max(maxLength, newLen)
        maxLengths.append(maxLength)

    return maxLengths


# TEST
def test(tables, merges, expected):
    result = merge(tables, merges)
    print('ok' if result == expected else 'wrong: expected %s instead of %s' % (expected, result))


# test([1, 1, 1, 1, 1], [(3, 5), (2, 4), (1, 4), (5, 4), (5, 3)], [2, 2, 3, 5, 5])
# test([10, 0, 5, 0, 3, 3], [(6, 6), (6, 5), (5, 4), (4, 3)], [10, 10, 10, 11])
# test([100000, 100000, 100000, 100000, 100000], [(1, 2), (2, 3), (4, 3), (5, 1)], [10, 15, 15])
test([0, 11, 10], [(1, 2), (2, 3)], [11, 12])

# RUN

ntables, nmerges = [int(a) for a in sys.stdin.readline().split()]
tables = [int(a) for a in sys.stdin.readline().split()]
merges = [tuple(sys.stdin.readline().split()) for _ in range(nmerges)]

# print(tables, merges)
result = merge(tables, merges)

for l in result:
    print(str(l))
