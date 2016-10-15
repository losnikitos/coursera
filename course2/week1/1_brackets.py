# python2

import sys

stack = []
open = '([{'
close = {']': '[', '}': '{', ')': '('}


def check(string):
    for index, char in enumerate(string):
        if char in open:
            stack.append((char, index))
        elif char in close:
            if not stack:
                return index + 1
            match = stack.pop()
            if not close[char] == match[0]:
                return index + 1
    if stack:
        return stack.pop()[1] + 1
    else:
        return 'Success'


text = sys.stdin.readline()
print(check(text))

# def test(input, expected):
#     res = check(input)
#     print 'ok' if res == expected else 'wrong: %s insted of %s' % (res, expected)

# test('[]', 'Success')
# test('{}[]', 'Success')
# test('[{}]', 'Success')
# test('(())', 'Success')
# test('{aaaaa', 1)
# test('{[}', 3)
# test('foo(bar);', 'Success')
# test('foo(bar[i);', 10)
