import os

(file, _) = os.path.splitext(os.path.basename(__file__))
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
    board_sum = 0
    for y in range(5):
        for x in range(5):
            if board[y][x] not in called:
                board_sum += board[y][x]
    return board_sum

called = numbers[:4]
pos = 4
won = None
while not won:
    lastcalled = numbers[pos]
    called.append(lastcalled)
    for board in boards:
        if wins(board, called):
            won = board
            break
    pos += 1
    
print(called)
print(won)
print(score(won), lastcalled)
print(score(won) * lastcalled)
