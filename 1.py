from collections import Counter


def load_input(filename: str):
    list1 = []
    list2 = []
    with open(filename, "r") as f:
        for line in f.readlines():
            num1, num2 = (int(x) for x in line.split())
            list1.append(num1)
            list2.append(num2)
    return (list1, list2)

def part1():
    list1, list2 = load_input("1.in")
    list1 = sorted(list1)
    list2 = sorted(list2)
    total = 0
    for n1, n2 in zip(list1, list2):
        total += abs(n1-n2)
    print(f"Day 1 Part 1: {total}")

def part2():
    list1, list2 = load_input("1.in")
    c = Counter(list2)
    total = 0
    for n1 in list1:
        total += n1 * c[n1]
    print(f"Day 1 Part 2: {total}")

part1()
part2()
