import os
import collections
import math
import time
start_time = time.time()

(file, _) = os.path.splitext(os.path.basename(__file__))
# f = open(f"{file}sample.txt", "r")
f = open(f"{file}.txt", "r")
lines = []
for rawline in f:
    line = str.strip(rawline)
    lines.append(line)
total = 0

w = 0
h = 0
points = []
instructions = []
for line in lines:
    if not line:
        continue
    if str.startswith(line, 'fold'):
        instructions.append(line)
    else:
        x,y = [int(a) for a in line.split(',')]
        w = max(w, x+1)
        h = max(h, y+1)
        points.append((x,y))

grid = ['.'] * (w * h)

for x,y in points:
    i = x + y * w
    grid[i] = '#'

def debug(grid, w):
    for i in range(0, len(grid), w):
        print(' '.join(grid[i:i+w]))

def foldY(grid, fy, w, h):
    grid2 = ['.'] * w * fy
    for y in range(0, h):
        if y == fy:
            continue
        for x in range(0, w):
            i1 = x + y * w
            i2 = i1
            if y > fy:
                y2 = fy + fy - y
                i2 = x + y2 * w
            grid2[i2] = '#' if grid2[i2] == '#' or grid[i1] == '#' else '.'
    return grid2
        
def foldX(grid, fx, w, h):
    grid2 = ['.'] * fx * h
    for y in range(0, h):
        for x in range(0, w):
            if x == fx:
                continue
            i1 = x + y * w
            x2 = x
            if x > fx:
                x2 = fx + fx - x
            i2 = x2 + y * fx
            grid2[i2] = '#' if grid2[i2] == '#' or grid[i1] == '#' else '.'
    return grid2
        
part1 = None
for ins in instructions:
    part,foldpoint = ins.split('=')
    foldpoint = int(foldpoint)
    if part.endswith('x'):
        grid = foldX(grid, foldpoint, w, h)
        w = foldpoint
    else:
        grid = foldY(grid, foldpoint, w, h)
        h = foldpoint
    if not part1:
        part1 = sum([1 if dot == '#' else 0 for dot in grid])

print('Part 1:', part1)
print('Part 2:')
debug(grid, w)

print("--- %s seconds ---" % (time.time() - start_time))