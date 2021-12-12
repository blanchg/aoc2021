import os
import itertools
import collections
import time
start = time.time()
(file, _) = os.path.splitext(os.path.basename(__file__))
# f = open(f"{file}sample.txt", "r")
f = open(f"{file}.txt", "r")
lines = []
for rawline in f:
    line = str.strip(rawline)
    lines.append(line)

fish = [int(l) for l in lines[0].split(',')]
fish.sort()

numdict = collections.defaultdict(int)

for k,g in itertools.groupby(fish, lambda k: k):
    numdict[k] = len(list(g))

def count(dict):
    c = 0
    for k in numdict.keys():
        c += numdict[k]
    return c

for day in range(256):
    print(day, count(numdict), numdict)
    newdict = collections.defaultdict(int)
    for i,f in enumerate(numdict.keys()):
        if f == 0:
            newdict[8] += numdict[f]
            newdict[6] += numdict[f]
        else:
            newdict[f-1] += numdict[f]
    numdict = newdict

print(count(numdict))
print(time.time() - start)