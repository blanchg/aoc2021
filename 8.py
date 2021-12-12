import os

(file, _) = os.path.splitext(os.path.basename(__file__))
# f = open(f"{file}sample.txt", "r")
f = open(f"{file}.txt", "r")
lines = []
for rawline in f:
    line = str.strip(rawline)
    lines.append(line)

total = 0
for line in lines:
    nums = str.strip(line.split("|")[1]).split(" ")
    for num in nums:
        if len(num) in [2,4,7,3]:
            total += 1

print(total)


lookup = {
    'a': 0b01000000,
    'b': 0b00100000,
    'c': 0b00010000,
    'd': 0b00001000,
    'e': 0b00000100,
    'f': 0b00000010,
    'g': 0b00000001
}

def strToBin(sig : str) -> int:
    total = 0
    for c in sig:
        total += lookup[c]
    return total

total = 0
for line in lines:
    parts = line.split("|")
    signals = [strToBin(signal) for signal in str.strip(parts[0]).split(" ")]
    nums = [strToBin(num) for num in str.strip(parts[1]).split(" ")]

    resolved = [None] * 10
    segments = {
        't' : 0,
        'tr': 0,
        'br': 0,
        'b' : 0,
        'bl': 0,
        'tl': 0,
        'm' : 0,
    }

    for signal in signals:
# (2) = 1
        if bin(signal).count("1") == 2:
            resolved[1] = signal
# (3) = 7
        elif bin(signal).count("1") == 3:
            resolved[7] = signal
# (4) = 4
        elif bin(signal).count("1") == 4:
            resolved[4] = signal
# (7) = 8
        elif bin(signal).count("1") == 7:
            resolved[8] = signal
# 7 ^ 1 = b0
    segments['t'] = resolved[7] & ~resolved[1]
# where 8^(6)^1 == 0 = 6
    for signal in signals:
        if bin(signal).count("1") == 6:
            if not resolved[8] & ~signal & ~resolved[1]:
                if resolved[6]:
                    print('err6', bin(signal), bin(segments['bl']))
                resolved[6] = signal
# 8 ^ 6 = b1
    segments['tr'] = resolved[8] & ~resolved[6]
# 1 ^ b1 = b2
    segments['br'] = resolved[1] & ~segments['tr']
# (5) ^ b1 = 5
    for signal in signals:
        if bin(signal).count("1") == 5:
            if not signal & segments['tr']:
                resolved[5] = signal
# 8 ^ 5 ^ 1 = b4
    segments['bl'] = resolved[8] & ~resolved[5] & ~resolved[1]
# (5) ^ b2 = 2
    for signal in signals:
        if bin(signal).count("1") == 5:
            if not signal & segments['br']:
                resolved[2] = signal
# (5) ^ b4 ^ b2 = 3
    for signal in signals:
        if bin(signal).count("1") == 5:
            if signal != resolved[2] and signal != resolved[5]:
                resolved[3] = signal
# (6) ^ b4 = 9
    for signal in signals:
        if bin(signal).count("1") == 6:
            if signal ^ segments['bl'] == resolved[8]:
                resolved[9] = signal
# any item not in resolved = 0
    for signal in signals:
        if bin(signal).count("1") == 6:
            if signal not in resolved:
                if resolved[0]:
                    print('err0', bin(signal))
                resolved[0] = signal
# 8 - 0 = b6
    segments['m'] = resolved[8] & ~resolved[0]
# 4 ^ 3 = b5
    segments['tl'] = resolved[4] & ~resolved[3]
# 3 - 4 ^ b0 ^ b5 = b3
    segments['b'] = resolved[3] & ~resolved[4] & ~segments['t'] & ~segments['b']

    numLookup = {}
    for val,b in enumerate(resolved):
        numLookup[b] = val
    result = ""
    for num in nums:
        result += str(numLookup[num])

    total += int(result)
    print(result)


print('===================')
print(total)
# 1 = 2
# 4 = 4
# 8 = 7
# 7 = 3

# 0 = top           7-1
# 1 = right top     8-6-1 = 0 -> 8-6
# 2 = right bottom  
# 3 = bottom
# 4 = left bottom   6 - 9 = 1
# 5 = left top      
# 6 = middle        0 - 1 = 4 -> 8-0




# 1 =     1 | 2                    x  2
# 7 = 0 | 1 | 2 |   |   |   |      x  3
# 4 =     1 | 2 |   |   | 5 | 6    x  4
# 3 = 0 | 1 | 2 | 3 |   |   | 6    x  5
# 2 = 0 | 1 |   | 3 | 4 |   | 6    x  5
# 5 = 0 |   | 2 | 3 |   | 5 | 6    x  5
# 9 = 0 | 1 | 2 | 3 |   | 5 | 6    x  6
# 6 = 0 |   | 2 | 3 | 4 | 5 | 6    x  6
# 0 = 0 | 1 | 2 | 3 | 4 | 5 |      x  6
# 8 = 0 | 1 | 2 | 3 | 4 | 5 | 6    x  7

# 7 = b01110000
# 3 = b01111001
# 8 = b01111111
# 9 = b01111011
# 2 = b01101101
# 5 = b01011011
# 6 = b01011111
# 1 = b00110000
# 4 = b00110011
# 0 = b01111110





# 4 - 7    =        5 6
# 7 - 1    =  0
# 7 - 4    =  0
# 8 - 1    =  0 3 4 5 6
# 8 - 4    =  0 3 4
# 8 - 7    =    3 4 5 6
  
