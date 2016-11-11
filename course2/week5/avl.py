# python3

from sys import stdin

MODULO = 1000000001
last_sum_result = 0


# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)


def update(v):
    if v == None:
        return
    v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v


def smallRotation(v):
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    else:
        # Zig-zag
        smallRotation(v);
        smallRotation(v);


# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
    v = root
    last = root
    next = None
    while v != None:
        if v.key >= key and (next == None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return (next, root)


def split(root, key):
    (result, root) = find(root, key)
    if result == None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)


def merge(left, right):
    if left == None:
        return right
    if right == None:
        return left
    while right.left != None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


# Code that uses splay tree to solve the problem

root = None


def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right == None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)


def erase(key):
    global root

    # print('erase', key)

    node, _ = find(root, key)
    if node is None or node.key != key:
        return

    next_node = next(node)

    if next_node is None:
        # print('no next node')
        splay(node)
        root = node.left
        if root:
            root.parent = None
        return

    root = splay(next_node)
    root = splay(node)
    # node is root, next_node is on his right
    next_node.left = node.left
    if node.left:
        node.left.parent = next_node

    root = next_node
    # TODO: update?


def search(x):
    global root, last_sum_result
    (found, _) = find(root, x)

    if not found or found.key != x:
        return None
    else:
        return found


def sum(fr, to):
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)

    update(middle)
    return middle.sum

def next(n):
    if not n:
        return None

    if not n.right:
        current = n.parent
        if current is None:
            return None
        while current.key < n.key and current is not None:
            current = current.parent
        return current
    else:
        current = n.right
        while current.left:
            current = current.left
        return current


def apply_operation(line):
    global last_sum_result

    # print('operation', line)
    line = line.split()
    if line[0] == '+':
        x = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        return 'Found' if search((x + last_sum_result) % MODULO) else 'Not found'
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        last_sum_result = res % MODULO
        return res


def apply_operations(lines):
    results = [apply_operation(line) for line in lines]
    return [str(res) for res in results if res is not None]


# TEST

def test(operations, expected):
    global last_sum_result, root
    last_sum_result = 0
    root = None
    result = list(apply_operations(operations))
    print('ok' if result == expected else 'wrong: expected %s instead of %s' % (expected, result))


set1 = ['? 1',
        '+ 1',
        '? 1',
        '+ 2',
        's 1 2',
        '+ 1000000000',
        '? 1000000000',
        '- 1000000000',
        '? 1000000000',
        's 999999999 1000000000',
        '- 2',
        '? 2',
        '- 0',
        '+ 9',
        's 0 9']

res1 = ['Not found',
        'Found',
        '3',
        'Found',
        'Not found',
        '1',
        'Not found',
        '10']

set2 = ['? 0', '+ 0', '? 0', '- 0', '? 0']
res2 = ['Not found', 'Found', 'Not found']

set3 = ['+ 491572259', '? 491572259', '? 899375874', 's 310971296 877523306', '+ 352411209']
res3 = ['Found', 'Not found', '491572259']

# test(set1, res1)
# test(set2, res2)
# test(set3, res3)

# RUN

n = int(stdin.readline())
lines = [stdin.readline() for _ in range(n)]
result = apply_operations(lines)
for line in result:
    print(line)
