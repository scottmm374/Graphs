

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def create_list(ancestor_list):
    adj_list = {}

    for vert in ancestor_list:

        if vert[0] not in adj_list:
            adj_list[vert[0]] = set()
        # adding the vertices that did not have ancestors(edges)
        if vert[1] not in adj_list:
            adj_list[vert[1]] = set()

        # add edges between verts
        adj_list[vert[1]].add(vert[0])

    # print(adj_list)
    return adj_list


def earliest_ancestor(ancestors, starting_node):
    search_ancestors = [[starting_node]]
    visited = set()

    max_path = 1
    curr_earliest = -1

    while len(search_ancestors) > 0:
        curr_path = search_ancestors.pop(0)
        curr_vert = curr_path[-1]

        if curr_vert not in visited:
            visited.add(curr_vert)

            if len(curr_path) > max_path or len(curr_path) >= max_path and curr_vert < curr_earliest:

                max_path = len(curr_path)
                curr_earliest = curr_vert

            for ancestor in ancestors[curr_vert]:
                new_path = list(curr_path)
                new_path.append(ancestor)
                search_ancestors.append(new_path)
    print(curr_earliest)
    return curr_earliest

    #     if curr_vert not in visited:
    #         # print(curr_vert)
    #         visited.append(curr_vert)
    #         for ancestor in self.get_ancestors(curr_vert):
    #             search.push(curr_path + [ancestor])
    # print(search, "stack in while")


earliest_ancestor(create_list(test_ancestors), 1)  # 10)
# earliest_ancestor(test_ancestors, 2)  # -1)
# earliest_ancestor(test_ancestors, 3)  # 10)
# earliest_ancestor(test_ancestors, 4)  # -1)
# earliest_ancestor(test_ancestors, 5)  # 4)
# earliest_ancestor(test_ancestors, 6)  # 10)
# earliest_ancestor(test_ancestors, 7)  # 4)
# earliest_ancestor(test_ancestors, 8)  # 4)
# earliest_ancestor(test_ancestors, 9)  # 4)
# earliest_ancestor(test_ancestors, 10)  # -1)
# earliest_ancestor(test_ancestors, 11)  # -1)
