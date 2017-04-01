# python 3
def build_trie(words):
    trie = root = {'next': {}}
    for word in words:
        node = root
        for letter in word:
            if letter not in node['next']:
                node['next'][letter] = {'next': {}}
            node = node['next'][letter]
    return trie


def has_match(start, text, trie):
    node = trie
    # print(text[start:])
    for i in range(start, len(text)):
        letter = text[i]
        if letter not in node['next']:
            return False
        node = node['next'][letter]
        if len(node['next']) == 0:
            return True
        else:
            continue


def pattern_matches(text, trie):
    return [start for start in range(len(text)) if has_match(start, text, trie)]


text = input()
n = int(input())
patterns = [input() for _ in range(n)]

# patterns = ["ATCG", "GGGT"]
# text = "AATCGGGTTCAATCGGGGT"

trie = build_trie(patterns)
print(' '.join([str(i) for i in pattern_matches(text, trie)]))
