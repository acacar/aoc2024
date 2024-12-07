def load_input(filename):
    grid = []
    with open(filename, "r") as f:
        for line in f.readlines():
            grid.append([str(x) for x in line.strip()])        
    return grid

example_grid = [
['M','M','M','S','X','X','M','A','S','M'],
['M','S','A','M','X','M','S','M','S','A'],
['A','M','X','S','X','M','A','A','M','M'],
['M','S','A','M','A','S','M','S','M','X'],
['X','M','A','S','A','M','X','A','M','M'],
['X','X','A','M','M','X','X','A','M','A'],
['S','M','S','M','S','A','S','X','S','S'],
['S','A','X','A','M','A','S','A','A','A'],
['M','A','M','M','M','X','M','M','M','M'],
['M','X','M','X','A','X','M','A','S','X']
]

def part1(grid):
    total = 0
    tgt = "XMAS"
    tgt_last = len(tgt)-1
    for y in range(len(grid)):
        for x in range(tgt_last, len(grid[y])): # Backward Horizontal
            test_ok = True
            for i in range(tgt_last+1):
                if grid[y][x-i] != tgt[tgt_last-i]:
                    test_ok = False
                    break
            if test_ok:
                total += 1
    for y in range(len(grid)):
        for x in range(tgt_last, len(grid[y])):            # Forward Horizontal
            test_ok = True
            for i in range(tgt_last+1):
                if grid[y][x-i] != tgt[i]:
                    test_ok = False
                    break
            if test_ok:
                total += 1
    for y in range(tgt_last, len(grid)):
        for x in range(len(grid[y])):            # Backward Vertical
            test_ok = True
            for i in range(tgt_last+1):
                if grid[y-i][x] != tgt[tgt_last-i]:
                    test_ok = False
                    break
            if test_ok:
                total += 1
    for y in range(tgt_last, len(grid)):
        for x in range(len(grid[y])):            # Forward Vertical
            test_ok = True
            for i in range(tgt_last+1):
                if grid[y-i][x] != tgt[i]:
                    test_ok = False
                    break
            if test_ok:
                total += 1
    for y in range(tgt_last, len(grid)):
        for x in range(tgt_last, len(grid)):            # Backward Diagonal
            test_ok = True
            for i in range(tgt_last+1):
                if grid[y-i][x-i] != tgt[tgt_last-i]:
                    test_ok = False
                    break
            if test_ok:
                total += 1
    for y in range(tgt_last, len(grid)):
        for x in range(tgt_last, len(grid)):            # Forward Diagonal
            test_ok = True
            for i in range(tgt_last+1):
                if grid[y-i][x-i] != tgt[i]:
                    test_ok = False
                    break
            if test_ok:
                total += 1
    for y in range(len(grid)-tgt_last):
        for x in range(tgt_last, len(grid[y])):            # Reverse Other Diagonal
            test_ok = True
            for i in range(tgt_last+1):
                if grid[y+i][x-i] != tgt[tgt_last-i]:
                    test_ok = False
                    break
            if test_ok:
                total += 1
    for y in range(len(grid)-tgt_last):
        for x in range(tgt_last, len(grid[y])):            # Forward Other Diagonal
            test_ok = True
            for i in range(tgt_last+1):
                if grid[y+i][x-i] != tgt[i]:
                    test_ok = False
                    break
            if test_ok:
                total += 1
    return total


def part2(grid):
    total = 0
    for y in range(1, len(grid)-1):
        for x in range(1, len(grid)-1):            # Backward Diagonal
            if grid[y][x] == 'A':
                if (grid[y-1][x-1] == 'M' and grid[y-1][x+1] == 'M' and \
                    grid[y+1][x-1] == 'S' and grid[y+1][x+1] == 'S') \
                    or \
                    (grid[y-1][x-1] == 'M' and grid[y-1][x+1] == 'S' and \
                     grid[y+1][x-1] == 'M' and grid[y+1][x+1] == 'S') \
                    or \
                    (grid[y-1][x-1] == 'S' and grid[y-1][x+1] == 'M' and \
                     grid[y+1][x-1] == 'S' and grid[y+1][x+1] == 'M') \
                    or \
                    (grid[y-1][x-1] == 'M' and grid[y-1][x+1] == 'M' and \
                     grid[y+1][x-1] == 'S' and grid[y+1][x+1] == 'S') \
                    or \
                    (grid[y-1][x-1] == 'S' and grid[y-1][x+1] == 'S' and \
                     grid[y+1][x-1] == 'M' and grid[y+1][x+1] == 'M'):
                    # print(x,y, "*")
                    total += 1  
    return total

if __name__ == "__main__":
    grid = load_input("4.in")
    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")
