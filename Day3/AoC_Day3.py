"""
Advent of Code 2015 Day 1
"""
from collections import defaultdict
from collections import namedtuple

with open('puzzel.txt') as f:
    moves = tuple(f.read())

# moves = ('>',)
# moves = ('^', '>', 'v', '<')
# moves = ('^', 'v', '^', 'v', '^', 'v', '^', 'v', '^', 'v')

visitedHouses = defaultdict(lambda: 0)
p= {'x': 0, 'y': 0}

for move in moves:
    if move is '<':
        p['x'] -= 1
    elif move is '>':
        p['x'] += 1
    elif move is '^':
        p['y'] += 1
    elif move is 'v':
        p['y'] -= 1
    else:
        continue
    visitedHouses[(p['x'], p['y'])] += 1

print(len(visitedHouses))
