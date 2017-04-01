# python3

def build_trie(words):
    index = 0
    trie = root = {'next': {}, 'index': index}
    for word in words:
        node = root
        for letter in word:
            if letter not in node['next']:
                index += 1
                node['next'][letter] = {'next': {}, 'index': index}
            node = node['next'][letter]
    return trie


def print_trie(trie):
    node = trie
    for letter in node['next']:
        next_node = node['next'][letter]
        print('%d->%d:%s' % (node['index'], next_node['index'], letter))
        print_trie(next_node)


# patterns = ['AT', 'AG', 'AC']
# patterns = ['ATA']
# patterns = ['ATAGA', 'ATC', 'GAT']

# trie = build_trie(patterns)
# print_trie(trie)

# run

n = int(input())
patterns = [input() for _ in range(n)]
trie = build_trie(patterns)
print_trie(trie)
