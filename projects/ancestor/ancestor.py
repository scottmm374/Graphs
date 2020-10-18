from stack import Queue


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


class Graph:

    def __init__(self):
        self.vertices = {}

    def __str__(self):
        return f'{self.vertices}'

    def add_vertices(self, ancestor_list):
        for vert in range(len(ancestor_list)):

            self.vertices[ancestor_list[vert][0]] = set()
            # adding the vertices that did not have ancestors(edges)
            if ancestor_list[vert][1] not in self.vertices:
                self.vertices[ancestor_list[vert][1]] = set()

        print(self.vertices)

    def add_edge(self, ancestor_list):
        for edge in range(len(ancestor_list)):
            key = ancestor_list[edge][0]
            value = ancestor_list[edge][1]
            self.vertices[key].add(value)

            # Somne print checks
            # print(ancestor_list[edge], "prints whole tuple set")
            # print(ancestor_list[edge][0], "should be vert")
            # print(ancestor_list[edge][1], "should be edge")

        print(self.vertices, "edges added?")

    def get_ancestors(self, vertex_id):
        return self.vertices[vertex_id]

    def earliest_ancestor(self, ancestors, starting_node):
        earliest_ancestors = {}
        search = Queue()
        visited = []

        curr_vert = [starting_node]
        search.enqueue(curr_vert)

        while len(search) > 0:
            curr_vert = search.dequeue()
            print(curr_vert, "curr_vert")

            if curr_vert[-1] not in visited:
                if not self.vertices[curr_vert[-1]]:
                    generations = len(curr_vert)

                    if generations not in earliest_ancestors or curr_vert[-1] < earliest_ancestors[generations]:
                        earliest_ancestors[generations] = curr_vert[-1]

                for ancestor in self.vertices[curr_vert[-1]]:
                    search.enqueue(curr_vert + [ancestor])

                visited.append(curr_vert[-1])

        if curr_vert[-1] == starting_node:
            return -1

        return earliest_ancestors[max(earliest_ancestors.keys())]

        #     if curr_vert not in visited:
        #         # print(curr_vert)
        #         visited.append(curr_vert)
        #         for ancestor in self.get_ancestors(curr_vert):
        #             search.push(curr_path + [ancestor])
        # print(search, "stack in while")


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
graph.add_edge(test_ancestors)
# graph.add_edge(9, 8)
# graph.add_edge(3, 2)
# graph.add_edge(3, 1)
# graph.add_edge(5, 4)
# graph.add_edge(3, 5)
# graph.add_edge(8, 4)
# graph.add_edge(8, 11)
# graph.add_edge(1, 10)

print(graph.earliest_ancestor(test_ancestors, 6))
