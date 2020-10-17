from stack import Stack


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.key = None
        self.value = None

    def __str__(self):
        return f'{self.vertices}'

    def add_vertices(self, ancestor_list):
        for vert in range(len(ancestor_list)):
            self.vertices[ancestor_list[vert][0]] = set()
            if ancestor_list[vert][1] not in self.vertices:
                self.vertices[ancestor_list[vert][1]] = set()

                # value = ancestor_list[0][1]
                # self.vertices[value]

        print(self.vertices)

        # def add_vertex(self, ancestor_list):
        #     self.vertices[ancestor_list[0]]

    # def add_edge(self, ancestor_list):
    #     for x in range(len(ancestor_list)):
    #         self.vertices[ancestor_list[x][1]] = set

    #     else:
    #         print("Vertex not found")

        # def get_neighbors(self, vertex_id):
        #     return self.vertices[vertex_id]

        # def earliest_ancestor(self, ancestors, starting_node):

        #     path = Stack()
        #     path.push([starting_node])

        #     visited = set()

        #     while len(path) > 0:
        #         # dequeue the current PATH from the queue
        #         curr_path = path.pop()
        #         # get the current vertex to analyze from the path, vertex at end of path list
        #         curr_vert = curr_path[-1]

        #        # CHECK IF CURRENT VERTEX IS THE TARGET VERTEX, if yes return path
        #         if curr_vert.get_neighbors() == None:
        #             return curr_vert

        #         if curr_vert not in visited:
        #             # add vertex to visited list
        #             visited.add(curr_vert)

        #             for neighbor in self.get_neighbors(curr_vert):
        #                 # Add the path to that neighbor, to the queue
        #                 path.push(curr_path + [neighbor])
graph = Graph()
graph.add_vertices(test_ancestors)
# graph.add_vertex(2)
# graph.add_vertex(3)
# graph.add_vertex(4)
# graph.add_vertex(5)
# graph.add_vertex(6)
# graph.add_vertex(7)
# graph.add_vertex(8)
# graph.add_vertex(9)
# graph.add_vertex(10)
# graph.add_vertex(11)
# graph.add_edge(6, 3)
# graph.add_edge(6, 5)
# graph.add_edge(7, 5)
# graph.add_edge(9, 8)
# graph.add_edge(3, 2)
# graph.add_edge(3, 1)
# graph.add_edge(5, 4)
# graph.add_edge(3, 5)
# graph.add_edge(8, 4)
# graph.add_edge(8, 11)
# graph.add_edge(1, 10)


# print(graph.earliest_ancestor(5, 7))
