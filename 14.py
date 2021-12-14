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

template = lines[0]
compounds = {}
uniqueParts = set(template)
for line in lines[2:]:
    a,b = line.split(" -> ")
    uniqueParts.add(b)
    compounds[a] = b

for step in range(0,10):
    newtemplate = []
    i2 = 0
    for i in range(0, len(template) - 1):
        i2 = i + 1
        part = template[i] + template[i2]
        newtemplate.append(template[i])
        newtemplate.append(compounds[part])
    newtemplate.append(template[i2])
    template = "".join(newtemplate)

counts = {}
minc = 100000
maxc = 0
for p in uniqueParts:
    val = sum([1 if t == p else 0 for t in template])
    counts[p] = val
    if val < minc:
        minc = val
    if val > maxc:
        maxc = val

print('Part 1:', maxc - minc)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

template = list(lines[0])
counts = collections.defaultdict(int)
origlen = len(template)
minc = float('inf')
maxc = 0

cache = {}

def add(a, b):
    c = collections.defaultdict(int)
    for p in uniqueParts:
        c[p] = a[p] + b[p]
    return c

hit = 0
miss = 0
def polymer(a,b,steps):
    global hit, miss
    if steps == 0:
        return None
    key = a+b+str(steps)
    if key in cache:
        hit+=1
        return cache[key]
    miss+=1
    c = compounds[a+b]
    left = polymer(a,c,steps - 1)
    right = polymer(c,b,steps - 1)
    if left and right:
        counts = add(left, right)
    else:
        counts = collections.defaultdict(int)
    counts[c] += 1
    cache[key] = counts
    return counts

for i in range(0, origlen - 1):
    a = template[i]
    b = template[i + 1]
    counts = add(counts, polymer(a,b,40))
    counts[template[i]] += 1
counts[template[-1]] += 1
print(template[0])
print(template[-1])
print(counts)
s = sorted(counts.values())
maxc = s[-1]
minc = s[0]
print('hit', hit, 'miss', miss)
print(s)
print('Part 2:', maxc - minc)
print("--- %s seconds ---" % (time.time() - start_time))