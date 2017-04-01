# python 3

def build_trie(words):
    trie = root = {'next': {}, 'end': False}
    for word in words:
        node = root
        for letter in word:
            if letter not in node['next']:
                node['next'][letter] = {'next': {}, 'end': False}
            node = node['next'][letter]
        node['end'] = True
    return trie


def has_match(start, text, trie):
    node = trie
    # print(text[start:])
    for i in range(start, len(text)):
        letter = text[i]
        if letter not in node['next']:
            return False
        node = node['next'][letter]
        if node['end']:
            return True
        else:
            continue


def pattern_matches(text, trie):
    return [start for start in range(len(text)) if has_match(start, text, trie)]


text = input()
n = int(input())
patterns = [input() for _ in range(n)]

# text = "AATCGGGTTCAATCGGGGT"
# patterns = ["ATCG", "GGGT"]

trie = build_trie(patterns)
print(' '.join([str(i) for i in pattern_matches(text, trie)]))
