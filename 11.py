example = "0 1 10 99 999"
example2 = "125 17"


def process(intxt):
    stones = []
    for stone_mark in [x for x in intxt.split()]:
        stones.append(int(stone_mark))
    return stones


memo = {}


def num_stones_for(origin_stone, steps):
    if (origin_stone, steps) in memo:
        return memo[(origin_stone, steps)]
    retval = 0
    if steps == 0:
        retval = 1
    elif origin_stone == 0:
        retval = num_stones_for(1, steps - 1)
    elif len(str(origin_stone)) % 2 == 0:
        retval = num_stones_for(
            int(str(origin_stone)[: len(str(origin_stone)) // 2]), steps - 1
        ) + num_stones_for(
            int(str(origin_stone)[len(str(origin_stone)) // 2 :]), steps - 1
        )
    else:
        retval = num_stones_for(origin_stone * 2024, steps - 1)
    memo[(origin_stone, steps)] = retval
    return retval


def part_1(stones):
    total = 0
    for stone in stones:
        total += num_stones_for(stone, steps=25)
    return total


def part_2(stones):
    total = 0
    for stone in stones:
        total += num_stones_for(stone, steps=75)
    return total


with open("11.in", "r") as f:
    intxt = f.read()

print("Day 11 Part 1: ", part_1(process(intxt)))
print("Day 11 Part 2: ", part_2(process(intxt)))
