import re

example = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def process(text):
    pattern = re.compile(
        r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
    )
    matches = pattern.findall(text)
    result = []
    for match in matches:
        button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y = map(
            int, match
        )
        result.append(
            {
                "A": (button_a_x, button_a_y),
                "B": (button_b_x, button_b_y),
                "prize": (prize_x, prize_y),
            }
        )
    return result

def cheapest_prize(machine, prize_offset=0):
    a_dx, a_dy = machine["A"]
    b_dx, b_dy = machine["B"]
    prize_x, prize_y = machine["prize"]
    prize_x += prize_offset
    prize_y += prize_offset
    # a_dx * a + b_dx * b = prize_x
    # a_dy * a + b_dy * b = prize_y
    # Solve for a and b:
    a = (prize_x * b_dy - b_dx * prize_y) / (a_dx * b_dy - b_dx * a_dy)
    b = (prize_x * a_dy - a_dx * prize_y) / (b_dx * a_dy - a_dx * b_dy)
    
    if a >= 0 and a.is_integer() and b >= 0 and b.is_integer():
        return (int(a), int(b))
    else:
        return None

def part1(machines):
    total_cost = 0
    for machine in machines:
        x = cheapest_prize(machine)
        if x is not None:
            total_cost += 3 * x[0] + x[1]
    return total_cost


def part2(machines):
    total_cost = 0
    for machine in machines:
        x = cheapest_prize(machine, prize_offset=10000000000000)
        if x is not None:
            total_cost += 3 * x[0] + x[1]
    return total_cost


with open("13.in") as f:
    machines = process(f.read())

print(f"Day 13 Part 1: {part1(machines)}")
print(f"Day 13 Part 2: {part2(machines)}")
