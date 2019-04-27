"""
Advent of Code 2015 Day 1
"""
from collections import defaultdict

with open('puzzel.txt') as f:
    moves = tuple(f.read())
santa = []
robosanta = []
for i, m in enumerate(moves):
    if i % 2 is 0:
        santa.append(m)
    else:
        robosanta.append(m)

print(f'länge von santasliste: {len(santa)} länge robo: {len(robosanta)}')


# moves = ('>',)
# moves = ('^', '>', 'v', '<')
# moves = ('^', 'v', '^', 'v', '^', 'v', '^', 'v', '^', 'v')

visitedHouses = defaultdict(lambda: 0)
p = {'x': 0, 'y': 0}

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

# part 2 with robo santas help

santas_point = {'x': 0, 'y': 0}
robos_point = {'x': 0, 'y': 0}
santasHouses = defaultdict(lambda: 0)
roboHouses = defaultdict(lambda: 0)


for s, r in zip(santa, robosanta):
    if s is '<':
        santas_point['x'] -= 1
    elif s is '>':
        santas_point['x'] += 1
    elif s is '^':
        santas_point['y'] += 1
    elif s is 'v':
        santas_point['y'] -= 1

    if r is '<':
        robos_point['x'] -= 1
    elif r is '>':
        robos_point['x'] += 1
    elif r is '^':
        robos_point['y'] += 1
    elif r is 'v':
        robos_point['y'] -= 1
    santasHouses[(santas_point['x'], santas_point['y'])] += 1
    roboHouses[(robos_point['x'], robos_point['y'])] += 1

allHouses = santasHouses
allHouses.update(roboHouses)
print(len(allHouses))