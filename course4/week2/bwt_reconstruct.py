#python3

bwt = input()
# bwt = 'AGGGAA$'


def build_index(s):
    known = {}
    res = []
    for c in s:
        if c not in known:
            known[c] = 0
        known[c] += 1
        res.append(c + str(known[c]))
    return res


last_row = build_index(bwt)
first_row = build_index(sorted(bwt))

next = {}
for i in range(len(bwt)):
    next[first_row[i]] = last_row[i]

res = []
sym = first_row[0]
for i in range(len(bwt)):
    res.append(sym[0])
    sym = next[sym]

print(''.join(reversed(res)))