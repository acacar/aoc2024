from itertools import product


example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def process(input):
    return {int(x): [int(y) for y in y.split()] for x,y in [x.split(":") for x in input.splitlines()]}

operators = {
    "+": lambda x,y: x+y,
     "*": lambda x,y: x*y,
     "|": lambda x,y: int(str(x)+str(y))
 }

def part1(input):
    retval = 0
    for k,v in input.items():
        number_of_positions = len(v)-1
        # Generate all possible combinations of operators
        operator_combinations = []
        for ops in product('*+', repeat=number_of_positions):
            operator_combinations.append(''.join(ops))
        for opcombo in operator_combinations:
            stack = [x for x in v]
            stack.reverse()
            for op in opcombo:
                stack.append(operators[op](stack.pop(), stack.pop()))
            if stack[0] == k:
                retval += k
                break        
    return retval
        
def part2(input):
    retval = 0
    for k,v in input.items():
        number_of_positions = len(v)-1
        # Generate all possible combinations of operators
        operator_combinations = []
        for ops in product('*+|', repeat=number_of_positions):
            operator_combinations.append(''.join(ops))
        for opcombo in operator_combinations:
            stack = [x for x in v]
            stack.reverse()
            for op in opcombo:
                stack.append(operators[op](stack.pop(), stack.pop()))
            if stack[0] == k:
                retval += k
                break        
    return retval

with open("7.in") as f:
    input = f.read()


print(f"Part 1: {part1(process(input))}")
print(f"Part 2: {part2(process(input))}")
