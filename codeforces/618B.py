n = int(input())
known = [0] * n

table = []
for i in range(n):
    table.append(list(map(int, input().split())))


def find(i):
    for i, line in enumerate(table):
        if known[i]:
            continue
        for item in line:
            if item > i + 1:
                continue
            return i


for i in range(n):
    line = table[i][i + 1:]
    m.append(max(line) if len(line) else n)

print(' '.join([str(x) for x in m]))
