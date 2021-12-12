f = open("2.txt", "r")
x = 0
depth = 0
aim = 0
for line in f:
    cmd,b = line.split(" ")
    units = int(b)
    if cmd == "forward":
        x += units
        depth += aim * units
    elif cmd == "up":
        aim -= units
    elif cmd == "down":
        aim += units

print(f"${x} ${depth}")
print(x * depth)
