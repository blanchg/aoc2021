import os

(file, _) = os.path.splitext(os.path.basename(__file__))
# f = open(f"{file}sample.txt", "r")
f = open(f"{file}.txt", "r")
lines = []
for rawline in f:
    line = str.strip(rawline)
    lines.append(line)

fish = [int(l) for l in lines[0].split(',')]

for day in range(80):
    oldfish = fish.copy()
    for i,f in enumerate(oldfish):
        if f == 0:
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1


print(len(fish))