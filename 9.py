import os
import math
import collections

(file, _) = os.path.splitext(os.path.basename(__file__))
# f = open(f"{file}sample.txt", "r")
f = open(f"{file}.txt", "r")
lines = []
for rawline in f:
    line = str.strip(rawline)
    lines.append(line)
total = 0

def neighbours(grid,x,y):
    xfrom = max(0, x- 1)
    xto = min(len(grid[0]), x+2)
    yfrom = max(0, y-1)
    yto = min(len(grid), y+2)
    results = []
    for x1 in range(xfrom, xto):
        if x1 == x:
            continue
        results.append(grid[y][x1])
    for y1 in range(yfrom, yto):
        if y1 == y:
            continue
        results.append(grid[y1][x])
    return results
    
grid = []
for line in lines:
    grid.append([int(num) for num in line])
    
w = len(grid[0])

def neighboursIndex(grid,x,y):
    xfrom = max(0, x- 1)
    xto = min(len(grid[0]), x+2)
    yfrom = max(0, y-1)
    yto = min(len(grid), y+2)
    results = collections.deque()
    for x1 in range(xfrom, xto):
        if x1 == x:
            continue
        results.append(y * w + x1)
    for y1 in range(yfrom, yto):
        if y1 == y:
            continue
        results.append(y1 * w + x)
    return results

def is_low(num, neighbours):
    return all([num < n for n in neighbours])

print(neighboursIndex(grid,9,1))

for y, row in enumerate(grid):
    for x, num in enumerate(row):
        if is_low(num, neighbours(grid, x, y)):
            total += num + 1
print(total)

gridi = []
for y, row in enumerate(grid):
    for x, num in enumerate(row):
        gridi.append(num)

hashome = []
basins = []
for y, row in enumerate(grid):
    for x, num in enumerate(row):
        i = y * w + x
        if num == 9 or i in hashome:
            continue
        basin = [i]
        hashome.append(i)
        basins.append(basin)
        todo = neighboursIndex(grid, x, y)
        while len(todo):
            i1 = todo.popleft()
            n = gridi[i1]
            if n == 9 or i1 in hashome:
                continue
            y1 = math.floor(i1 / w)
            x1 = i1 % w
            basin.append(i1)
            hashome.append(i1)
            for n2 in neighboursIndex(grid, x1, y1):
                if n2 not in todo and n2 not in hashome:
                    todo.append(n2)

print(basins)
total = 1
for b in sorted([len(b) for b in basins], reverse=True)[:3]:
    print(b)
    total *= b

print(total)
            
