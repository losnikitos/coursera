# python3

import sys
from random import randint


def polyHash(S, p, x):
    hash = 0
    for i in range(len(S) - 1, -1, -1):
        hash = (hash * x + ord(S[i])) % p
    # print('hash of', S, '=', hash)
    return hash


def precomputeHashes(text, patternLength, p, x):
    last = len(text) - patternLength  # start of last substring
    H = [0 for _ in range(0, last + 1)]
    S = text[-patternLength:]
    H[last] = polyHash(S, p, x)
    y = 1
    for i in range(1, patternLength + 1):
        y = (y * x) % p

    # print('H[last]=', H[last])
    for i in range(last - 1, -1, -1):
        # print('H[%d]=...' % i)
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + patternLength])) % p

    # substrings = [text[i:i + patternLength] for i in range(0, last + 1)]
    # print('Substrings', substrings)
    # print('Hashes  ', H)
    # print('Expected', [polyHash(S, p, x) for S in substrings])
    return H


def find(pattern, text):
    p = 1000000007
    x = 100  # randint(1, p - 1)
    result = []
    pHash = polyHash(pattern, p, x)
    H = precomputeHashes(text, len(pattern), p, x)
    for i in range(0, len(text) - len(pattern) + 1):
        if pHash != H[i]:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)

    return result


# TEST

# def test(substring, string, expected):
#     result = find(substring, string)
#     if result == expected:
#         print('ok')
#     else:
#         print('wrong, expected %s instead of %s' % (expected, result))
#
#
# test('aba', 'abacaba', [0, 4])
# test('Test', 'testTesttesT', [4])
# test('aaaaa', 'baaaaaaa', [1, 2, 3])
# RUN

substring = sys.stdin.readline().strip()
string = sys.stdin.readline().strip()
print(' '.join(str(x) for x in find(substring, string)))
