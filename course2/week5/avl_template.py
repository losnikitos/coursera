# python3

from sys import stdin

MODULO = 1000000001


# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)


class SplayTree:
    def __init__(self, root = None):
        self.last_sum_result = 0
        self.root = root

    def update(self, v):
        if v is None:
            return
        v.sum = v.key + (v.left.sum if v.left is not None else 0) + (v.right.sum if v.right is not None else 0)
        if v.left is not None:
            v.left.parent = v
        if v.right is not None:
            v.right.parent = v

    def smallRotation(self, v):
        parent = v.parent
        if parent is None:
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
        self.update(parent)
        self.update(v)
        v.parent = grandparent
        if grandparent is not None:
            if grandparent.left == parent:
                grandparent.left = v
            else:
                grandparent.right = v

    def bigRotation(self, v):
        if v.parent.left == v and v.parent.parent.left == v.parent:
            # Zig-zig
            self.smallRotation(v.parent)
            self.smallRotation(v)
        elif v.parent.right == v and v.parent.parent.right == v.parent:
            # Zig-zig
            self.smallRotation(v.parent)
            self.smallRotation(v)
        else:
            # Zig-zag
            self.smallRotation(v)
            self.smallRotation(v)

    # Makes splay of the given vertex and makes
    # it the new root.
    def splay(self, v):
        if v is None:
            return None
        while v.parent is not None:
            if v.parent.parent is None:
                self.smallRotation(v)
                break
            self.bigRotation(v)
        return v

    # Searches for the given key in the tree with the given root
    # and calls splay for the deepest visited node after that.
    # Returns pair of the result and the new root.
    # If found, result is a pointer to the node with the given key.
    # Otherwise, result is a pointer to the node with the smallest
    # bigger key (next value in the order).
    # If the key is bigger than all keys in the tree,
    # then result is None.
    def find(self, key):
        v = self.root
        last = self.root
        next = None
        while v is not None:
            if v.key >= key and (next is None or v.key < next.key):
                next = v
            last = v
            if v.key == key:
                break
            if v.key < key:
                v = v.right
            else:
                v = v.left
        self.root = self.splay(last)
        return next

    def split(self, key):
        result = self.find(key)
        if result is None:
            return (self, None)
        right = self.splay(result)
        left = right.left
        right.left = None
        if left is not None:
            left.parent = None
        self.update(left)
        self.update(right)
        return (SplayTree(left), SplayTree(right))

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        leftmost = right.root.left
        while leftmost is not None:
            leftmost = leftmost.left

        right.splay(leftmost)
        right.root.left = left.root
        right.update(right.root)
        return right

    # Code that uses splay tree to solve the problem

    def insert(self, x):
        (left, right) = self.split(x)
        new_vertex = None
        if right is None or right.root.key != x:
            new_vertex = Vertex(x, x, None, None, None)
        self.root = self.merge(self.merge(left, SplayTree(new_vertex)), right)

    def next(self, n):
        if not n.right:
            current = n.parent
            while current.key < n.key and current is not None:
                current = current.parent
            return current
        else:
            current = n.right
            while current.left:
                current = current.left
            return current

    def delete(self, node):
        parent = node.parent
        if node is parent.left:
            parent.left = None
        if node is parent.right:
            parent.right = None
        raise NameError('Node is not son of his own parents')

    def erase(self, x):
        node = self.find(self.root, x)
        if node.key != x:
            return None

        next = self.next(node)
        self.root = self.splay(next)
        self.root = self.splay(node)
        self.delete(node)

    def search(self, x):
        current = self.root

        while current:
            if x == current.key:
                self.splay(current)
                return current  # should be self.root
            elif x > current.key:
                current = current.right
            else:
                current = current.left

        return False

    def sum(self, fr, to):
        (left, middle) = self.split(fr)
        (middle, right) = self.split(middle, to + 1)
        ans = 0
        # Complete the implementation of sum

        return ans

    def apply_operation(self, line):
        line = line.split()
        if line[0] == '+':
            x = int(line[1])
            self.insert((x + self.last_sum_result) % MODULO)
        elif line[0] == '-':
            x = int(line[1])
            self.erase((x + self.last_sum_result) % MODULO)
        elif line[0] == '?':
            x = int(line[1])
            return 'Found' if self.search((x + self.last_sum_result) % MODULO) else 'Not found'
        elif line[0] == 's':
            l = int(line[1])
            r = int(line[2])
            res = self.sum((l + self.last_sum_result) % MODULO, (r + self.last_sum_result) % MODULO)
            self.last_sum_result = res % MODULO
            return res

    def apply_operations(self, lines):
        results = [self.apply_operation(line) for line in lines]
        return [res for res in results if res is not None]


# TEST


def test(operations, expected):
    tree = SplayTree()
    result = list(tree.apply_operations(operations))
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

test(set1, res1)
test(set2, res2)
test(set3, res3)

# RUN

n = int(stdin.readline())
lines = [stdin.readline() for _ in range(n)]
tree = SplayTree()
result = tree.apply_operations(lines)
for line in result:
    print(line)
