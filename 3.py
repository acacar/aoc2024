import re


def part_1():
    total = 0
    with open("3.in","r") as f:
        input = f.read()
    matches = re.findall(r"mul\((\d+?),(\d+?)\)", input)
    for i in matches:
            total += int(i[0]) * int(i[1])
    print(f"Part 1: {total}")


def part_2():
    total = 0
    enabled = True
    with open("3.in","r") as f:
        input = f.read()
    matches = re.findall(r"mul\((\d+?),(\d+?)\)|(do\(\))|(don't\(\))", input)
    for i in matches:
        if i[3] == "don't()":
            enabled = False
        elif i[2] == "do()":
            enabled = True
        elif enabled:
            total += int(i[0]) * int(i[1])
    print(f"Part 2: {total}")

part_1()
part_2()