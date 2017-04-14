# python 3

# text = input()
text = "abac$"

# вначале
trie = {}

# add_word('abac$')
trie = { next: [ { range: range(0, 5), start: 0 }] }

# add_word('bac$')
trie = { start: None, range: None, next: [
    { range: range(0, 5), start: 0, next: set() },
    { range: range(1, 4), start: 1, next: set() }
] }

# add_word('ac$')
trie = { start: None, range: None, next: [
    { start: None, range: range(0, 1), next: [
        { start: 0, range: range(1, 4), next: set() },
        { start: 2, range: range(2, 4), next: set() }
    ] },
    { range: range(1, 5), start: 1, next: set() }
] }

# add_word('c$')
trie = { start: None, range: None, next: [
    { start: None, range: range(0, 1), next: [
        { start: 0, range: range(1, 4), next: set() },
        { start: 2, range: range(2, 4), next: set() }
    ] },
    { range: range(1, 4), start: 1, next: set() },
    { range: range(3, 4), start: 3, next: set() }
] }


def read(word):
    return text[word.start:word.start + len(word)]


def add_word(node, word):

    if len(word) > len(node['word'])


# def add_word(text, node, word):
#     for i in range(node['start'], node['start'] + node['length']):
#
# def build_suffix_trie(text):
#     root = {'next': set(), 'start': None, 'length': None, 'word_start': None}
#     for start in range(len(text)):
#         # слово от start до len(text)
#         length = len(text) - start
#         new_node = {'start': start, 'length': length, 'word_start': start}
#         node = root
#         children = node['next']
#         for child in children:
#             if text[child['start']] == text[child[start]] # идем в эту ветку
#                 recursion(child, new_node)
#             word_range = range(child['start'], child['start'] + child['length'])
#             for i in word_range:
#
#         # else...children.add(new_node)
#
#         for letter in word:
#             if letter not in node['next']:
#                 node['next'][letter] = {'next': {}, 'start': None}
#             node = node['next'][letter]
#         node['start'] = start
#     return trie


def print_trie(trie):
    print(trie)
