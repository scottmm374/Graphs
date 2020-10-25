from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# print(player, "current room?")
# <player.Player object at 0x103959850> current room?
# print(room_graph, "room_graph")
# {0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}], 1: [(3, 6), {'s': 0, 'n': 2}], 2: [(3, 7), {'s': 1}], 3: [(4, 5), {'w': 0, 'e': 4}], 4: [(5, 5), {'w': 3}], 5: [(3, 4), {'n': 0, 's': 6}], 6: [(3, 3), {'n': 5}], 7: [(2, 5), {'w': 8, 'e': 0}], 8: [(1, 5), {'e': 7}]} room_graph
# traversal_dict = {}

# for rooms in room_graph:
#     world_rooms = (room_graph[rooms][1])
#     traversal_dict[rooms] = dict

# for key in player.current_room.get_exits():

#     d = {key: None for k in key}

# {0: ['n', 's', 'e', 'w'], 1: ['s', 'n'], 2: ['s'], 3: ['w', 'e'], 4: ['w'], 5: ['n', 's'], 6: ['n'], 7: ['w', 'e'], 8: ['e']}
# traversal_dict[0][0][0] = 3
# print(rooms, room_graph[rooms][1])
# 0 {'n': 1, 's': 5, 'e': 3, 'w': 7}
# world_rooms = (room_graph[rooms][1])
# for i in world_rooms:
#     print(i, world_rooms[i])

# s 5 - e 3 - w 7 -  s 0 - n 2 - s 1 - w 0 - e 4 - w 3 - n 0 - s 6 - n 5 - w 8 e 0  e 7  These print per line
# print("room connecte: \n ", room_graph[rooms][1][1])

#     room = rooms

#     if rooms not in traversal_dict:
#         traversal_dict[room] = rooms

# print((traversal_dict), "Hash")
# # Fill this out with directions to walk


# traversal_path = ['n', 'n']
traversal_path = [player.current_room.id]
# * grabs exits in current room
exits = player.current_room.get_exits()

# ? this gives me the room in the direction we are going in.
# connected_room_by_direction = player.current_room.get_room_in_direction('s')
# print(exits, "exits")
# print(connected_room_by_direction, "room connected. ")
# ['n', 's', 'w', 'e'] exits
# print(traversal_path, "trav path")
# [[0]] trav path


# DFT for discovering rooms
my_travels = {}
visited = []

while len(traversal_path) > 0:

    curr_room = traversal_path.pop(0)
    direction = player.current_room.get_exits()
    choose_direction = random.choice(direction)
    connected = player.current_room.get_room_in_direction(
        str(choose_direction))

    if curr_room not in my_travels:
        my_travels[curr_room] = dict.fromkeys(direction)

        for key, values in my_travels.items():
            print(values)
            for x in values:
                if x == choose_direction:
                    values[x] = connected.id
                print(x, "x")
                print(values[x], "values[x]")
                print(values, "values in second loop")

            # {0: {'n': None, 's': None, 'w': None, 'e': None}} my travels
    print(my_travels, "my travels")
    # print(connected_room_by_direction(direction), "connected")
    print(curr_room, "popped from traversal, curr_room")
    print(direction, "direction")
    print(choose_direction, "choose a direction")
    print(connected, "connected")
    print(visited, "visited")
    if curr_room not in visited:
        # print(curr_path, "if curr_path not visited print")
        visited.append(curr_room)
        # print(visited[curr_path], "visited[curr_path]")
        # for exit in exits:
        #     new_path = traversal_path.copy()
        #     # print(new_path, "new_path = traversal_path.copy()")
        #     new_path.append(exit)
        #     # print(new_path, "new_path.append(exit)")
        #     traversal_path.append(new_path)
    # print(traversal_path, "traversal_path.append(new_path)")
    print(visited, "visted end of if")
    # print(traversal_path, "transversal paths end of if")
print(visited, "visted end of while")
# print(traversal_path, "transversal paths end of while")

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print("test passed")
    # f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    # print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)

# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

# ! Very odd this printed when I did a run on the program
# 10:51  up 23 days, 21:35, 1 user, load averages: 1.49 1.79 1.56
# USER     TTY      FROM              LOGIN@  IDLE WHAT
# michellescott console  -                29Sep20 23days -
