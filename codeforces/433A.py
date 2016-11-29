# python3
# http://codeforces.com/problemset/problem/433/A

input()
weights = input().split()
a = weights.count('100')
b = weights.count('200')
print('YES' if (b % 2 == 0 and a % 2 == 0) or (b % 2 == 1 and a > 1 and a % 2 == 0) else 'NO')