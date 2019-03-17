# -*- coding: utf-8 -*-
"""
Advent of Code 2015 day 1
computes the floor where the instructions take Santa
instructions are given by text file AoC_2015_1.txt
"""
f = open('AoC_2015_1.txt')
data = f.read()
number=0
for line in data:    
    if '(' in line:
        number += 1
    elif ')' in line:
        number -=1
print('nummer: ' + str(number))
f.close()
    