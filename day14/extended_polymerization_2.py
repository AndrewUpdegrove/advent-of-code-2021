import sys
import re

def find_pairs(letters):
    matches = re.finditer(r'(?=([A-Z]{2}))', letters)
    return [match.group(1) for match in matches]

seed = ''
rules = {}
with open(sys.argv[1], 'r') as in_file:
    seed = in_file.readline().rstrip()
    in_file.readline()
    for line in in_file:
        parts = line.rstrip().split(' -> ')
        rules[parts[0]] = parts[1]

arr_pairs = find_pairs(seed)
pairs = {}
for pair in arr_pairs:
    if not pairs.get(pair):
        pairs[pair] = 0
    pairs[pair] += 1

blank_pairs = { pair : 0 for pair in rules.keys() }

for i in range(40):
    new_pairs = blank_pairs.copy()
    for pair in pairs.keys():
        add_char = rules[pair]
        new_pairs[pair[0]+add_char] += pairs[pair]
        new_pairs[add_char+pair[1]] += pairs[pair]

    pairs = new_pairs

letter_counts = {}
for pair in pairs.keys():
    if not letter_counts.get(pair[0]):
        letter_counts[pair[0]] = pairs[pair]
    else:
        letter_counts[pair[0]] += pairs[pair]

letter_counts[seed[-1]] += 1

dict_list = [(k, v) for k, v in letter_counts.items()]
dict_list.sort(key=lambda x:x[1])
print(f'Part 2 solution: {dict_list[-1][1] - dict_list[0][1]}')

