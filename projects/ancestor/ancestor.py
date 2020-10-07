from collections import defaultdict


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def dfs(starting_vertex, family):
    # Depth first search uses stacks so...
    # Create a stack
    stack = Stack()
    stack.push([starting_vertex])

    # Create an array for visited vertices
    visited = []

    while stack.size() > 0:
        path = stack.pop()

        # Get the last vertex in the path
        vertex = path[-1]

        # Check if the vertex has been visited or not
        if vertex not in visited:
            visited.append(vertex)

        for descendant in family[vertex]:
            new_path = path.copy()
            new_path.append(descendant)
            stack.push(new_path)

    return visited[-1]

def earliest_ancestor(ancestors, starting_node):
    # default items are created using list(), which returns a new empty list object.
    family = defaultdict(list)

    # Creates a dictionary where each child (key) has parents (values)
    for parent, child in ancestors:
        family[child].append(parent)

    # If the child has no parents 🤷🏼‍♂️
    if starting_node not in family:
        return -1

    # Perform DFS using the specified ID and the family list
    earliest = dfs(starting_node, family)

    return earliest