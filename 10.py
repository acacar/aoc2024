example = """0123
1234
8765
9876"""

example_2 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]


def bfs(start, map, ends):
    queue = [(start, 0)]
    reachable_ends = set()
    while queue:
        (x, y), height = queue.pop(0)
        if (x, y) in ends:
            reachable_ends.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in map and map[nx, ny] == height + 1:
                queue.append(((nx, ny), height + 1))
    return reachable_ends


def bfs_with_path(start, map, ends):
    queue = [(start, 0, ())]
    reachable_ends = set()
    while queue:
        (x, y), height, path = queue.pop(0)
        if (x, y) in ends:
            reachable_ends.add(((x, y), path))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in map and map[nx, ny] == height + 1:
                queue.append(((nx, ny), height + 1, path + (nx, ny)))
    return reachable_ends


def process(input):
    map = {}
    starts = []
    ends = []
    lines = input.splitlines()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            map[x, y] = int(char)
            if char == "0":
                starts.append((x, y))
            elif char == "9":
                ends.append((x, y))
    return map, starts, ends


def part_1(map, starts, ends):
    return sum(len(bfs(start, map, ends)) for start in starts)


def part_2(map, starts, ends):
    return sum(len(bfs_with_path(start, map, ends)) for start in starts)


with open("10.in") as f:
    intxt = f.read()

print(f"Part 1: {part_1(*process(intxt))}")
print(f"Part 2: {part_2(*process(intxt))}")
