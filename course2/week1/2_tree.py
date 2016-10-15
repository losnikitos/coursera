# python2

import sys


def buildTree(items):
    tree = {}
    for index, item in enumerate(items):
        if item not in tree:
            tree[item] = {'children': []}
        tree[item]['children'].append(str(index))
    return tree


def height(tree, nodeIndex=-1):
    if str(nodeIndex) not in tree:
        return 0

    node = tree[nodeIndex]
    heights = [height(tree, child) for child in node['children']]
    return max(heights) + 1


# test

# def test(input, expected):
#     nodes = input.split()
#     tree = buildTree(nodes)
#     res = height(tree)
#     print 'ok' if res == expected else 'wrong: %s insted of %s' % (res, expected)
#
#
# test('4 -1 4 1 1', 3)
# test('-1 0 4 0 3', 4)
# test('-1', 1)
# test('-1 -1 -1', 1)
# test('9 7 5 5 2 9 9 9 2 -1', 4)

#
n = sys.stdin.readline()
nodes = sys.stdin.readline().split()
tree = buildTree(nodes)
print(height(tree))
