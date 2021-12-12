import os

(file, _) = os.path.splitext(os.path.basename(__file__))
# f = open(f"{file}sample.txt", "r")
f = open(f"{file}.txt", "r")
lines = []
for rawline in f:
    line = str.strip(rawline)
    lines.append(line)



inputs = []
maxval = 0
for line in lines:
    parts = line.split(" -> ")
    parta = parts[0].split(",")
    partb = parts[1].split(",")
    xa = int(parta[0])
    ya = int(parta[1])
    xb = int(partb[0])
    yb = int(partb[1])
    inputs.append(((xa,ya), (xb, yb)))
    maxval = max(maxval, xa, ya, xb, yb)

maxval += 1
board = []
for y in range(maxval):
    board.append([])
    for x in range(maxval):
        board[y].append(0)

count = 0

for input in inputs:
    if input[0][0] != input[1][0] and input[0][1] != input[1][1]:
        continue

    ystep = 1
    xstep = 1
    if input[0][0] == input[1][0]:
        if input[0][1] >= input[1][1]:
            input = (input[0], (input[1][0] + 1, input[1][1] - 1))
            ystep = -1
        else:
            input = (input[0], (input[1][0] + 1, input[1][1] + 1))
            ystep = 1

    if input[0][1] == input[1][1]:
        if input[0][0] >= input[1][0]:
            input = (input[0], (input[1][0] - 1, input[1][1] + 1))
            xstep = -1
        else:
            input = (input[0], (input[1][0] + 1, input[1][1] + 1))
            xstep = 1
            
    for y in range(input[0][1], input[1][1], ystep):
        for x in range(input[0][0], input[1][0], xstep):
            board[y][x] += 1
            if board[y][x] == 2:
                count += 1;
print(board)
print(count)