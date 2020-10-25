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


exits = player.current_room.get_exits()

# Final dictionary, adding as we walk.
my_travels = {}
traversal_path = [[player.current_room.id]]
visited = []

while len(traversal_path) > 0:

    curr_path = traversal_path.pop(0)
    print(curr_path, "curr path")
    # [0, 'n', 'n', 'n', 's', 's', 'e', 'e', 's'] curr path
    curr_room = curr_path[-1]
    print(curr_room, "curr Room")
    direction = player.current_room.get_exits()
    choose_direction = random.choice(direction)

    connected = player.current_room.get_room_in_direction(
        str(choose_direction))

    if curr_room not in visited:
        visited.append(curr_room)

    # # ! adds new rooms to travel dict - works good
    if curr_room not in my_travels:

        my_travels[curr_room] = dict.fromkeys(direction)

    # ! checks final dictionary, exits in room, and updates values.
    for key, values in my_travels.items():
        print(values)
        for x in values:
            if x == choose_direction:
                values[x] = connected.id
                print(x, "x")
                print(values[x], "values[x]")
                print(values, "values in second loop")

            new_path = list(curr_path)
            new_path.append(values[x])
            traversal_path.append(new_path)

    # {0: {'n': None, 's': None, 'w': None, 'e': None}} my travels
    print(my_travels, "my travels")
    # print(connected_room_by_direction(direction), "connected")
    # print(curr_room, "popped from traversal, curr_room")
    print(direction, "direction")
    print(choose_direction, "choose a direction")
    print(connected, "connected")
    print(visited, "visited")

    # print(visited, "visted end of if")
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
