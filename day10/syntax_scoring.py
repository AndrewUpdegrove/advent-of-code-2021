import sys
import math


def find_illegal_characters(lines):
    matching_chars = {
        ')' : '(',
        ']' : '[',
        '}' : '{',
        '>' : '<'
    }

    violating_chars = []
    bad_lines = []
    for index, line in enumerate(lines):
        stack = []
        flag = False
        for char in list(line):
            if char in matching_chars.values():
                stack.append(char)
            elif matching_chars.get(char) != stack.pop():
                violating_chars.append(char)
                bad_lines.append(index)
                flag = True
                break
    return (bad_lines, violating_chars)

def complete_lines(lines):
    matching_chars = {
        '(' : ')',
        '{' : '}',
        '[' : ']',
        '<' : '>'
    }
    line_ends = []
    for line in lines:
        stack = []
        for char in list(line):
            if char in matching_chars.keys():
                stack.append(char)
            else:
                assert matching_chars[stack.pop()] == char

        end = ''
        while stack:
            end += matching_chars[stack.pop()]
        line_ends.append(end)

    return line_ends

def calc_autocomplete(lines):
    auto_points = {
        ')' : 1,
        ']' : 2,
        '}' : 3,
        '>' : 4
    }

    scores = []
    for end in lines:
        money = 0
        for char in list(end):
            money *= 5
            money += auto_points[char]
        scores.append(money)
    return scores

with open(sys.argv[1], 'r') as in_file:
    syntax = [line.rstrip() for line in in_file]


point_dict = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

corrupted_lines, bad_chars = find_illegal_characters(syntax)
good_lines = set(range(len(syntax))) - set(corrupted_lines)
total = sum([point_dict.get(a) for a in bad_chars])
print(total)

incomplete_lines = [syntax[a] for a in good_lines]
line_ends = complete_lines(incomplete_lines)
final_scores = calc_autocomplete(line_ends)
final_scores.sort()
print(final_scores[math.floor(len(final_scores) / 2)])

