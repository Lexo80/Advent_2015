"""
Advent of code day2 part 2
"""
from collections import namedtuple
dims = namedtuple('Dimensions', 'length width height')

with open('puzzel2.txt') as f:
    stream = f.read().split('\n')


prestents = [dims(*(int(i) for i in line.split('x'))) for line in stream]
# intlist = [tuple(int(i) for i in line.split('x')) for line in stream]
# print(intlist)
# x = intlist[0]
# print(x.height)


# intlist=[(1,1,10)]
# intlist=[(2,3,4)]
answer = 0
for t in prestents:
    a, b, c = sorted(t)
    answer += 2 * (a + b) + a * b * c
print(answer)
