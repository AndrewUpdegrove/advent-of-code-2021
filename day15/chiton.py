import sys
import heapq

class Graph(dict):
    def __init__(self, text_grid):
        super().__init__()
        self.x_max = None
        self.y_max = None
        self._generate_graph(text_grid)

    class Node:
        def __init__(self, coor):
            self.entry_cost = None
            self.position = coor
            self.adjacency = None
            self.visited = False
            self.prev_node = None
            self.shortest_length = float('inf')

    def __missing__(self, key):
        val = self[key] = self.Node(key)
        return val
    
    def find_path(self, start, end):
        self[start].shortest_length = 0
        p_queue = []
        heapq.heappush(p_queue, (0, start))
        while p_queue and not self[end].visited:
            _, curr = heapq.heappop(p_queue)
            if not self[curr].visited:
                for adj_node in self[curr].adjacency:
                    if not self[adj_node].visited:
                        new_path = self[curr].shortest_length + self[adj_node].entry_cost 
                        if new_path < self[adj_node].shortest_length:
                            self[adj_node].shortest_length = new_path
                            self[adj_node].prev_node = curr
                        heapq.heappush(p_queue, (self[adj_node].shortest_length, adj_node))
                self[curr].visited |= True
        return self[end].shortest_length

    def _generate_graph(self, text_grid):
        # set limits
        self.y_max = 0
        for dumb in text_grid:
            self.y_max += 1
            if not self.x_max:
                self.x_max = len(dumb.rstrip())
                
        text_grid.seek(0)
        # populate graph
        for j, line in enumerate(text_grid):
            for i, char in enumerate(line.rstrip()):
                pos = (i,j)
                self[pos].adjacency = self.generate_surrounding_points(i,j)
                self[pos].entry_cost = int(char)

    def generate_surrounding_points(self, x, y):
        res = []
        if x+1 < self.x_max:
            res.append((x+1,y))
        if x-1 >= 0:
            res.append((x-1,y))
        if y+1 < self.y_max:
            res.append((x,y+1))
        if y-1 >= 0:
            res.append((x,y-1))
        return res


# with open(sys.argv[1], 'r') as in_file:
#     the_cave = Graph(in_file)
# Part 1 solution
# short_path = the_cave.find_path((0,0), (the_cave.x_max-1, the_cave.y_max-1))
# print(short_path)


# create new input file
with open(sys.argv[1], 'r') as in_file:
    with open('tile_grid.txt', 'w') as out_file:
        for i in range(5):
            in_file.seek(0)
            for line in in_file:
                new_line = ''
                for j in range(5):
                    for char in line.rstrip():
                        new_int = int(char)+i+j
                        if new_int > 9:
                            new_int -= 9
                        new_line += str(new_int)
                out_file.write(new_line+'\n')

with open('tile_grid.txt', 'r') as in_file:
    bigger_cave = Graph(in_file)

# Part 2 Solution
no_mo_danger = bigger_cave.find_path((0,0), (bigger_cave.x_max-1, bigger_cave.y_max-1))
print(no_mo_danger)

