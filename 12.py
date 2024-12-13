example_1 = """AAAA
BBCD
BBCC
EEEC"""

example_2 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


def process(input: str):
    map = {}
    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            map[(x, y)] = char
    return map


def pop_region(map: dict):
    x, y = next(iter(map.keys()))
    region_type = map[(x, y)]
    region = {}
    to_visit = set()
    to_visit.add((x, y))
    while len(to_visit) > 0:
        x, y = to_visit.pop()
        region[(x, y)] = map.pop((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (
                (x + dx, y + dy) not in to_visit
                and (x + dx, y + dy) in map
                and map[(x + dx, y + dy)] == region_type
            ):
                to_visit.add((x + dx, y + dy))
    return region


def plot_perimeter(region, x, y):
    perimeter = 0
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if (x + dx, y + dy) not in region:
            perimeter += 1
    return perimeter


def region_perimeter(region):
    return sum(plot_perimeter(region, x, y) for x, y in region)


def region_num_sides(region):
    sides = 0
    directions = {(0, 1): "d", (1, 0): "r", (0, -1): "u", (-1, 0): "l"}
    for x, y in region:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (x + dx, y + dy) not in region:
                sides += 1
                match directions[(dx, dy)]:
                    case "u":
                        nx, ny = (-1, 0)  # left neighbor
                    case "l":
                        nx, ny = (0, 1)  # down neighbor
                    case "d":
                        nx, ny = (1, 0)  # right neighbor
                    case "r":
                        nx, ny = (0, -1)  # up neighbor
                if (x + nx, y + ny) in region and (
                    x + nx + dx,
                    y + ny + dy,
                ) not in region:
                    sides -= 1
    return sides


def cost_p1(region):
    return region_perimeter(region) * len(region)


def cost_p2(region):
    return region_num_sides(region) * len(region)


def part1(map):
    total = 0
    while len(map) > 0:
        total += cost_p1(pop_region(map))
    return total


def part2(map):
    total = 0
    while len(map) > 0:
        total += cost_p2(pop_region(map))
    return total


with open("12.in", "r") as f:
    intxt = f.read()

print(part1(process(intxt)))
print(part2(process(intxt)))
