from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "/Users/joshua/Desktop/CS_FLEX/modules/Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# print(World)

def step_back(direction):
    a = ['n','s','e','w']
    b = ['s','n','w','e']
    rtn = dict(zip(a,b))
    return rtn[direction]

def get_path(start, visited = None):

    # if visited is None / visited should be a set()
    if not visited:
        visited = set()
    # create a path
    path = []
    # add current room to visited set
    visited.add(player.current_room.id)
    # for dir in player.current_room.get_exits() move in that direction
    for direction in player.current_room.get_exits():
        player.travel(direction)
        # if that location is not in the visited set
        if player.current_room.id not in visited:
            # add room to the visited set and add the direction to the path
            visited.add(player.current_room.id)
            path.append(direction)
            # concatincate path with the recursed return of player.current_room.id
            path += get_path(player.current_room.id, visited)
            # add a step_back(direction) to path
            path.append(step_back(direction))
            # step_back
            player.travel(step_back(direction))
        #else step_back
        else:
            player.travel(step_back(direction))
    return path


traversal_path = get_path(player.current_room)
# print(get_exits())
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
# player.travel('s')
# print(player.current_room.id,"<")
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
