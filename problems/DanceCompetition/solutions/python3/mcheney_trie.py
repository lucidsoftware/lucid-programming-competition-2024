from collections import defaultdict

class Node:
    def __init__(self, value):
        self.value = value
        self.children = dict()
        self.dancers = set()

root = Node("$")

D, N = [int(ea) for ea in input().split(" ")]

copiers = set()
for d in range(D):
    line = input().split(" ")
    name = line[0]
    routine = line[1:]
    # Process every sub-array of length N
    for starting_i in range(len(routine) - N + 1):
        current = root
        for current_i in range(N):
            move = routine[starting_i + current_i]
            if move not in current.children:
                current.children[move] = Node(move)
            current = current.children[move]
        current.dancers.add(name)
        # If 2 dancers have reached this position, save as copiers
        if len(current.dancers) > 1:
            copiers = copiers.union(set(current.dancers))

print(len(copiers))
