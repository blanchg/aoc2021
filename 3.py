import os

(file, _) = os.path.splitext(os.path.basename(__file__))
f = open(f"{file}.txt", "r")
l = 0
zeros = []
ones = []
for rawline in f:
    if l == 0:
        l = len(rawline) - 1
        for i in range(l):
            zeros.append(0)
            ones.append(0)
    
    line = str.strip(rawline)
    for i, c in enumerate(rawline):
        if c == "0":
            zeros[i] = zeros[i] + 1
        elif c == "1":
            ones[i]+=1
    
bits = ""
nbits = ""
for i in range(l):
    if zeros[i] > ones[i]:
        bits = bits + "0"
        nbits = nbits + "1"
    else:
        bits = bits + "1"
        nbits = nbits + "0"

gamma = int(bits, 2)
eps = int(nbits, 2)
print (bits, nbits)
print(gamma, eps)

print(gamma * eps)

