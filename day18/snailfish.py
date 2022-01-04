import sys
import logging
import math
import copy

class Node:
    def __init__(self):
        self._left = None
        self._right = None
        self._data = None
        self._parent = None
        self._magnitude = None
        self.depth = None

    def __add__(self, b):
        head = Node()
        head.add_child(self.copy())
        head.add_child(b.copy())
        head.update_depth()
        Node.Reduce(head)
        return head

    def copy(self):
        new_node = copy.deepcopy(self)
        return new_node

    def update_depth(self):
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

        if self.left:
            self.left.update_depth()
        if self.right:
            self.right.update_depth()

    def magnitude(self):
        if self.is_leaf():
            self._magnitude = self.data
        else:
            self._magnitude = (3 * self.left.magnitude()) + (2 * self.right.magnitude())
        return self._magnitude

    # d: direction to find nearest adjacent leaf.
    #       'l' look to left, 'r' look to right
    # 
    @classmethod
    def find_adjacent_leaf(cls, n, prim_dir = 'left'):
        assert n.is_leaf(), "Provided node is not a leaf node :shruggers:"
        if prim_dir == 'left':
            sec_dir = 'right'
        elif prim_dir == 'right':
            sec_dir = 'left'
        else:
            raise ValueError(f"{prim_dir} is not a valid direction command to parse the tree")

        prev = n
        nex = n.parent
        while nex and getattr(nex, prim_dir) == prev:
            prev = nex
            nex = nex.parent
        if not nex:
            return None

        prev = nex
        nex = getattr(nex, prim_dir)
        while not nex.is_leaf():
            nex = getattr(nex, sec_dir)
        return nex

    @classmethod
    def Explode(cls, n):
        exit = 0
        if not n.is_leaf():
            if n.depth >= 4 and n.left.is_leaf() and n.right.is_leaf():
                n.data = 0
                adj_left_leaf = cls.find_adjacent_leaf(n.left, 'left')
                adj_right_leaf = cls.find_adjacent_leaf(n.right, 'right')
                if adj_left_leaf:
                    adj_left_leaf.data += n.left.data
                if adj_right_leaf:
                    adj_right_leaf.data += n.right.data

                n.right = None; n.left = None
                exit = n
        return exit

    @classmethod
    def Split(cls, n):
        exit = 0
        if n.is_leaf() and n.data >= 10:
            n.add_child(math.floor(n.data/2.0))
            n.add_child(math.ceil(n.data/2.0))
            n.data = None
            exit = n
        return exit

    @classmethod
    def Reduce(cls, n):
        assert not n.parent, "Supplied Node is not the head of a tree."
        flag = True
        while flag:
            exit_code = n.dfs(Node.Explode)
            if exit_code:
                continue
            exit_code = n.dfs(Node.Split)
            if not exit_code:
                flag = False

    def dfs(self, func):
        exit = func(self)
        if exit:
            return exit

        if self.left:
            exit_code = self.left.dfs(func)
            if exit_code:
                return exit_code
        if self.right:
            exit_code = self.right.dfs(func)
            if exit_code:
                return exit_code

        return 0

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def parent(self):
        return self._parent

    @property
    def data(self):
        return self._data

    @parent.setter
    def parent(self, p):
        # if self._parent:
            # logging.warn("Reassinging parent node. Potentially creating unreachable tree.")
        if not isinstance(p, Node): raise AttributeError("Parent Attribute must be another Node.")
        self._parent = p
            
    @data.setter
    def data(self, d):
        self._data = d

    @left.setter
    def left(self, l):
        if not isinstance(l, Node) and l is not None: raise AttributeError("New Left Child is not a Node")
        self._left = l

    @right.setter
    def right(self, r):
        if not isinstance(r, Node) and r is not None: raise AttributeError("New Right Child is not a Node")
        self._right = r

    def is_leaf(self):
        return False if self.left or self.right else True

    def is_head(self):
        return not bool(self._parent) 

    def add_child(self, d = None):
        if isinstance(d, Node):
            child = d
        else:
            child = Node()
            if d is not None:
                child.data = d
        child.parent = self
        if not self.left:
            self.left = child
        elif not self.right:
            self.right = child
        else: 
            raise RuntimeError("Attempted to set a third child node when constructing binary tree.")

        self.update_depth()
        return child

    def print_tree(self):
        if self.is_leaf():
            print(self.data, end='')
        else:
            print('[',end='')
            self.left.print_tree()
            print(',', end='')
            self.right.print_tree()
            print(']',end='')
            

def tree_constructor(line):
    pointer = None
    char_list = list(line)
    num_set = ['0','1','2','3','4','5','6','7','8','9']
    while char_list:
        char = char_list.pop(0)
        if char == '[':
            if not pointer:
                pointer = Node()
            else:
                pointer = pointer.add_child()
        elif char in num_set:
            while char_list[0] in num_set:
                char += char_list.pop(0)
            pointer.add_child(int(char))
        elif char == ']':
            if pointer.parent:
                pointer = pointer.parent
            else:
                # Sanity Check
                assert not char_list, "Found None parent and there are still characters to parse????"

    pointer.depth = 0
    pointer.update_depth()
    return pointer

# must be passed list of numbers already constructed into trees
def add_all_numbers(num_list):
    final = num_list.pop(0)
    while num_list:
        final = final + num_list.pop(0)

    return final

snail_number_list = []
with open(sys.argv[1], 'r') as in_file:
    for line in in_file:
        snail_number_list.append(tree_constructor(line.rstrip()))


# Part 1
'''
final_number = add_all_numbers(snail_number_list)


# final_number.print_tree()
# print('\n')
print(final_number.magnitude())
'''

# Part 2
biggest_magnitude = 0
best_pair = ()
for i, num_1 in enumerate(snail_number_list):
    for j, num_2 in enumerate(snail_number_list):
        if i == j: continue
        current_add = num_1 + num_2
        if current_add.magnitude() > biggest_magnitude:
            biggest_magnitude = current_add.magnitude()
            best_pair = (num_1, num_2)

print(biggest_magnitude)


