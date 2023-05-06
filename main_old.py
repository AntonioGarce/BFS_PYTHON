import heapq
from collections import defaultdict
import re
import sys


def shortest_path(start, end, transit_lines):
    # Create adjacency list for villages
    graph = defaultdict(list)
    for line in transit_lines:
        v1, v2, color, type = line.split(' ')
        graph[v1].append((v2, color, type))
        graph[v2].append((v1, color, type))

    # Breadth-First Search (BFS)
    visited = set()
    queue = [(start, [])]

    while queue:
        current, path = queue.pop(0)
        if current == end:
            # Found the end village, return the path
            return ' '.join(path + [current])

        visited.add(current)

        for neighbor, color, type in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [current]))

    # No path found
    return "NO PATH"


def readInput(fileName):
    with open(fileName) as file_in:
        lines = []
        for line in file_in:
            lines.append(line.strip('\n'))
    return lines


def model_input(input_lines):
    transit_lines = []
    line = re.split(' ', input_lines[0])
    villages = int(line[0])
    transit_lines_count = int(line[1])
    start = line[2]
    end = line[3]
    return villages, transit_lines_count, start, end, input_lines[1:]


input_lines = readInput('/autograder/submission/main.py')
_, _, start, end, transit_lines = model_input(input_lines)
path = shortest_path(start, end, transit_lines=transit_lines)
print(path)
