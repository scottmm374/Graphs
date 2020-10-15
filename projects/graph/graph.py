"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

# for testing in python preview
# class Queue():
#     def __init__(self):
#         self.queue = []
#         self.size = 0

# def __str__(self):
#     return f'{self.queue} : QUE'

# def __len__(self):
#     return len(self.queue)

# def enqueue(self, value):
#     self.queue.append(value)
#     self.size += 1
#     return value

# def dequeue(self):
#     if self.size >= 1:
#         value = self.queue.pop(0)
#         self.size -= 1
#         return value

#     else:
#         return None


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("Vertex not found")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

# ! <------------------------------------------------------>

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        que = Queue()
        que.enqueue(starting_vertex)

        # create list to keep track of visted verticies
        visited = []

        while len(que) > 0:
            curr_vert = que.dequeue()

            if curr_vert not in visited:
                print(curr_vert)
                visited.append(curr_vert)

                for neighbor in self.get_neighbors(curr_vert):
                    que.enqueue(neighbor)

# ! <------------------------------------------------------>

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        dftStack = Stack()
        dftStack.push(starting_vertex)

        visited = []

        while len(dftStack) > 0:
            curr_vert = dftStack.pop()

            if curr_vert not in visited:
                print(curr_vert)
                visited.append(curr_vert)
                for neighbor in self.get_neighbors(curr_vert):
                    dftStack.push(neighbor)

 # ! <------------------------------------------------------>

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if starting_vertex in visited:
            return
        print(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            visited.add(starting_vertex)
            self.dft_recursive(neighbor, visited)


# ! <------------------------------------------------------>

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        path = Queue()
        # creating empty path que with starting vertex
        path.enqueue([starting_vertex])
        visited = set()

        while len(path) > 0:
            # dequeue the current PATH from the queue
            curr_path = path.dequeue()
            # get the current vertex to analyze from the path, vertex at end of path list
            curr_vert = curr_path[-1]

           # CHECK IF CURRENT VERTEX IS THE TARGET VERTEX, if yes return path
            if curr_vert == destination_vertex:
                return curr_path

            if curr_vert not in visited:
                # add vertex to visited list
                visited.add(curr_vert)

                for neighbor in self.get_neighbors(curr_vert):
                    # Add the path to that neighbor, to the queue
                    path.enqueue(curr_path + [neighbor])

            # print("Que when done with while loop : \n", path)

    # ! <------------------------------------------------------>

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        path = Stack()
        path.push([starting_vertex])

        visited = set()

        while len(path) > 0:
            # dequeue the current PATH from the queue
            curr_path = path.pop()
            # get the current vertex to analyze from the path, vertex at end of path list
            curr_vert = curr_path[-1]

           # CHECK IF CURRENT VERTEX IS THE TARGET VERTEX, if yes return path
            if curr_vert == destination_vertex:
                return curr_path

            if curr_vert not in visited:
                # add vertex to visited list
                visited.add(curr_vert)

                for neighbor in self.get_neighbors(curr_vert):
                    # Add the path to that neighbor, to the queue
                    path.push(curr_path + [neighbor])

    # ! <------------------------------------------------------>

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass

    # ! <------------------------------------------------------>
    # ! <------------------------------------------------------>


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
    print(graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(graph.dft(1))
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
