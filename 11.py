import os
import collections

(file, _) = os.path.splitext(os.path.basename(__file__))
# f = open(f"{file}sample.txt", "r")
f = open(f"{file}.txt", "r")
lines = []
for rawline in f:
    line = str.strip(rawline)
    lines.append(line)
total = 0


def neighboursIndex(grid,i):
    x = i % grid.width
    y = int(i / grid.width)
    xfrom = max(0, x- 1)
    xto = min(grid.width, x+2)
    yfrom = max(0, y-1)
    yto = min(int(len(grid)/grid.width), y+2)
    results = []
    for y1 in range(yfrom, yto):
        for x1 in range(xfrom, xto):
            i1 = y1 * grid.width + x1
            if i1 == i:
                continue
            results.append(i1)
    return results

class Grid(list):
    width = 0

grid = Grid()
for line in lines:
    grid.width = len(line)
    for o in line:
        grid.append(int(o))

def flash(grid):
    flashes = 0
    toflash = collections.deque()
    for i,o in enumerate(grid):
        if o == 10:
            toflash.append(i)

    while toflash:
        flashes += 1
        f = toflash.popleft()
        n = neighboursIndex(grid, f)
        for ni in n:
            grid[ni] += 1
            if grid[ni] == 10:
                toflash.append(ni)
                
    return flashes

allflash = 0

def step(grid, step):
    global total, allflash
    # inc
    for i,o in enumerate(grid):
        grid[i] = o + 1
    # flash
    flashes = flash(grid)
    total += flashes
    if flashes == len(grid):
        allflash = step + 1
    # reset
    for i,o in enumerate(grid):
        if o > 9:
            grid[i] = 0
    return grid

def debug(grid):
    for i, o in enumerate(grid):
        if i % grid.width == 0:
            print('')
        print(f'{o},', end='')

    print('')

debug(grid)
part1 = 0
for i in range(0, 1000):
    print(f'Step: {i}')
    grid = step(grid, i)
    if (i == 99):
        part1 = total
    if allflash:
        break
debug(grid)

print('Part 1:', part1)
print('Part 2:', allflash)