example = """AAAA
BBCD
BBCC
EEEC"""


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
        for dx, dy in [(0, 1), (0, 1), (0, -1), (-1, 0)]:
            print(dx, dy)
            if (
                (x + dx, y + dy) not in to_visit
                and (x + dx, y + dy) in map
                and map[(x + dx, y + dy)] == region_type
            ):
                print(f"{x,y} adding {x+dx,y+dy}")
                to_visit.add((x + dx, y + dy))
        print([v for v in to_visit])
    return region


def part1(map):
    print(map)
    while len(map) > 0:
        print(pop_region(map))


print(example)
print(part1(process(example)))
