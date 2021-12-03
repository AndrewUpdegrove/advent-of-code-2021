import sys

with open(sys.argv[1], 'r') as in_file:
    instructions = [line.rstrip() for line in in_file]

h_pos = 0
depth = 0

for operation in instructions:
    split = operation.split()
    direction = split[0]
    amount = int(split[1])
    if direction == "forward":
        h_pos += amount
    elif direction == "down":
        depth += amount
    else:
        depth -= amount

print(f"Horizontal position: {h_pos} and depth: {depth}")
print(f"Position * depth: {h_pos*depth}")
