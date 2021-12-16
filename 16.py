from io import TextIOWrapper
import os
import collections
import math
import time
from typing import Tuple
start_time = time.time()

(file, _) = os.path.splitext(os.path.basename(__file__))
# f = open(f"{file}sample.txt", "r")
f = open(f"{file}.txt", "r")
total = 0

# VVV
# TTT

# VVV == 100 = 4 = Literal number
# group of 5 bits with 1st bit being continuation
# all bits is literal number

# VVV == 110 = 6 = Operator
# I == 0 = 15 bits total length sub packets
# I == 1 = 11 bits number of sub packets

def toint(bits):
    value = 0
    l = len(bits) - 1
    for i,b in enumerate(bits):
        value += int(b) << l - i
    return value

class BitStream():
    buffer = []
    def __init__(self, f:TextIOWrapper) -> None:
        self.f = f

    def chomp(self):
        data = self.f.read(1)
        if not data:
            raise EOFError("EOF")
        bits = f"{int(data, 16):04b}"
        self.buffer.extend(bits)

    def readint(self, n:int) -> int:
        bits = self.readbits(n)
        return toint(bits)

    def readbits(self, n:int) -> list:
        while len(self.buffer) < n:
            self.chomp()
        bits = self.popleft(n)
        return bits

    def popleft(self, n):
        value = self.buffer[:n]
        self.buffer = self.buffer[n:]
        return value


s = BitStream(f)
total = 0
def readpacket(s, indent=0) -> Tuple[int, int]:
    global total
    bitsread = 0
    version = s.readint(3)
    bitsread += 3
    total += version
    ptype = s.readint(3)
    bitsread += 3
    if ptype != 4:
        print(' '*indent,'op',ptype, 'v:', version)
    value = 0
    if ptype == 4:
        valuebits = []
        while True:
            bits = s.readbits(5)
            bitsread += 5
            valuebits += bits[1:]
            if bits[0] == '0':
                break
        value = toint(valuebits)
        print(' '*indent,'literal', value, 'v:', version)
    else:
        lengthtype = s.readint(1)
        bitsread += 1
        numpackets = 0
        values = []
        if lengthtype == 0: # bits
            toread = s.readint(15)
            bitsread += 15
            while toread:
                (subread, subvalue) = readpacket(s, indent+2)
                values.append(subvalue)
                toread -= subread
                bitsread += subread
                numpackets += 1
        else: # packets
            packets = s.readint(11)
            bitsread += 11
            for i in range(packets):
                (subread, subvalue) = readpacket(s, indent+2)
                values.append(subvalue)
                bitsread += subread
                numpackets += 1
        if ptype == 0:
            value = sum(values)
        elif ptype == 1:
            value = values[0]
            for v in values[1:]:
                value *= v
        elif ptype == 2:
            value = min(values)
        elif ptype == 3:
            value = max(values)
        elif ptype == 5:
            value = 1 if values[0] > values[1] else 0
        elif ptype == 6:
            value = 1 if values[0] < values[1] else 0
        elif ptype == 7:
            value = 1 if values[0] == values[1] else 0
        print(' '*indent,'op', value)
    return (bitsread, value)
(totalread, totalp2) = readpacket(s)

print('Part 1:', total)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()


print('Part 2:', totalp2)
print("--- %s seconds ---" % (time.time() - start_time))