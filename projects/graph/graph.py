"""
Simple graph implementation
"""
from util import Stack, Queue
import collections  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set([])

    def add_edge(self, v1, v2):
        if v1 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            self.vertices[v1] = [v2]

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        visited, queue = set(), [starting_vertex]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(self.vertices[vertex] - visited)
        for i in visited:
            print(i)

    def dft(self, starting_vertex):
        q = Stack()
        visited = set()     
		# Init:
        q.push(starting_vertex)
		# While queue isn't empty
        while q.size() > 0:
            v = q.pop()
            if v not in visited:
                print(v)   # "Visit" the node
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.push(neighbor)



    def dft_recursive(self, starting_vertex, visited=None):
        if visited is None:
            visited = set()
        print(starting_vertex)
        visited.add(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        # maintain a queue of paths
        queue = []
        # push the first path into the queue
        queue.append([starting_vertex])
        while queue:
            # get the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            # path found
            if node == destination_vertex:
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for adjacent in self.vertices.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return queue

    def dfs(self, starting_vertex, destination_vertex):
        pass

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = [starting_vertex]
        print(starting_vertex)
        visited.add(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == destination_vertex:
                    return new_path
                dfs_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                if dfs_path is not None:
                    return dfs_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
