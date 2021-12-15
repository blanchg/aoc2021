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

for line in lines:
    pass

print('Part 1:', total)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()


print('Part 2:', total)
print("--- %s seconds ---" % (time.time() - start_time))