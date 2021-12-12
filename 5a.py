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
    # if input[0][0] != input[1][0] and input[0][1] != input[1][1]:
    #     continue
    print(input)
    ystep = 1
    xstep = 1
    if input[0][0] == input[1][0]:
        x = input[0][0]
        yfrom = input[0][1]
        yto = input[1][1]
        ystep = 1 if yfrom < yto else -1
        yto += ystep
        print(f'[{x}][{yfrom},{yto},{ystep}]')
        for y in range(yfrom,yto,ystep):
            board[y][x] += 1
            if board[y][x] == 2:
                count += 1;


    elif input[0][1] == input[1][1]:
        y = input[0][1]
        xfrom = input[0][0]
        xto = input[1][0]
        xstep = 1 if xfrom < xto else -1
        xto += xstep
        print(f'[{xfrom},{xto},{xstep}][{y}')
        for x in range(xfrom,xto,xstep):
            board[y][x] += 1
            if board[y][x] == 2:
                count += 1;
    else:
        xfrom = input[0][0]
        xto = input[1][0]
        xstep = 1 if xfrom < xto else -1
        xto += xstep

        yfrom = input[0][1]
        yto = input[1][1]
        ystep = 1 if yfrom < yto else -1
        yto += ystep
        y = yfrom

        print(f'[{xfrom, xto, xstep}][{yfrom},{yto},{ystep}]')

        for x in range(xfrom, xto, xstep):
            board[y][x] += 1
            if board[y][x] == 2:
                count += 1;
            y += ystep

for b in board:
    print(b)
print(count)