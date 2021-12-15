import os
import collections
import math
import time

(file, _) = os.path.splitext(os.path.basename(__file__))
# f = open(f"{file}sample.txt", "r")
f = open(f"{file}.txt", "r")
lines = []
for rawline in f:
    line = str.strip(rawline)
    lines.append(line)
total = 0


def debug(grid, w):
    for i in range(0, len(grid), w):
        print(''.join(str(grid[i:i+w]).replace(",","")[1:-1]))

start_time = time.time()
grid = []
w = len(lines[0])
h = len(lines)
for line in lines:
    for cost in line:
        grid.append(int(cost))

# debug(grid, w)

def build_path(visited, current):
    path = collections.deque([current])
    while current in visited:
        current = visited[current]
        path.appendleft(current)
    return path

def inf():
    return math.inf

def cost(i, target):
    ix = i % w
    iy = int(i / w)
    tx = target % w
    ty = int(target / w)
    return tx - ix + ty - iy

def minopen(open, fscore):
    m = math.inf
    bestn = -1
    for n in open:
        if fscore[n] < m:
            m = fscore[n]
            bestn = n
    return bestn

def neighboursIndex(i):
    x = i % w
    y = int(i / w)
    xfrom = max(0, x- 1)
    xto = min(w, x+2)
    yfrom = max(0, y-1)
    yto = min(h, y+2)
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

def find_path(grid, start, target):
    open = [start]
    visited = {}
    gscore = collections.defaultdict(inf)
    gscore[start] = 0
    fscore = collections.defaultdict(inf)
    fscore[start] = cost(start, target)

    while open:
        current = minopen(open, fscore)
        if current == target:
            return (fscore[current], build_path(visited, current))
        open.remove(current)
        for n in neighboursIndex(current):
            tentative_gscore = gscore[current] + grid[n]
            if tentative_gscore < gscore[n]:
                visited[n] = current
                gscore[n] = tentative_gscore
                fscore[n] = tentative_gscore + cost(n, target)
                if n not in open:
                    open.append(n)
    return (None, None)

(c, path) = find_path(grid, 0, len(grid) - 1)

print('Part 1:', c, path)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

times = 5
nw = w * times
nh = h * times

def build_grid(times):
    
    newgrid = [0] * (len(grid) * times * times)
    for i in range(0, len(newgrid)):
        x = i % nw
        y = int(i / nw)
        tx = int(x / w)
        ty = int(y / h)
        gx = x % w
        gy = y % h
        gi = gx + gy * w
        val = (grid[gi] + tx + ty)
        if val > 9:
            val = val % 10 + 1
        newgrid[i] = val 
    return newgrid
newgrid = build_grid(times)

w = nw
h = nh
(c, path) = find_path(newgrid, 0, len(newgrid) - 1)

print('Part 2:', c, path)
print("--- %s seconds ---" % (time.time() - start_time))