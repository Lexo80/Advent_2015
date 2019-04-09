"""
Advent of code 2015
Day 2 part 1
"""
tlist = []
with open('puzzel1.txt') as f:
    data = f.read().splitlines()

for s in data:
    tlist.append(tuple(s.split('x')))
summe = 0
for l, w, h in tlist:
    flaeche = 2 * int(l) * int(w) + 2 * int(w) * int(h) + 2 * \
        int(h) * int(l) + min((int(l)*int(w)), (int(w)*int(h)), (int(h)*int(l)))
    summe += flaeche

print(summe)


