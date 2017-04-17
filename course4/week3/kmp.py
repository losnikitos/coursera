# python3

def prefix_function(string):
    values = [0]
    border = 0
    for i in range(1, len(string)):
        while border > 0 and string[i] != string[border]:
            border = values[border-1]
        border = border + 1 if string[i] == string[border] else 0
        values.append(border)
    return values

pattern = input()
text = input()

# pattern = 'ATAT'
# text = 'GATATATGCATATACTT'

# print(pattern + '$' + text)
prefix_function_values = prefix_function(pattern + '$' + text)
pattern_length = len(pattern)
# print(prefix_function_values)
res = [str(i - 2 * pattern_length) for (i, prefix_length) in enumerate(prefix_function_values) if prefix_length == pattern_length]
print(' '.join(res))
