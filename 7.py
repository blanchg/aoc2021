import os
import math

(file, _) = os.path.splitext(os.path.basename(__file__))
# f = open(f"{file}sample.txt", "r")
f = open(f"{file}.txt", "r")
lines = []
for rawline in f:
    line = str.strip(rawline)
    lines.append(line)

pos = [int(p) for p in lines[0].split(',')]

minp = min(pos)
maxp = max(pos)

mincost = 500000000
minpos = 0
for i in range(minp, maxp + 1):
    s = sum([abs(p - i) for p in pos])
    if s < mincost:
        mincost = s
        minpos = i

print(minpos, mincost)

mincost = 50000000000000
minpos = 0
for i in range(minp, maxp + 1):
    s = sum([((abs(p - i) + 1) * (abs(p - i))) / 2 for p in pos])
    if s < mincost:
        mincost = s
        minpos = i


print(minpos, int(mincost))