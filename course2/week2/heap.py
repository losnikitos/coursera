# python2

import sys, math


def heap(items):
    swaps = []

    def swap(i, j):
        swaps.append((i, j))
        items[i], items[j] = items[j], items[i]

    def siftDown(i):
        left = i * 2 + 1
        right = i * 2 + 2
        hasLeft = i * 2 + 1 < len(items)
        hasRight = i * 2 + 2 < len(items)
        min = i

        if hasLeft:
            if items[left] < items[min]:
                min = left

        if hasRight:
            if items[right] < items[min]:
                min = right

        if min != i:
            swap(i, min)
            siftDown(min)

    h = int(math.log(len(items), 2))
    end = 2 ** h - 2

    for i in range(end, -1, -1):
        siftDown(i)

    return swaps


# def test(items, resultSwaps):
#     result = heap(items)
#     if result == resultSwaps:
#         print('ok')
#     else:
#         print 'wrong: ', result, 'instead of', resultSwaps
#
#
# test([5, 4, 3, 2, 1], [(1, 4), (0, 1), (1, 3)])
# test([1, 2, 3, 4, 5], [])

elementsCount = sys.stdin.readline()
elements = [int(item) for item in sys.stdin.readline().split()]

swaps = heap(elements)

print(len(swaps))
for swap in swaps:
    print swap[0], swap[1]
