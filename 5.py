from collections import defaultdict, deque

example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

def process(inputstr: str):
    rules = {}
    pagelists = []
    inputstr = inputstr.splitlines()
    section_sep = inputstr.index("")
    for line in range(section_sep):
        lhs, rhs = (int(x) for x in inputstr[line].split("|"))
        if lhs not in rules:
            rules[lhs] = []
        rules[lhs].append(rhs)
    for line in range(section_sep+1,len(inputstr)):
        pagelists.append([int(x) for x in inputstr[line].split(",")])
    return rules, pagelists

def check_pagelist(rules, pagelist):
    retval = True
    for i in range(len(pagelist)):
        if pagelist[i] in rules:
            for pre in rules[pagelist[i]]:
                if pre in pagelist[:i]:
                    retval = False
    return retval

def part1(rules, pagelists):
    retval = 0
    for pagelist in pagelists:
        if check_pagelist(rules, pagelist):
           retval += pagelist[len(pagelist)//2]
    return retval

def toposort(rules):
    edges = [[(v,k) for v in rules[k]] for k in rules]
    edges = [item for sublist in edges for item in sublist]
    vertices = set()
    for k,v in rules.items():
        vertices.add(k)
        vertices = vertices.union(set(v))
    # Initialize the graph
    vertices
    graph = defaultdict(list)
    in_degree = {v: 0 for v in vertices}

    # Build the graph and calculate in-degrees
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Collect all nodes with in-degree of 0
    queue = deque([v for v in vertices if in_degree[v] == 0])
    topological_order = []

    while queue:
        current = queue.popleft()
        topological_order.append(current)

        # Reduce the in-degree of neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycles
    if len(topological_order) != len(vertices):
        raise ValueError("Graph contains a cycle; topological sort is not possible.")

    return topological_order

def part2(rules, pagelists):
    retval = 0
    for pagelist in pagelists:
        if not check_pagelist(rules, pagelist):
            subrules = {k: [vi for vi in v if vi in pagelist] for k,v in rules.items() if k in pagelist}
            order = list(reversed(toposort(subrules)))
            retval += order[len(order)//2]
    return retval

part1(*process(example))

with open("5.in") as f:
    intxt = f.read()
    
print(part1(*process(intxt)))

print(part2(*process(intxt)))
