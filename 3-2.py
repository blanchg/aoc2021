import os

(file, _) = os.path.splitext(os.path.basename(__file__))
f = open(f"{file}.txt", "r")
l = 0
zeros = []
ones = []
lines = []
for rawline in f:
    
    line = str.strip(rawline)
    if l == 0:
        l = len(line)
        for i in range(l):
            zeros.append(0)
            ones.append(0)
    lines.append(line)

def onesWin(i, lines):
    
    zeros = 0
    ones = 0
    for line in lines:
        c = line[i]
        if c == "0":
            zeros = zeros + 1
        elif c == "1":
            ones = ones + 1

    return ones >= zeros

onesLines = lines.copy()
bit = 0
while len(onesLines) > 1:
    if onesWin(bit, onesLines):
        onesLines = [line for line in onesLines if line[bit] == "1"]
    else:
        onesLines = [line for line in onesLines if line[bit] == "0"]
    bit+=1
    print(onesLines)

zerosLines = lines.copy()
bit = 0
while len(zerosLines) > 1:
    if onesWin(bit, zerosLines):
        zerosLines = [line for line in zerosLines if line[bit] == "0"]
    else:
        zerosLines = [line for line in zerosLines if line[bit] == "1"]
    bit+=1
    print(zerosLines)

oxy = int(onesLines[0], 2)
co2 = int(zerosLines[0], 2)
print(oxy, co2)
print(oxy * co2)

# bits = ""
# nbits = ""
# for i in range(l):
#     if zeros[i] > ones[i]:
#         bits = bits + "0"
#         nbits = nbits + "1"
#     else:
#         bits = bits + "1"
#         nbits = nbits + "0"



# gamma = int(bits, 2)
# eps = int(nbits, 2)
# print (bits, nbits)
# print(gamma, eps)

# print(gamma * eps)

