import sys
import re


def find_pairs(letters):
    matches = re.finditer(r'(?=([A-Z]{2}))', letters)
    return [match.group(1) for match in matches]

def generate_new_polymer(pairs, rules):
    res = ''
    for pair in pairs:
        res += (pair[0] + rules[pair])
    res += pairs[-1][1]
    return res

seed = ''
rules = {}
with open(sys.argv[1], 'r') as in_file:
    seed = in_file.readline().rstrip()
    in_file.readline()
    for line in in_file:
        parts = line.rstrip().split(' -> ')
        rules[parts[0]] = parts[1]

for i in range(10):
    pairs = find_pairs(seed)
    seed = generate_new_polymer(pairs, rules)
    poly_len = len(seed)
    count = {}
    for let in seed:
        if not count.get(let):
            count[let] = 0
        count[let] += 1
    dict_list = [(k, v/poly_len) for k, v in count.items()]
    dict_list.sort(key=lambda x:x[1])
    print(f'Step {i+1}:\n{dict_list}')


count = {}
for let in seed:
    if not count.get(let):
        count[let] = 1
    count[let] += 1

dict_list = [(k, v) for k, v in count.items()]
dict_list.sort(key=lambda x:x[1])
print(f'Part 2 solution: {dict_list[-1][1] - dict_list[0][1]}')

