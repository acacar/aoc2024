from collections import Counter
from dataclasses import dataclass
from math import prod

example = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def parse_input(input):
    for line in input.splitlines():
        p, v = line.split(" ")
        p = p[2:]
        v = v[2:]
        px, py = p.split(",")
        vx, vy = v.split(",")
        yield (int(px), int(py)), (int(vx), int(vy))


@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int

    def move(self, width, height):
        self.x = (self.x + self.vx) % width
        self.y = (self.y + self.vy) % height


@dataclass
class Area:
    width: int
    height: int
    robots: list[Robot]

    def move_all(self, step_count=1):
        for _ in range(step_count):
            for robot in self.robots:
                robot.move(self.width, self.height)

    def get_quadrant(self, robot: Robot):
        # width and height are odd, the middle row and column don't belong to any quadrant
        if robot.x < self.width // 2:
            if robot.y < self.height // 2:
                return "NW"
            elif robot.y == self.height // 2:
                return "NA"
            else:
                return "SW"
        elif robot.x == self.width // 2:
            return "NA"
        else:
            if robot.y < self.height // 2:
                return "NE"
            elif robot.y == self.height // 2:
                return "NA"
            else:
                return "SE"

    def get_quadrant_counts(self):
        return list(
            Counter(
                self.get_quadrant(robot)
                for robot in self.robots
                if self.get_quadrant(robot) != "NA"
            ).values()
        )

    def get_safety_score(self):
        return prod(self.get_quadrant_counts())

    def get_robot_center(self):
        total_x = sum(robot.x for robot in self.robots)
        total_y = sum(robot.y for robot in self.robots)
        return (total_x // len(self.robots), total_y // len(self.robots))

    def calculate_average_distance(self):
        num_robots = len(self.robots)
        center = self.get_robot_center()
        global_total = 0
        for robot in self.robots:
            global_total += abs(robot.x - center[0]) + abs(robot.y - center[1])
        return global_total / num_robots

    def make_map(self):
        cc = Counter((r.x, r.y) for r in self.robots)
        return "\n".join(
            "".join(
                str(cc[(x, y)]) if cc[(x, y)] >= 1 else "." for x in range(self.width)
            )
            for y in range(self.height)
        )


def process_input(input, width, height):
    return [Robot(*p, *v) for p, v in parse_input(input)]


def part1(input, width, height):
    robots = [Robot(*p, *v) for p, v in parse_input(input)]
    area = Area(width, height, robots)
    area.move_all(100)
    return area.get_safety_score()


def part2(instr, width, height):
    robots = [Robot(*p, *v) for p, v in parse_input(instr)]
    area = Area(width, height, robots)
    avg_dist = []
    for t in range(10000):
        avg_dist.append((area.calculate_average_distance(), t))
        area.move_all(1)
    lowest_dist_time = min(avg_dist)[1]
    robots = [Robot(*p, *v) for p, v in parse_input(instr)]
    area = Area(width, height, robots)
    area.move_all(lowest_dist_time)
    print(area.make_map())
    print("-" * 100)
    print(lowest_dist_time)


# ----------------------------------------------------------------------------

with open("14.in") as f:
    instr = f.read()


print(f"part1: {part1(instr, 101, 103)}")
print("part2:")
part2(instr, 101, 103)
