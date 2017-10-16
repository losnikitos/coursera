# python3

# python3

alphabet = '$ACGT'


def sort_characters(s):
    order = [None for _ in s]
    count = {key: 0 for key in alphabet}
    for c in s:
        count[c] += 1
    i = 0
    for c in alphabet:
        count[c] += i
        i = count[c]
    for i, c in list(enumerate(s))[::-1]:
        count[c] -= 1
        order[count[c]] = i
    return order


def compute_char_classes(s, order):
    cls = [None for _ in s]
    cls[order[0]] = 0
    for i in range(1, len(s)):
        if s[order[i]] != s[order[i - 1]]:
            cls[order[i]] = cls[order[i - 1]] + 1
        else:
            cls[order[i]] = cls[order[i - 1]]
    return cls


def sort_doubled(s, l, order, cls):
    count = [0 for _ in s]
    new_order = [None for _ in s]
    for c in cls:
        count[c] += 1
    for j in range(1, len(s)):
        count[j] += count[j - 1]
    for i in range(len(s) - 1, -1, -1):  # len(s)-1 down to 0
        start = (order[i] - l + len(s)) % len(s)
        cl = cls[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order


def update_classes(new_order, cls, l):
    n = len(new_order)
    new_class = [None for _ in range(n)]
    new_class[new_order[0]] = 0
    for i in range(1, n):
        cur = new_order[i]
        prev = new_order[i - 1]
        mid = (cur + l) % n
        mid_prev = (prev + l) % n
        if cls[cur] != cls[prev] or cls[mid] != cls[mid_prev]:
            new_class[cur] = new_class[prev] + 1
        else:
            new_class[cur] = new_class[prev]
    return new_class


# s = input()
s = 'AACGATAGCGGTAGA$'

order = sort_characters(s)
# for idx in order:
#     print(s[idx])
cls = compute_char_classes(s, order)

l = 1
while l < len(s):
    order = sort_doubled(s, l, order, cls)
    # if l == 1:
    #     print(order)
    # print([(s+s)[i:i + 2] for i in order])
    cls = update_classes(order, cls, l)
    if l == 1:
        print(cls)
    l *= 2

# print(' '.join([str(s) for s in order]))
# 15 14 0 1 12 6 4 2 8 13 3 7 9 10 11 5
