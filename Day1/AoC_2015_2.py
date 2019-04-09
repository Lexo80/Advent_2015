"""
Advent of code
Day 1 star 2
"""
with open('puzzle2.txt') as f:
    data = f.read()
    floor = 0
    index =0
    for element in data:
        index +=1
        if element == '(':
            floor +=1
        elif element == ')':
            floor -=1
        if floor == -1:
            break
    print(index)