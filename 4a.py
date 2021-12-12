import os

(file, _) = os.path.splitext(os.path.basename(__file__))
# f = open(f"{file}sample.txt", "r")
f = open(f"{file}.txt", "r")
lines = [str.strip(line) for line in f]
numbers = [int(num) for num in lines[0].split(",")]
boards = []
board = None
for line in lines[1:]:
    if not line:
        if board:
            boards.append(board)
        board = []
    else:
        board.append([int(str.strip(num)) for num in line.split(" ") if str.strip(num)])

boards.append(board)

def wins(board, called):
    for y in range(5):
        winner = True
        for x in range(5):
            if board[y][x] not in called:
                winner = False
                break;
        if winner:
            return True
    for x in range(5):
        winner = True
        for y in range(5):
            if board[y][x] not in called:
                winner = False
                break;
        if winner:
            return True
    return False

def score(won):
    return sum( [sum([num for num in row if num not in called]) for row in board])

called = numbers[:4]
pos = 4
lastwon = None
while len(boards) > 0:
    lastcalled = numbers[pos]
    called.append(lastcalled)
    nextboards = []
    for board in boards:
        if not wins(board, called):
            nextboards.append(board)
            lastwon = board
        
    boards = nextboards
    pos += 1
won = lastwon
sumnotcalled = score(won)
print(sumnotcalled, lastcalled)
print(sumnotcalled * lastcalled)
