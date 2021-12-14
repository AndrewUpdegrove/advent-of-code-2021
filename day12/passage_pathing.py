import sys


class Graph(dict):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.visited = {}
        self.paths = []
        self.multi_enabled = False

    def __missing__(self, key):
        val = self[key] = []
        self.visited[key] = 0
        return val

    def find_all_paths(self, enable_multi = False):
        self.paths.clear()
        curr_path = []
        self.multi_enabled |= enable_multi
        self.dfs('start', curr_path)
        return len(self.paths)

    def dfs(self, node, stack, doubled = False):
        # Base Cases
        if node == 'end':
            stack.append('end')
            self.paths.append(stack.copy())
            stack.pop()
            return

        if node == 'start' or not self.multi_enabled:
            if self.visited[node]:
                return
        else:
            if doubled:
                if self.visited[node] > 0:
                    return
            else:
                if self.visited[node] > 1:
                    return

        # Action
        stack.append(node)
        if node.islower():
            self.visited[node] += 1
            if self.visited[node] > 1:
                doubled |= True


        # Recursive call
        for neighbor in self[node]:
            self.dfs(neighbor, stack, doubled)

        self.visited[node] -= 1
        doubled &= False
        stack.pop()
        return

caves = Graph()
with open(sys.argv[1], 'r') as in_file:
    for line in in_file:
        nodes = line.rstrip().split('-')
        caves[nodes[0]].append(nodes[1])
        caves[nodes[1]].append(nodes[0])

# Part 1
'''
num_paths = caves.find_all_paths()
print(f'A grand total of {num_paths} paths were found.')
'''

# Part 2
num_paths = caves.find_all_paths(True)
print(f'A grand total of {num_paths} paths were found.')
