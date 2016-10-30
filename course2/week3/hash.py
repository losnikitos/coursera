# python3

import sys

p = 1000000007
x = 263


class Hash:
    def __init__(self, m):
        self.m = m
        self.table = [[] for _ in range(m)]

    def hash(self, str):
        hash = 0
        for i, char in enumerate(str):
            hash += ord(char) * (x ** i)
            # print(ord(char), '*', x, '^', i, 'mod', p)
            # print('+=', ord(char) * (x ** i) % p)

        # print('all mod', self.m)

        # print('hash of', str, 'is', (hash % p) % self.m)
        return (hash % p) % self.m

    def add(self, item):
        hash = self.hash(item)
        list = self.table[hash]
        if item not in list:
            list.append(item)

            # print('added', item, 'at', hash)
            # print(self.table)

    def delete(self, item):
        hash = self.hash(item)
        list = self.table[hash]

        if item in list:
            list.remove(item)

    def find(self, item):
        hash = self.hash(item)
        list = self.table[hash]
        return 'yes' if item in list else 'no'

    def check(self, hash):
        list = self.table[int(hash)]
        return ' '.join(reversed(list))

    def process(self, input):
        cmd, arg = input
        if cmd == 'add':
            return self.add(arg)
        if cmd == 'del':
            return self.delete(arg)
        if cmd == 'find':
            return self.find(arg)
        if cmd == 'check':
            return self.check(arg)


# TEST
# def test(m, operations, expected):
#     phonebook = Hash(m)
#     ops = [op.split() for op in operations]
#     output = [res for res in map(phonebook.process, ops) if res is not None]
#     if output == expected:
#         print('ok')
#     else:
#         print('wrong, expected %s instead of %s' % (expected, output))
#
#
# test(5, ['add world',
#          'add HellO',
#          'check 4',
#          'find World',
#          'find world',
#          'del world',
#          'check 4',
#          'del HellO',
#          'add luck',
#          'add GooD',
#          'check 2',
#          'del good'], [
#          'HellO world',
#          'no',
#          'yes',
#          'HellO',
#          'GooD luck'])
#
# test(4, [
#     'add test',
#     'add test',
#     'find test',
#     'del test',
#     'find test',
#     'find Test',
#     'add Test',
#     'find Test'
# ], [
#          'yes',
#          'no',
#          'no',
#          'yes'
#      ])
#
# test(3, [
#     'check 0',
#     'find help',
#     'add help',
#     'add del',
#     'add add',
#     'find add',
#     'find del',
#     'del del',
#     'find del',
#     'check 0',
#     'check 1',
#     'check 2'
# ], ['', 'no', 'yes', 'yes', 'no', '', 'add help', ''])

# RUN

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
operations = [sys.stdin.readline().strip() for _ in range(n)]
operations = [s.split() for s in operations]
hash = Hash(m)
[print(res) for res in map(hash.process, operations) if res is not None]
