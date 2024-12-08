from collections import defaultdict
from itertools import combinations

example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def process(input):
    lines = input.splitlines()
    height = len(lines)
    width = len(lines[0])
    positions = defaultdict(list)
    
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '.':
                positions[char].append((x,y))
                
    return {
        'positions': positions,
        'width': width,
        'height': height
    }


def generate_antinodes(positions: list[tuple[int, int]]):
    antinodes = []
    for pos1, pos2 in combinations(positions, 2):
        if pos1[0] != pos2[0] or pos1[1] != pos2[1]:
            dx = pos2[0] - pos1[0]
            dy = pos2[1] - pos1[1]
            antinodes.append((pos2[0] + dx, pos2[1] + dy))
            antinodes.append((pos1[0] - dx, pos1[1] - dy))
    return antinodes


def generate_harmonic_antinodes(positions: list[tuple[int, int]], width: int, height: int):
    antinodes = []
    for pos1, pos2 in combinations(positions, 2):
        if pos1[0] != pos2[0] or pos1[1] != pos2[1]:
            dx = pos2[0] - pos1[0]
            dy = pos2[1] - pos1[1]
            harmonic = 0
            while True:
                antinode = (pos2[0] + harmonic * dx, pos2[1] + harmonic * dy)
                if 0 <= antinode[0] < width and 0 <= antinode[1] < height:
                    antinodes.append(antinode)
                else:
                    break
                harmonic += 1
            harmonic = 0
            while True:
                antinode = (pos1[0] - harmonic * dx, pos1[1] - harmonic * dy)
                if 0 <= antinode[0] < width and 0 <= antinode[1] < height:
                    antinodes.append(antinode)
                else:
                    break
                harmonic += 1
    return antinodes

def part1(map):
    overall_antinodes = set()
    positions = map['positions']
    width = map['width']
    height = map['height']
    for frequency, positions in map['positions'].items():
        for antinode in generate_antinodes(positions):
            if 0 <= antinode[0] < width and 0 <= antinode[1] < height:
                overall_antinodes.add(antinode)
    return len(overall_antinodes)

def part2(map):
    overall_antinodes = set()
    positions = map['positions']
    width = map['width']
    height = map['height']
    for frequency, positions in map['positions'].items():
        for antinode in generate_harmonic_antinodes(positions, width, height):
            overall_antinodes.add(antinode)
    return len(overall_antinodes)

with open('8.in') as f:
    input = f.read()

print(f'Day 8 Part 1: {part1(process(input))}')
print(f'Day 8 Part 2: {part2(process(input))}')    
