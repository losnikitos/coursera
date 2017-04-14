# python 3


# def permutations(s):
#     return [s[i:len(s)] + s[0:i] for i in range(len(s))]
#
#
# def bwt(s):
#     return [line[-1] for line in sorted(permutations(s))]
#
#
# print(''.join(bwt(input())))
#
#

s = input()
permutations = [s[i:len(s)] + s[0:i] for i in range(len(s))]
last_col = [line[-1] for line in sorted(permutations)]
print(''.join(last_col))
