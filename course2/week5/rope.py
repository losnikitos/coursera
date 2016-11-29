# python3

from sys import stdin

DEBUG = False

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, char, left=None, right=None, parent=None):
        (self.key, self.char, self.left, self.right, self.parent) = (key, char, left, right, parent)

    def __repr__(self):
        return '%s(%s)' % (self.char, self.key)


def shift(node, offset):
    if node is None:
        return

    queue = [node]
    while len(queue):
        node = queue.pop()
        if node:
            node.key += offset
            queue.append(node.left)
            queue.append(node.right)


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
        smallRotation(v)
        smallRotation(v)


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


def update(v):
    if v is None:
        return
    if v.left is not None:
        v.left.parent = v
    if v.right is not None:
        v.right.parent = v


# Code that uses splay tree to solve the problem

root = None


def insert(key, char):
    global root
    DEBUG and print('# insert', char, 'at', key)
    new_vertex = Vertex(key, char, None, None, None)
    root = merge(root, new_vertex)


def last(node):
    while node and node.right:
        node = node.right
    return node


def first(node):
    while node and node.left is not None:
        node = node.left
    return node


def move(start, end, put_after):
    global root
    DEBUG and print('# move from', start, 'to', end, 'after', put_after)

    left, middle = split(root, start)
    middle, right = split(middle, end + 1)

    DEBUG and print('# split into "%s"+"%s"+"%s"' % (printString(left), printString(middle), printString(right)))

    # вырезанный кусок
    length = end - start + 1

    # соединяем левую и правую части
    shift(right, -length)
    left = merge(left, right)

    DEBUG and print('# merged without "%s" : "%s"' % (printString(middle), printString(left)))

    # место под вырезанный кусок
    left, right = split(left, put_after)

    DEBUG and print('# split before insert: "%s" + "%s"' % (printString(left), printString(right)))

    # правую часть двигаем вправо, особождаем место
    shift(right, +length)

    # вырезанную часть двигаем сначала к 0, потом до места вставки
    shift(middle, -start + put_after)

    # склеиваем
    root = merge(merge(left, middle), right)
    DEBUG and print('# merged to', printString(root))


def apply_operation(line):
    global root
    start, end, put_after = [int(n) for n in line.split()]
    move(start, end, put_after)


def apply_operations(lines):
    for line in lines:
        apply_operation(line)


def make_tree(string):
    global root
    root = None
    for index, char in enumerate(string):
        insert(index, char)
    return root


def next(node):
    if not node:
        return None

    if not node.right:
        current = node.parent
        if current is None:
            return None
        while current is not None and current.key < node.key:
            current = current.parent
        return current
    else:
        current = node.right
        while current.left:
            current = current.left
        return current


def printTree(node, depth=0):
    output = ""
    prefix = ("   " * depth if depth else '*')

    if not node:
        if depth == 0:
            print('*')
            return
        else:
            return prefix + '-\n'

    if depth == 0:
        print('')

    output += printTree(node.right, depth + 1)
    output += prefix + str(node.key) + '(' + str(node.char) + ')^' + (
        str(node.parent.key) if node.parent else '*') + '\n'
    output += printTree(node.left, depth + 1)

    if depth == 0:
        print(output[:-1])
        print('')

    return output


def printString(node):
    current = first(node)
    res = []
    while current:
        res.append(current.char)
        current = next(current)
    return ''.join(res)


def traverse():
    current = first(root)
    while current:
        print('!', current.char)
        current = next(current)


def interactive():
    global root
    while True:
        apply_operation(stdin.readline())
        printTree(root)


def test(string, operations, expected):
    global root
    root = None
    make_tree(string)
    apply_operations(operations)
    result = printString(root)
    print('ok' if result == expected else 'wrong: expected %s instead of %s' % (expected, result))


def run():
    global root
    s = stdin.readline().strip()
    n = int(stdin.readline())
    lines = [stdin.readline().strip() for _ in range(n)]

    make_tree(s)
    apply_operations(lines)
    res = printString(root)

    print(res)


# test('hlelowrold', ['1 1 2', '6 6 7'], 'helloworld')
# test('abcdef', ['2 4 3'], 'abfcde')
# test('abcdef', ['0 1 1', '4 5 0'], 'efcabd')

l = 300 * 1000
s = 'abc' * int(l / 3)
moveright = '0 ' + str(l - 2) + ' 1'
moveleft = '1 ' + str(l - 1) + ' 0'
operations = [moveleft, moveright] * 10
test(s, operations, s)

# interactive()

run()
