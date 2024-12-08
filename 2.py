def load_input(filename):
    with open(filename, "r") as f:
        reports = [[int(l) for l in line.split()] for line in f.readlines()]
    return reports

ex_reports = [
[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9],
]


def part1(reports):
    num_ok = 0
    for report in reports:
        if check_report(report):
            num_ok += 1
                
    return num_ok

def part2(reports):
    num_ok = 0
    for report in reports:
        if not check_report(report):
            for i in range(len(report)):
                if check_report(report[:i] + report[i+1:]):
                    num_ok += 1
                    break
        else:
            num_ok +=1
    return num_ok

def check_report(report):
    dir = None
    ok = True
    for i in range(1,len(report)):
        diff = report[i-1] - report[i]
        if dir is None:
            if diff < 0:
                dir = "up"
            else:
                dir = "down"
        if diff < 0:
            if dir == "down":
                ok = False
                break
        else:
            if dir == "up":
                ok = False
                break
        if not (1 <= abs(diff) <= 3):
            ok = False
            break
    return ok



print(f"Day 2 Part 1: {part1(load_input('2.in'))}")
print(f"Day 2 Part 2: {part2(load_input('2.in'))}")
