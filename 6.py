from collections import defaultdict
from itertools import product
import sys


example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


# ^ > v < : every time you hit an obstacle turn right. i.e. facing = (facing + 1) % 4
UP, RIGHT, DOWN, LEFT = range(4)

facing = {
    "^": UP,
    ">": RIGHT,
    "v": DOWN,
    "<": LEFT,
}

# the (dx, dy) for each direction, ordered according to UP, RIGHT, DOWN, LEFT
directions = {
    UP: (0, -1),
    RIGHT: (1, 0),
    DOWN: (0, 1),
    LEFT: (-1, 0),
}

# Given the the example, we need to create a dict of the form:
# {
#     (x, y): "." or "#"
# }


def process_map(map):
    map = {
        (x, y): c for y, line in enumerate(map.split("\n")) for x, c in enumerate(line)
    }
    # find the starting position ( where the arrow is)
    start = next((x, y) for (x, y), c in map.items() if c in "^>v<")
    # get the direction
    direction = facing[map[start]]
    # set the start to "."
    map[start] = "."
    return map, start, direction


def part1(map, start, direction):
    path, _ = simulate_path(map, start, direction)
    # return the length of unique positions in the path
    return len(set(path))


def simulate_path(map, start, direction):
    width = max(x for x, y in map) + 1
    height = max(y for x, y in map) + 1
    x, y = start
    path = []
    visited = set()  # Track (position, direction) pairs
    path.append((x, y))

    while True:
        # Store current state
        state = (x, y, direction)
        if state in visited:
            # We found a cycle
            return path, True
        visited.add(state)

        dx, dy = directions[direction]
        if not (0 <= x + dx < width and 0 <= y + dy < height):
            # Hit boundary
            return path, False

        if map[(x + dx, y + dy)] == "#":
            direction = (direction + 1) % 4
        else:
            x, y = x + dx, y + dy
            path.append((x, y))


def part2(map, start, direction):
    map_size = ((max(x for x, y in map) + 1), (max(y for x, y in map) + 1))
    solutions = 0
    for x, y in product(range(map_size[0]), range(map_size[1])):
        candidate_map = {**map, (x, y): "#"}
        path, is_cycle = simulate_path(candidate_map, start, direction)
        if is_cycle:
            solutions += 1
    return solutions


with open("6.in") as f:
    intxt = f.read()

print(f"Day 6 Part 1: {part1(*process_map(intxt))}")

print("Day 6 Part 2 (might take a while, suboptimal solution): ", end="")
sys.stdout.flush()
print(part2(*process_map(intxt)))
