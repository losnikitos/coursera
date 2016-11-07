# python3

# http://stackoverflow.com/questions/2116662/help-me-understand-inorder-traversal-without-using-recursion

import sys


class Node:
	def __init__(self, key, left = None, right = None):
		self.key = key
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.key)


class Tree:
	def __init__(self, _nodes):
		nodes = [Node(*n) for n in _nodes]
		for node in nodes:
			node.left = nodes[node.left] if node.left != -1 else None
			node.right = nodes[node.right] if node.right != -1 else None
			# print('Node', node.key, 'left', node.left.key if node.left else '-', 'right', node.right.key if node.right else '-')
		self.nodes = nodes
		self.root = nodes[0]


	def in_order2(self):
		stck = []
		rslt = []
		node = self.root
		while node:
			stck.append(node)
			node = node.left

		while len(stck):
			node = stck.pop()
			rslt.append(node)
			node = node.right

			while node:
				stck.append(node)
				node = node.left

		return rslt

	def pre_order(self):
		stck = []
		node = self.root
		rslt = []
		while len(stck) or node:
			if node:
				stck.append(node)
				rslt.append(node)
				node = node.left
			else:
				node = stck.pop()
				node = node.right

		return rslt

	def post_order(self):
		node = self.root
		stck = [node]
		rslt = []
		while len(stck):
			next = stck[-1]
			finished_subtrees = next.right == node or next.left == node
			is_leaf = not (next.left or next.right)
			if finished_subtrees or is_leaf:
				stck.pop()
				rslt.append(next)
				node = next
			else:
				if next.right:
					stck.append(next.right)
				if next.left:
					stck.append(next.left)

		return rslt

	def in_order(self):
		stck = []
		node = self.root
		rslt = []
		while len(stck) or node != None:
			if node:
				# если node != None, идем вглубь
				stck.append(node)
				# print('Go left to', node.left)
				node = node.left
			else:
				# если node == None, идем наверх
				node = stck.pop()
				# print('Return', node)
				rslt.append(node)
				# print('Go right', node.right)
				node = node.right

		return rslt


# TEST

# def test(nodes, expected_in, expected_pre, expected_post):
# 	tree = Tree(nodes)
# 	res_in = [node.key for node in tree.in_order2()]
# 	res_pre = [node.key for node in tree.pre_order()]
# 	res_post = [node.key for node in tree.post_order()]
# 	print('ok' if res_in == expected_in else 'wrong in: expected %s instead of %s' % (expected_in, res_in))
# 	print('ok' if res_pre == expected_pre else 'wrong pre: expected %s instead of %s' % (expected_pre, res_pre))
# 	print('ok' if res_post == expected_post else 'wrong post: expected %s instead of %s' % (expected_post, res_post))

# nodes1 = [(4,1,2), (2,3,4), (5,-1,-1), (1,-1,-1), (3,-1,-1)]
# test(nodes1, [1,2,3,4,5], [4,2,1,3,5], [1,3,2,5,4])

# nodes2 = [(0,7,2),(10,-1,-1),(20,-1,6),(30,8,9),(40,3,-1),(50,-1,-1),(60,1,-1),(70,5,4),(80,-1,-1),(90,-1,-1)]
# test(nodes2, [50,70,80,30,90,40,0,20,10,60],[0,70,50,40,30,80,90,20,60,10],[50,80,90,30,40,70,10,60,20,0])

#         4
#        / \
#       2   5
#      / \
#     1   3 

# RUN

n = int(sys.stdin.readline())
nodes = [tuple(map(int, sys.stdin.readline().split())) for _ in range(0, n)]
tree = Tree(nodes)

print(' '.join(map(str, tree.in_order())))
print(' '.join(map(str, tree.pre_order())))
print(' '.join(map(str, tree.post_order())))