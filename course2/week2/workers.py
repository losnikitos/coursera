# python2

import sys, math


class Heap:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def pop(self):
        last = len(self.items) - 1
        root = 0
        self.swap(last, root)
        min = self.items.pop()  # ex root is the min element
        self.siftDown(root)
        return min

    def siftUp(self, i):
        if i == 0:
            return

        parent = (i - 1) / 2
        this = i
        if self.items[this] < self.items[parent]:
            self.swap(this, parent)
            self.siftUp(parent)

    def siftDown(self, i):
        left = i * 2 + 1
        right = i * 2 + 2
        hasLeft = i * 2 + 1 < len(self.items)
        hasRight = i * 2 + 2 < len(self.items)
        min = i

        if hasLeft:
            if self.items[left] < self.items[min]:
                min = left

        if hasRight:
            if self.items[right] < self.items[min]:
                min = right

        if min != i:
            self.swap(i, min)
            self.siftDown(min)

    def push(self, item):
        self.items.append(item)
        last = len(self.items) - 1
        self.siftUp(last)


def process(workerCount, tasks):
    heap = Heap()
    starts = []

    for worker in xrange(workerCount):
        heap.push((0, worker))

    for taskIndex, task in enumerate(tasks):
        time, worker = heap.pop()
        finishTime = time + task
        # print 'time', time, 'worker', worker, 'finished. Next task will finish at', finishTime
        starts.append((worker, time))
        heap.push((finishTime, worker))

    return starts


# TEST

# def test(workers, tasks, expectedStarts):
#     starts = process(workers, tasks)
#     if starts == expectedStarts:
#         print('ok')
#     else:
#         print 'wrong: ', starts, 'instead of', expectedStarts


# test(2, [1, 2, 3, 4, 5], [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)])
#
# test(4, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#      [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2), (0, 3), (1, 3),
#       (2, 3), (3, 3), (0, 4), (1, 4), (2, 4), (3, 4)])

# test(1, [5, 5, 10, 200], [(0, 0), (0, 5), (0, 10), (0, 20)])
# test(2, [5, 5, 10, 200], [(0, 0), (1, 0), (0, 5), (1, 5)])
# test(10, [5, 5, 10, 200], [(0, 0), (1, 0), (2, 0), (3, 0)])

# test(2, [100, 3, 3, 3, 3], [(0, 0), (1, 0), (1, 3), (1, 6), (1, 9)])

# RUN

workersCount, tasksCount = [int(item) for item in sys.stdin.readline().split()]
tasks = [int(item) for item in sys.stdin.readline().split()]

starts = process(workersCount, tasks)

for start in starts:
    print start[0], start[1]
