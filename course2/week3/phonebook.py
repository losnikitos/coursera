# python3

import sys


class Phonebook:
    def __init__(self):
        self.hash = {}

    def add(self, number, name):
        self.hash[number] = name

    def delete(self, number):
        if number not in self.hash:
            return
        del self.hash[number]

    def find(self, number):
        return self.hash[number] if (number in self.hash) else 'not found'

    def process(self, input):
        if input[0] == 'add':
            return self.add(int(input[1]), input[2])
        if input[0] == 'del':
            return self.delete(int(input[1]))
        if input[0] == 'find':
            return self.find(int(input[1]))


# TEST
def test(operations, expected):
    phonebook = Phonebook()
    ops = [op.split() for op in operations]
    output = [res for res in map(phonebook.process, ops) if res]
    if output == expected:
        print('ok')
    else:
        print('wrong, expected %s instead of %s' % (expected, output))


# test(['add 911 police',
#       'add 76213 Mom',
#       'add 17239 Bob',
#       'find 76213',
#       'find 910',
#       'find 911',
#       'del 910',
#       'del 911',
#       'find 911',
#       'find 76213',
#       'add 76213 daddy',
#       'find 76213'], ['Mom',
#                       'not found',
#                       'police',
#                       'not found',
#                       'Mom',
#                       'daddy'])
#
# test(['find 3839442',
#       'add 123456 me',
#       'add 0 granny',
#       'find 0',
#       'find 123456',
#       'del 0',
#       'del 0',
#       'find 0'], ['not found',
#                   'granny',
#                   'me',
#                   'not found'])

# RUN

n = int(sys.stdin.readline())
operations = [sys.stdin.readline() for _ in range(n)]
operations = [s.split() for s in operations]
phonebook = Phonebook()
[print(res) for res in map(phonebook.process, operations) if res]
